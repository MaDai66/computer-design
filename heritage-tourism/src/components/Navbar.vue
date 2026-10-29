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
    window.location.reload()
  } catch (error) {
    // 忽略错误
  }
}

watch(() => route.path, () => {
  checkLoginStatus()
})

onMounted(() => {
  checkLoginStatus()
  window.addEventListener('storage', checkLoginStatus)
})

onUnmounted(() => {
  window.removeEventListener('storage', checkLoginStatus)
})
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: transparent;
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
  font-family: var(--font-serif);
  color: var(--white);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.navbar-nav {
  display: flex;
  gap: 32px;
}

.nav-item {
  text-decoration: none;
  font-weight: 500;
  color: var(--white);
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  transition: color 0.3s ease;
  position: relative;
}

.nav-item:hover {
  color: rgba(255, 255, 255, 0.8);
}

.nav-item.router-link-active {
  color: var(--white);
}

.nav-item.router-link-active::after {
  content: '';
  position: absolute;
  bottom: -20px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--white);
  border-radius: 1px;
}

.logout-btn {
  background: none;
  border: none;
  text-decoration: none;
  font-weight: 500;
  color: var(--white);
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  cursor: pointer;
  padding: 0;
  font-size: 16px;
  transition: color 0.3s ease;
}

.logout-btn:hover {
  color: rgba(255, 255, 255, 0.8);
}

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