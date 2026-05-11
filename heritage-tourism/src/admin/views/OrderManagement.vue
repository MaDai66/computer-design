<template>
  <div class="order-management">
    <div class="order-header">
      <h2>订单管理</h2>
      <div class="order-actions">
        <div class="search-box">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索订单号/用户..."
          />
          <button class="search-btn">搜索</button>
        </div>
        <div class="filter-box">
          <select v-model="statusFilter">
            <option value="all">全部状态</option>
            <option value="pending">待处理</option>
            <option value="shipped">已发货</option>
            <option value="completed">已完成</option>
            <option value="cancelled">已取消</option>
          </select>
        </div>
      </div>
    </div>

    <!-- 订单列表 -->
    <div class="orders-table">
      <table>
        <thead>
          <tr>
            <th>订单号</th>
            <th>用户</th>
            <th>金额</th>
            <th>商品数量</th>
            <th>状态</th>
            <th>下单时间</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in filteredOrders" :key="order.id">
            <td>{{ order.id }}</td>
            <td>{{ order.user }}</td>
            <td>¥{{ order.amount }}</td>
            <td>{{ order.itemsCount }}</td>
            <td>
              <span :class="['status', order.status]">
                {{ order.statusText }}
              </span>
            </td>
            <td>{{ order.createTime }}</td>
            <td>
              <div class="order-actions">
                <button class="action-btn view" @click="viewOrder(order)">
                  查看
                </button>
                <button class="action-btn edit" @click="editOrderStatus(order)">
                  编辑
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 分页 -->
    <div class="pagination">
      <button class="page-btn" :disabled="currentPage === 1">上一页</button>
      <span class="page-info">
        第 {{ currentPage }} 页，共 {{ totalPages }} 页
      </span>
      <button class="page-btn" :disabled="currentPage === totalPages">下一页</button>
    </div>

    <!-- 订单详情模态框 -->
    <div v-if="showOrderModal" class="modal-overlay" @click="showOrderModal = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>{{ currentOrder ? '订单详情' : '订单信息' }}</h3>
          <button class="close-btn" @click="showOrderModal = false">&times;</button>
        </div>
        <div class="modal-body" v-if="currentOrder">
          <div class="order-detail">
            <div class="detail-section">
              <h4>订单信息</h4>
              <div class="detail-row">
                <span class="detail-label">订单号：</span>
                <span>{{ currentOrder.id }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">用户：</span>
                <span>{{ currentOrder.user }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">下单时间：</span>
                <span>{{ currentOrder.createTime }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">订单状态：</span>
                <select 
                  v-model="currentOrder.status"
                  class="status-select"
                  @change="updateStatusText"
                >
                  <option value="pending">待处理</option>
                  <option value="shipped">已发货</option>
                  <option value="completed">已完成</option>
                  <option value="cancelled">已取消</option>
                </select>
              </div>
              <div class="detail-row">
                <span class="detail-label">总金额：</span>
                <span class="amount">¥{{ currentOrder.amount }}</span>
              </div>
            </div>

            <div class="detail-section">
              <h4>商品信息</h4>
              <div class="order-items">
                <div v-for="item in currentOrder.items" :key="item.id" class="order-item">
                  <div class="item-image">
                    <img :src="item.image" :alt="item.name" />
                  </div>
                  <div class="item-info">
                    <h5>{{ item.name }}</h5>
                    <p class="item-price">¥{{ item.price }}</p>
                    <p class="item-quantity">数量：{{ item.quantity }}</p>
                  </div>
                  <div class="item-subtotal">
                    ¥{{ item.price * item.quantity }}
                  </div>
                </div>
              </div>
            </div>

            <div class="detail-section">
              <h4>收货信息</h4>
              <div class="detail-row">
                <span class="detail-label">收货人：</span>
                <span>{{ currentOrder.shipping.name }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">电话：</span>
                <span>{{ currentOrder.shipping.phone }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">地址：</span>
                <span>{{ currentOrder.shipping.address }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" @click="showOrderModal = false">关闭</button>
          <button class="btn btn-primary" @click="saveOrderChanges">保存更改</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { adminAPI } from '../api/adminAPI'

const searchQuery = ref('')
const statusFilter = ref('all')
const currentPage = ref(1)
const totalPages = ref(1)
const showOrderModal = ref(false)
const currentOrder = ref(null)
const isLoading = ref(false)

// 订单数据
const orders = ref([])

// 过滤订单
const filteredOrders = computed(() => {
  let result = orders.value
  
  // 状态过滤
  if (statusFilter.value !== 'all') {
    result = result.filter(order => order.status === statusFilter.value)
  }
  
  // 搜索过滤
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(order => 
      order.id.toLowerCase().includes(query) ||
      order.user.toLowerCase().includes(query)
    )
  }
  
  return result
})

// 加载订单数据
const loadOrders = async () => {
  isLoading.value = true
  try {
    const response = await adminAPI.orders.getList({
      search: searchQuery.value,
      status: statusFilter.value === 'all' ? '' : statusFilter.value,
      page: currentPage.value
    })
    orders.value = response.results || []
    totalPages.value = response.total_pages || 1
  } catch (error) {
    console.error('加载订单失败:', error)
  } finally {
    isLoading.value = false
  }
}

// 查看订单详情
const viewOrder = async (order) => {
  try {
    const response = await adminAPI.orders.getDetail(order.id)
    currentOrder.value = response
    showOrderModal.value = true
  } catch (error) {
    console.error('加载订单详情失败:', error)
  }
}

// 编辑订单状态
const editOrderStatus = (order) => {
  viewOrder(order)
}

// 更新状态文本
const updateStatusText = () => {
  if (currentOrder.value) {
    const statusMap = {
      'pending': '待处理',
      'shipped': '已发货',
      'completed': '已完成',
      'cancelled': '已取消'
    }
    currentOrder.value.statusText = statusMap[currentOrder.value.status]
  }
}

// 保存订单更改
const saveOrderChanges = async () => {
  if (currentOrder.value) {
    try {
      await adminAPI.orders.updateStatus(currentOrder.value.id, currentOrder.value.status)
      showOrderModal.value = false
      // 重新加载数据
      loadOrders()
    } catch (error) {
      console.error('保存订单更改失败:', error)
    }
  }
}

// 搜索
const handleSearch = () => {
  currentPage.value = 1
  loadOrders()
}

// 状态过滤
const handleStatusFilter = () => {
  currentPage.value = 1
  loadOrders()
}

// 分页
const handlePageChange = (page) => {
  currentPage.value = page
  loadOrders()
}

onMounted(() => {
  // 初始加载订单数据
  loadOrders()
})
</script>

<style scoped>
.order-management {
  width: 100%;
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.order-header h2 {
  margin: 0;
  color: #333;
  font-size: 24px;
}

.order-actions {
  display: flex;
  gap: 15px;
  align-items: center;
}

.search-box {
  display: flex;
  gap: 10px;
}

.search-box input {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.search-btn {
  padding: 8px 16px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.filter-box select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  background: white;
}

/* 订单列表 */
.orders-table {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 30px;
}

.orders-table table {
  width: 100%;
  border-collapse: collapse;
}

.orders-table th,
.orders-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.orders-table th {
  background: #f5f7fa;
  font-weight: 600;
  color: #333;
}

.orders-table tr:hover {
  background: #f9f9f9;
}

.status {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.status.pending {
  background: #fff3e0;
  color: #ff9800;
}

.status.shipped {
  background: #e3f2fd;
  color: #2196f3;
}

.status.completed {
  background: #e8f5e8;
  color: #4caf50;
}

.status.cancelled {
  background: #ffebee;
  color: #e53935;
}

.order-actions {
  display: flex;
  gap: 8px;
}

.action-btn {
  padding: 4px 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  transition: background-color 0.3s;
}

.action-btn.view {
  background: #3498db;
  color: white;
}

.action-btn.view:hover {
  background: #2980b9;
}

.action-btn.edit {
  background: #f39c12;
  color: white;
}

.action-btn.edit:hover {
  background: #e67e22;
}

/* 分页 */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
}

.page-btn {
  padding: 6px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;
}

.page-btn:hover:not(:disabled) {
  background: #f5f7fa;
  border-color: #3498db;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  font-size: 14px;
  color: #666;
}

/* 模态框 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 8px;
  padding: 20px;
  width: 100%;
  max-width: 800px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.modal-header h3 {
  margin: 0;
  color: #333;
  font-size: 18px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #999;
}

.order-detail {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.detail-section {
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 15px;
}

.detail-section h4 {
  margin: 0 0 15px 0;
  color: #333;
  font-size: 16px;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
}

.detail-row {
  display: flex;
  gap: 15px;
  margin-bottom: 10px;
  align-items: center;
}

.detail-label {
  width: 100px;
  color: #666;
  font-weight: 500;
  flex-shrink: 0;
}

.status-select {
  padding: 6px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.amount {
  color: #e74c3c;
  font-weight: 600;
}

.order-items {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.order-item {
  display: flex;
  gap: 15px;
  padding: 10px;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
  align-items: center;
}

.item-image {
  width: 80px;
  height: 80px;
  overflow: hidden;
  border-radius: 4px;
  flex-shrink: 0;
}

.item-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-info {
  flex: 1;
}

.item-info h5 {
  margin: 0 0 5px 0;
  color: #333;
  font-size: 14px;
}

.item-price {
  margin: 0 0 5px 0;
  color: #e74c3c;
  font-size: 14px;
  font-weight: 500;
}

.item-quantity {
  margin: 0;
  color: #666;
  font-size: 14px;
}

.item-subtotal {
  font-weight: 600;
  color: #333;
  flex-shrink: 0;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  padding-top: 20px;
  border-top: 1px solid #eee;
  margin-top: 20px;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.btn-primary {
  background: #3498db;
  color: white;
}

.btn-primary:hover {
  background: #2980b9;
}

.btn-secondary {
  background: #95a5a6;
  color: white;
}

.btn-secondary:hover {
  background: #7f8c8d;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .order-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }
  
  .order-actions {
    width: 100%;
    flex-direction: column;
    align-items: flex-start;
  }
  
  .orders-table {
    overflow-x: auto;
  }
  
  .order-item {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .item-image {
    width: 100px;
    height: 100px;
  }
}
</style>