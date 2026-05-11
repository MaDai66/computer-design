<template>
  <div class="login">
    <div class="login-container">
      <div class="login-header">
        <h1>欢迎登录</h1>
        <p>吉韵遗风 - 非遗文化旅游平台</p>
      </div>
      <div class="login-form">
        <form @submit.prevent="login">
          <div class="form-group">
            <label for="username">用户名</label>
            <input type="text" id="username" v-model="form.username" placeholder="请输入用户名" required />
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" id="password" v-model="form.password" placeholder="请输入密码" required />
          </div>
          <div class="form-actions">
            <button type="submit" class="btn btn-primary" :disabled="loading">
              {{ loading ? '登录中...' : '登录' }}
            </button>
          </div>
          <div class="form-footer">
            <p>还没有账号？ <router-link to="/register">立即注册</router-link></p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { userAPI } from '../api/users'

const router = useRouter()
const form = ref({
  username: '',
  password: ''
})
const loading = ref(false)

const login = async () => {
  try {
    loading.value = true
    // 调用登录API
    const response = await userAPI.login(form.value)
    console.log('登录成功，响应数据:', response)
    // 构建用户对象
    const userData = {
      username: response.username,
      role: response.role,
      token: response.token
    }
    // 保存user到localStorage
    localStorage.setItem('user', JSON.stringify(userData))
    console.log('已保存用户数据到localStorage:', userData)
    // 保存token到localStorage
    localStorage.setItem('token', response.token)
    console.log('已保存token到localStorage')
    // 跳转到个人中心
    router.push('/profile')
  } catch (error) {
    console.error('登录失败:', error)
    alert('登录失败，请检查用户名和密码')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--bg-color);
  padding: 20px;
}

.login-container {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-hover);
  width: 100%;
  max-width: 400px;
  padding: 40px;
}

.login-header {
  text-align: center;
  margin-bottom: 32px;
}

.login-header h1 {
  font-size: 28px;
  font-weight: 700;
  color: var(--text-dark);
  margin-bottom: 8px;
}

.login-header p {
  font-size: 14px;
  color: var(--text-medium);
}

.login-form {
  width: 100%;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--text-dark);
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  font-size: 14px;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: var(--primary-color);
}

.form-actions {
  margin-bottom: 24px;
}

.btn-primary {
  width: 100%;
  padding: 12px;
  background-color: var(--primary-color);
  color: var(--white);
  border: none;
  border-radius: var(--radius-md);
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: var(--primary-dark);
}

.btn-primary:disabled {
  background-color: var(--text-light);
  cursor: not-allowed;
}

.form-footer {
  text-align: center;
  font-size: 14px;
  color: var(--text-medium);
}

.form-footer a {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.form-footer a:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

@media (max-width: 768px) {
  .login-container {
    padding: 32px 24px;
  }
  
  .login-header h1 {
    font-size: 24px;
  }
}
</style>
