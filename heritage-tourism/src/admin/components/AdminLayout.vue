<template>
  <div class="admin-layout">
    <!-- 侧边导航 -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <h2>后台管理</h2>
      </div>
      <nav class="sidebar-nav">
        <ul>
          <li>
            <router-link to="/admin" class="nav-item">
              <span class="nav-icon">🏠</span>
              <span class="nav-text">首页</span>
            </router-link>
          </li>
          <li>
            <router-link to="/admin/content" class="nav-item">
              <span class="nav-icon">📄</span>
              <span class="nav-text">内容管理</span>
            </router-link>
          </li>
          <li>
            <router-link to="/admin/users" class="nav-item">
              <span class="nav-icon">👥</span>
              <span class="nav-text">用户管理</span>
            </router-link>
          </li>
          <li>
            <router-link to="/admin/orders" class="nav-item">
              <span class="nav-icon">📦</span>
              <span class="nav-text">订单管理</span>
            </router-link>
          </li>
          <li>
            <router-link to="/admin/analytics" class="nav-item">
              <span class="nav-icon">📊</span>
              <span class="nav-text">数据分析</span>
            </router-link>
          </li>
          <li>
            <router-link to="/admin/settings" class="nav-item">
              <span class="nav-icon">⚙️</span>
              <span class="nav-text">系统设置</span>
            </router-link>
          </li>
        </ul>
      </nav>
    </aside>

    <!-- 主内容区 -->
    <main class="main-content">
      <!-- 顶部栏 -->
      <header class="top-bar">
        <div class="top-bar-left">
          <button class="toggle-sidebar" @click="toggleSidebar">
            ☰
          </button>
          <h3>{{ currentPage }}</h3>
        </div>
        <div class="top-bar-right">
          <div class="user-info">
            <span class="username">{{ adminUser.username }}</span>
            <button class="logout-btn" @click="handleLogout">
              退出
            </button>
          </div>
        </div>
      </header>

      <!-- 内容区域 -->
      <div class="content-area">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const sidebarCollapsed = ref(false)
const adminUser = ref({ username: '管理员' })

const currentPage = computed(() => {
  const pageMap = {
    '/admin': '首页',
    '/admin/content': '内容管理',
    '/admin/users': '用户管理',
    '/admin/orders': '订单管理',
    '/admin/analytics': '数据分析',
    '/admin/settings': '系统设置'
  }
  return pageMap[route.path] || '后台管理'
})

const toggleSidebar = () => {
  sidebarCollapsed.value = !sidebarCollapsed.value
}

const handleLogout = () => {
  // 清除登录状态
  localStorage.removeItem('adminToken')
  localStorage.removeItem('adminUser')
  // 跳转到登录页面
  router.push('/admin/login')
}

onMounted(() => {
  // 检查登录状态
  const user = localStorage.getItem('adminUser')
  if (user) {
    adminUser.value = JSON.parse(user)
  } else {
    // 未登录，跳转到登录页
    router.push('/admin/login')
  }
})
</script>

<style scoped>
.admin-layout {
  display: flex;
  min-height: 100vh;
  background: #f5f7fa;
}

/* 侧边导航 */
.sidebar {
  width: 240px;
  background: #2c3e50;
  color: white;
  transition: width 0.3s;
}

.sidebar.collapsed {
  width: 80px;
}

.sidebar-header {
  padding: 20px;
  border-bottom: 1px solid #34495e;
}

.sidebar-header h2 {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
}

.sidebar-nav {
  padding: 20px 0;
}

.sidebar-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 12px 20px;
  color: #ecf0f1;
  text-decoration: none;
  transition: all 0.3s;
  border-left: 3px solid transparent;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
  border-left-color: #3498db;
}

.nav-item.router-link-active {
  background: rgba(255, 255, 255, 0.15);
  border-left-color: #3498db;
  font-weight: 500;
}

.nav-icon {
  margin-right: 12px;
  font-size: 18px;
}

/* 主内容区 */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* 顶部栏 */
.top-bar {
  background: white;
  border-bottom: 1px solid #e0e6ed;
  padding: 0 20px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.top-bar-left {
  display: flex;
  align-items: center;
}

.toggle-sidebar {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  margin-right: 20px;
  color: #333;
}

.top-bar-left h3 {
  margin: 0;
  font-size: 18px;
  color: #333;
}

.top-bar-right {
  display: flex;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
}

.username {
  margin-right: 20px;
  font-weight: 500;
  color: #333;
}

.logout-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.logout-btn:hover {
  background: #c0392b;
}

/* 内容区域 */
.content-area {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    z-index: 1000;
    transform: translateX(-100%);
  }

  .sidebar.open {
    transform: translateX(0);
  }

  .content-area {
    padding: 15px;
  }
}
</style>