<template>
  <div class="user-management">
    <div class="user-header">
      <h2>用户管理</h2>
      <div class="user-actions">
        <div class="search-box">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索用户..."
            @keyup.enter="handleSearch"
          />
          <button class="search-btn" @click="handleSearch">搜索</button>
        </div>
        <button class="btn btn-primary">
          导出用户数据
        </button>
      </div>
    </div>

    <!-- 加载状态 -->
    <div v-if="isLoading" class="loading-state">
      <p>加载中...</p>
    </div>

    <!-- 用户列表 -->
    <div v-else class="users-table">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>头像</th>
            <th>用户名</th>
            <th>邮箱</th>
            <th>注册时间</th>
            <th>最后登录</th>
            <th>状态</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.id }}</td>
            <td>
              <div class="user-avatar">
                <img :src="user.avatar" :alt="user.username" />
              </div>
            </td>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.registerTime }}</td>
            <td>{{ user.lastLogin }}</td>
            <td>
              <span :class="['status', user.status]">
                {{ user.statusText }}
              </span>
            </td>
            <td>
              <div class="user-actions">
                <button class="action-btn view" @click="viewUser(user)">
                  查看
                </button>
                <button class="action-btn edit" @click="editUser(user)">
                  编辑
                </button>
                <button 
                  class="action-btn" 
                  :class="user.status === 'active' ? 'block' : 'unblock'"
                  @click="toggleUserStatus(user)"
                >
                  {{ user.status === 'active' ? '禁用' : '启用' }}
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 分页 -->
    <div v-if="!isLoading" class="pagination">
      <button class="page-btn" :disabled="currentPage === 1" @click="handlePageChange(currentPage - 1)">上一页</button>
      <span class="page-info">
        第 {{ currentPage }} 页，共 {{ totalPages }} 页
      </span>
      <button class="page-btn" :disabled="currentPage === totalPages" @click="handlePageChange(currentPage + 1)">下一页</button>
    </div>

    <!-- 用户详情模态框 -->
    <div v-if="showUserModal" class="modal-overlay" @click="showUserModal = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>{{ currentUser ? (isEditing ? '编辑用户' : '用户详情') : '用户信息' }}</h3>
          <button class="close-btn" @click="showUserModal = false">&times;</button>
        </div>
        <div class="modal-body" v-if="currentUser">
          <div class="user-detail">
            <div class="detail-avatar">
              <img :src="currentUser.avatar" :alt="currentUser.username" />
            </div>
            <div class="detail-info">
              <div class="detail-row">
                <span class="detail-label">用户名：</span>
                <input 
                  v-if="isEditing" 
                  type="text" 
                  v-model="currentUser.username"
                  class="detail-input"
                />
                <span v-else>{{ currentUser.username }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">邮箱：</span>
                <input 
                  v-if="isEditing" 
                  type="email" 
                  v-model="currentUser.email"
                  class="detail-input"
                />
                <span v-else>{{ currentUser.email }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">注册时间：</span>
                <span>{{ currentUser.registerTime }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">最后登录：</span>
                <span>{{ currentUser.lastLogin }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">状态：</span>
                <select 
                  v-if="isEditing" 
                  v-model="currentUser.status"
                  class="detail-select"
                >
                  <option value="active">活跃</option>
                  <option value="inactive">禁用</option>
                </select>
                <span v-else>{{ currentUser.statusText }}</span>
              </div>
              <div class="detail-row">
                <span class="detail-label">角色：</span>
                <select 
                  v-if="isEditing" 
                  v-model="currentUser.role"
                  class="detail-select"
                >
                  <option value="user">普通用户</option>
                  <option value="vip">VIP用户</option>
                  <option value="admin">管理员</option>
                </select>
                <span v-else>{{ currentUser.roleText }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" @click="showUserModal = false">取消</button>
          <button 
            v-if="isEditing" 
            class="btn btn-primary" 
            @click="saveUser"
          >
            保存
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { adminAPI } from '../api/adminAPI'

const searchQuery = ref('')
const currentPage = ref(1)
const totalPages = ref(1)
const showUserModal = ref(false)
const currentUser = ref(null)
const isEditing = ref(false)
const isLoading = ref(false)

// 用户数据
const users = ref([])

// 加载用户数据
const loadUsers = async () => {
  isLoading.value = true
  try {
    const response = await adminAPI.users.getList({
      search: searchQuery.value,
      page: currentPage.value
    })
    users.value = response.results || []
    totalPages.value = response.total_pages || 1
  } catch (error) {
    console.error('加载用户失败:', error)
  } finally {
    isLoading.value = false
  }
}

// 查看用户详情
const viewUser = (user) => {
  currentUser.value = { ...user }
  isEditing.value = false
  showUserModal.value = true
}

// 编辑用户
const editUser = (user) => {
  currentUser.value = { ...user }
  isEditing.value = true
  showUserModal.value = true
}

// 切换用户状态
const toggleUserStatus = async (user) => {
  try {
    await adminAPI.users.toggleStatus(user.id)
    // 重新加载数据
    loadUsers()
  } catch (error) {
    console.error('切换用户状态失败:', error)
  }
}

// 保存用户
const saveUser = async () => {
  if (currentUser.value) {
    try {
      await adminAPI.users.update(currentUser.value.id, currentUser.value)
      showUserModal.value = false
      // 重新加载数据
      loadUsers()
    } catch (error) {
      console.error('保存用户失败:', error)
    }
  }
}

// 搜索
const handleSearch = () => {
  currentPage.value = 1
  loadUsers()
}

// 分页
const handlePageChange = (page) => {
  currentPage.value = page
  loadUsers()
}

onMounted(() => {
  // 初始加载用户数据
  loadUsers()
})
</script>

<style scoped>
.user-management {
  width: 100%;
}

.user-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.user-header h2 {
  margin: 0;
  color: #333;
  font-size: 24px;
}

.user-actions {
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

/* 加载状态 */
.loading-state {
  text-align: center;
  padding: 48px 24px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.loading-state p {
  font-size: 16px;
  color: #666;
}

/* 用户列表 */
.users-table {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 30px;
}

.users-table table {
  width: 100%;
  border-collapse: collapse;
}

.users-table th,
.users-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.users-table th {
  background: #f5f7fa;
  font-weight: 600;
  color: #333;
}

.users-table tr:hover {
  background: #f9f9f9;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
}

.user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.status {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.status.active {
  background: #e8f5e8;
  color: #4caf50;
}

.status.inactive {
  background: #ffebee;
  color: #e53935;
}

.user-actions {
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

.action-btn.block {
  background: #e74c3c;
  color: white;
}

.action-btn.block:hover {
  background: #c0392b;
}

.action-btn.unblock {
  background: #27ae60;
  color: white;
}

.action-btn.unblock:hover {
  background: #229954;
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
  max-width: 600px;
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

.user-detail {
  display: flex;
  gap: 30px;
}

.detail-avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
}

.detail-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.detail-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.detail-row {
  display: flex;
  align-items: center;
  gap: 15px;
}

.detail-label {
  width: 100px;
  color: #666;
  font-weight: 500;
  flex-shrink: 0;
}

.detail-input,
.detail-select {
  flex: 1;
  padding: 6px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  padding-top: 20px;
  border-top: 1px solid #eee;
  margin-top: 20px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .user-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }
  
  .user-actions {
    width: 100%;
    flex-direction: column;
    align-items: flex-start;
  }
  
  .users-table {
    overflow-x: auto;
  }
  
  .user-detail {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .detail-row {
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
  }
  
  .detail-label {
    width: auto;
  }
}
</style>