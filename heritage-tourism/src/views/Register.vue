<template>
  <div class="register">
    <div class="register-container">
      <div class="register-header">
        <h1>用户注册</h1>
        <p>加入吉韵遗风，体验非遗文化之旅</p>
      </div>
      <div class="register-form">
        <form @submit.prevent="register">
          <div class="form-group">
            <label for="username">用户名</label>
            <input type="text" id="username" v-model="form.username" placeholder="请输入用户名" required />
          </div>
          <div class="form-group">
            <label for="email">邮箱</label>
            <input type="email" id="email" v-model="form.email" placeholder="请输入邮箱" required />
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input type="password" id="password" v-model="form.password" placeholder="请输入密码" required />
          </div>
          <div class="form-group">
            <label for="confirmPassword">确认密码</label>
            <input type="password" id="confirmPassword" v-model="form.confirmPassword" placeholder="请确认密码" required />
          </div>
          <div class="form-actions">
            <button type="submit" class="btn btn-primary" :disabled="loading">
              {{ loading ? '注册中...' : '注册' }}
            </button>
          </div>
          <div class="form-footer">
            <p>已有账号？ <router-link to="/login">立即登录</router-link></p>
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
  email: '',
  password: '',
  confirmPassword: ''
})
const loading = ref(false)

const register = async () => {
  if (form.value.password !== form.value.confirmPassword) {
    alert('两次输入的密码不一致')
    return
  }
  
  try {
    loading.value = true
    // 调用注册API
    const response = await userAPI.register({
      username: form.value.username,
      email: form.value.email,
      password: form.value.password
    })
    console.log('注册成功:', response)
    // 跳转到登录页面
    router.push('/login')
  } catch (error) {
    console.error('注册失败:', error)
    alert('注册失败，请稍后重试')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--bg-color);
  padding: 20px;
}

.register-container {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-hover);
  width: 100%;
  max-width: 400px;
  padding: 40px;
}

.register-header {
  text-align: center;
  margin-bottom: 32px;
}

.register-header h1 {
  font-size: 28px;
  font-weight: 700;
  color: var(--text-dark);
  margin-bottom: 8px;
}

.register-header p {
  font-size: 14px;
  color: var(--text-medium);
}

.register-form {
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
  .register-container {
    padding: 32px 24px;
  }
  
  .register-header h1 {
    font-size: 24px;
  }
}
</style>
