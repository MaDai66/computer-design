<template>
  <header class="navbar">
    <div class="container">
      <div class="navbar-content">
        <!-- Logo -->
        <router-link to="/" class="navbar-logo">
          <div class="logo">
            <span class="logo-text">吉韵遗风</span>
          </div>
        </router-link>
        
        <!-- Desktop Navigation -->
        <nav class="navbar-nav">
          <router-link to="/" class="nav-item">首页</router-link>
          <router-link to="/smart-tour" class="nav-item">智游</router-link>
          <router-link to="/heritage" class="nav-item">遗珍</router-link>
          <router-link to="/homestay" class="nav-item">乡宿</router-link>
          <router-link to="/gifts" class="nav-item">吉礼</router-link>
          <template v-if="isLoggedIn">
            <router-link to="/profile" class="nav-item">我的</router-link>
            <button class="nav-item logout-btn" @click="logout">退出登录</button>
          </template>
          <template v-else>
            <router-link to="/login" class="nav-item">登录</router-link>
            <router-link to="/register" class="nav-item">注册</router-link>
          </template>
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const isLoggedIn = ref(false)

const checkLoginStatus = () => {
  try {
    const user = localStorage.getItem('user')
    isLoggedIn.value = !!user
  } catch (error) {
    isLoggedIn.value = false
  }
}

const logout = () => {
  try {
    localStorage.removeItem('user')
    checkLoginStatus()
    // 刷新页面以更新导航栏
    window.location.reload()
  } catch (error) {
    // 忽略错误
  }
}

// 监听路由变化，每次路由变化时检查登录状态
watch(() => route.path, () => {
  checkLoginStatus()
})

onMounted(() => {
  checkLoginStatus()
  // 监听storage变化，以便在其他页面登录/注销后更新状态
  window.addEventListener('storage', checkLoginStatus)
})

onUnmounted(() => {
  window.removeEventListener('storage', checkLoginStatus)
})
</script>

<style scoped>
.logout-btn {
  background: none;
  border: none;
  color: var(--text-dark);
  text-decoration: none;
  font-weight: 500;
  transition: var(--transition);
  position: relative;
  cursor: pointer;
  padding: 0;
  font-size: 16px;
}

.logout-btn:hover {
  color: var(--primary-color);
}
</style>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  background-color: rgba(253, 248, 240, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border-color);
  z-index: 1000;
  padding: 16px 0;
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-logo {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.logo-text {
  font-size: 24px;
  font-weight: 700;
  color: var(--primary-color);
  font-family: var(--font-serif);
}

.navbar-nav {
  display: flex;
  gap: 32px;
}

.nav-item {
  color: var(--text-dark);
  text-decoration: none;
  font-weight: 500;
  transition: var(--transition);
  position: relative;
}

.nav-item:hover {
  color: var(--primary-color);
}

.nav-item.router-link-active {
  color: var(--primary-color);
}

.nav-item.router-link-active::after {
  content: '';
  position: absolute;
  bottom: -20px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--primary-color);
  border-radius: 1px;
}

/* Responsive */
@media (max-width: 768px) {
  .navbar {
    padding: 12px 0;
  }
  
  .logo-text {
    font-size: 20px;
  }
  
  .navbar-nav {
    gap: 16px;
  }
  
  .nav-item {
    font-size: 14px;
  }
}
</style>