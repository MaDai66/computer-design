<template>
  <div class="dashboard">
    <div class="dashboard-header">
      <h2>系统概览</h2>
      <p>欢迎回来，{{ adminUser.username }}</p>
    </div>

    <!-- 数据卡片 -->
    <div class="stats-cards">
      <div class="stat-card">
        <div class="stat-icon users">👥</div>
        <div class="stat-content">
          <h3>{{ stats.users }}</h3>
          <p>总用户数</p>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon orders">📦</div>
        <div class="stat-content">
          <h3>{{ stats.orders }}</h3>
          <p>总订单数</p>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon products">🎁</div>
        <div class="stat-content">
          <h3>{{ stats.products }}</h3>
          <p>产品数量</p>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon revenue">💰</div>
        <div class="stat-content">
          <h3>¥{{ stats.revenue }}</h3>
          <p>总销售额</p>
        </div>
      </div>
    </div>

    <!-- 最近订单 -->
    <div class="recent-orders">
      <div class="section-header">
        <h3>最近订单</h3>
        <router-link to="/admin/orders" class="view-all">查看全部</router-link>
      </div>
      <div class="orders-table">
        <table>
          <thead>
            <tr>
              <th>订单号</th>
              <th>用户</th>
              <th>金额</th>
              <th>状态</th>
              <th>时间</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in recentOrders" :key="order.id">
              <td>{{ order.id }}</td>
              <td>{{ order.user }}</td>
              <td>¥{{ order.amount }}</td>
              <td>
                <span :class="['status', order.status]">
                  {{ order.statusText }}
                </span>
              </td>
              <td>{{ order.time }}</td>
              <td>
                <button class="action-btn view">查看</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 系统状态 -->
    <div class="system-status">
      <div class="section-header">
        <h3>系统状态</h3>
      </div>
      <div class="status-grid">
        <div class="status-item">
          <span class="status-label">服务器状态</span>
          <span class="status-value online">正常</span>
        </div>
        <div class="status-item">
          <span class="status-label">数据库状态</span>
          <span class="status-value online">正常</span>
        </div>
        <div class="status-item">
          <span class="status-label">API状态</span>
          <span class="status-value online">正常</span>
        </div>
        <div class="status-item">
          <span class="status-label">存储空间</span>
          <span class="status-value">75%</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { adminAPI } from '../api/adminAPI'

const adminUser = ref({ username: '管理员' })
const stats = ref({
  users: 0,
  orders: 0,
  products: 0,
  revenue: 0
})
const recentOrders = ref([])
const isLoading = ref(true)

const loadDashboardData = async () => {
  isLoading.value = true
  try {
    // 获取概览数据
    const overviewData = await adminAPI.analytics.getOverview({})
    stats.value = {
      users: overviewData.users || 0,
      orders: overviewData.orders || 0,
      products: overviewData.products || 0,
      revenue: overviewData.revenue || 0
    }
    
    // 获取最近订单
    const ordersData = await adminAPI.orders.getList({ limit: 4 })
    recentOrders.value = ordersData.results || []
  } catch (error) {
    console.error('加载数据失败:', error)
    // 保留默认数据作为兜底
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  // 从localStorage获取管理员信息
  const user = localStorage.getItem('adminUser')
  if (user) {
    adminUser.value = JSON.parse(user)
  }
  
  // 加载数据
  loadDashboardData()
})
</script>

<style scoped>
.dashboard {
  width: 100%;
}

.dashboard-header {
  margin-bottom: 30px;
}

.dashboard-header h2 {
  margin: 0 0 5px 0;
  color: #333;
  font-size: 24px;
}

.dashboard-header p {
  margin: 0;
  color: #666;
  font-size: 14px;
}

/* 数据卡片 */
.stats-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  transition: transform 0.3s, box-shadow 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.stat-icon {
  font-size: 32px;
  margin-right: 15px;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
}

.stat-icon.users {
  background: #e3f2fd;
  color: #2196f3;
}

.stat-icon.orders {
  background: #e8f5e8;
  color: #4caf50;
}

.stat-icon.products {
  background: #fff3e0;
  color: #ff9800;
}

.stat-icon.revenue {
  background: #f3e5f5;
  color: #9c27b0;
}

.stat-content h3 {
  margin: 0 0 5px 0;
  font-size: 24px;
  color: #333;
}

.stat-content p {
  margin: 0;
  color: #666;
  font-size: 14px;
}

/* 最近订单 */
.recent-orders {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.section-header h3 {
  margin: 0;
  color: #333;
  font-size: 18px;
}

.view-all {
  color: #3498db;
  text-decoration: none;
  font-size: 14px;
}

.view-all:hover {
  text-decoration: underline;
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

.status.completed {
  background: #e8f5e8;
  color: #4caf50;
}

.status.pending {
  background: #fff3e0;
  color: #ff9800;
}

.status.shipped {
  background: #e3f2fd;
  color: #2196f3;
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

/* 系统状态 */
.system-status {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.status-item:last-child {
  border-bottom: none;
}

.status-label {
  color: #666;
  font-size: 14px;
}

.status-value {
  font-weight: 500;
  font-size: 14px;
}

.status-value.online {
  color: #4caf50;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .stats-cards {
    grid-template-columns: 1fr;
  }
  
  .orders-table {
    overflow-x: auto;
  }
  
  .status-grid {
    grid-template-columns: 1fr;
  }
}
</style>