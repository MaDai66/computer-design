<template>
  <el-container class="admin-layout">
    <!-- 侧边导航 -->
    <el-aside width="200px" class="sidebar">
      <div class="sidebar-logo">
        <h2>吉韵遗风</h2>
        <span class="logo-subtitle">后台管理系统</span>
      </div>
      <el-menu
        :default-active="activeMenu"
        class="sidebar-menu"
        mode="vertical"
        background-color="#2c3e50"
        text-color="#ecf0f1"
        active-text-color="#409eff"
        @select="handleMenuSelect"
      >
        <el-menu-item index="/admin">
          <el-icon name="House"></el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-menu-item index="/admin/content">
          <el-icon name="Folder"></el-icon>
          <span>内容管理</span>
        </el-menu-item>
        <el-menu-item index="/admin/users">
          <el-icon name="User"></el-icon>
          <span>用户管理</span>
        </el-menu-item>
        <el-menu-item index="/admin/orders">
          <el-icon name="ShoppingCart"></el-icon>
          <span>订单管理</span>
        </el-menu-item>
        <el-menu-item index="/admin/analytics">
          <el-icon name="BarChart3"></el-icon>
          <span>数据分析</span>
        </el-menu-item>
        <el-menu-item index="/admin/settings">
          <el-icon name="Settings"></el-icon>
          <span>系统设置</span>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <!-- 主内容区 -->
    <el-container class="main-container">
      <!-- 顶部栏 -->
      <el-header class="top-header">
        <div class="header-left">
          <el-button
            icon="Menu"
            class="toggle-btn"
            @click="toggleSidebar"
            circle
          ></el-button>
          <span class="page-title">{{ currentPage }}</span>
        </div>
        <div class="header-right">
          <el-dropdown>
            <span class="user-info">
              <el-icon name="User"></el-icon>
              <span>{{ adminUser.username }}</span>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>个人信息</el-dropdown-item>
                <el-dropdown-item @click="handleLogout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <!-- 内容区域 -->
      <el-main class="content-area">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const adminUser = ref({ username: '管理员' })

const activeMenu = computed(() => route.path)

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
}

const handleMenuSelect = (index) => {
  router.push(index)
}

const handleLogout = () => {
  localStorage.removeItem('adminToken')
  localStorage.removeItem('adminUser')
  router.push('/admin/login')
}

onMounted(() => {
  console.log('AdminLayout mounted')
  console.log('当前路径:', window.location.pathname)
  
  const token = localStorage.getItem('adminToken')
  const user = localStorage.getItem('adminUser')
  
  console.log('Token存在:', !!token)
  console.log('User信息存在:', !!user)
  
  if (token) {
    if (user) {
      try {
        adminUser.value = JSON.parse(user)
        console.log('已解析用户信息:', adminUser.value)
      } catch (e) {
        console.error('解析用户信息失败:', e)
        adminUser.value = { username: '管理员' }
      }
    } else {
      adminUser.value = { username: '管理员' }
      console.log('无用户信息，使用默认值')
    }
  } else {
    console.log('未找到token，跳转到登录页')
    router.push('/admin/login')
  }
})
</script>

<style scoped>
.admin-layout {
  height: 100vh;
}

.sidebar {
  background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.15);
}

.sidebar-logo {
  padding: 24px;
  text-align: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-logo h2 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  color: #fff;
}

.sidebar-logo .logo-subtitle {
  display: block;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.7);
  margin-top: 4px;
}

.sidebar-menu {
  border-right: none;
  height: calc(100% - 80px);
}

.main-container {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.top-header {
  background: #fff;
  border-bottom: 1px solid #e8e8e8;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
}

.header-left {
  display: flex;
  align-items: center;
}

.toggle-btn {
  margin-right: 16px;
}

.page-title {
  font-size: 16px;
  font-weight: 600;
  color: #303133;
}

.header-right {
  display: flex;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  padding: 8px 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.user-info:hover {
  background-color: #f5f7fa;
}

.user-info span {
  margin-left: 8px;
  color: #606266;
}

.content-area {
  padding: 20px;
  background-color: #f5f7fa;
  overflow-y: auto;
}
</style>