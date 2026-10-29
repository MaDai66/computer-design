<template>
  <div class="admin-login">
    <div class="login-container">
      <div class="login-header">
        <h1>吉林非遗旅游后台管理</h1>
        <p>管理员登录</p>
      </div>
      <div class="login-form">
        <div class="form-group">
          <label for="username">用户名</label>
          <input 
            type="text" 
            id="username" 
            v-model="loginForm.username" 
            placeholder="请输入管理员用户名"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">密码</label>
          <input 
            type="password" 
            id="password" 
            v-model="loginForm.password" 
            placeholder="请输入密码"
            required
          />
        </div>
        <div class="form-actions">
          <button 
            class="login-btn" 
            @click="handleLogin" 
            :disabled="isLoading"
          >
            {{ isLoading ? '登录中...' : '登录' }}
          </button>
        </div>
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
      </div>
      <div class="login-footer">
        <p>© 2026 吉林非遗旅游管理系统</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { adminAPI } from '../api/adminAPI'

const router = useRouter()
const loginForm = ref({
  username: 'admin',
  password: 'admin123'
})
const isLoading = ref(false)
const errorMessage = ref('')

const handleLogin = async () => {
  if (!loginForm.value.username || !loginForm.value.password) {
    errorMessage.value = '请填写用户名和密码'
    return
  }

  isLoading.value = true
  errorMessage.value = ''

  try {
    console.log('开始登录流程...')
    console.log('用户名:', loginForm.value.username)
    
    // 调用真实的登录API
    const response = await adminAPI.auth.login({
      username: loginForm.value.username,
      password: loginForm.value.password
    })
    
    console.log('登录响应成功:', response)
    console.log('Token:', response.token ? '已获取' : '未获取')
    
    // 保存登录状态
    if (response.token) {
      localStorage.setItem('adminToken', response.token)
      localStorage.setItem('adminUser', JSON.stringify({
        username: response.username || loginForm.value.username,
        role: response.role || 'admin'
      }))
      
      console.log('已保存token和用户信息到localStorage')
      console.log('准备跳转到 /admin')
      
      // 使用 router.push 进行跳转
      await router.push('/admin')
      
      console.log('跳转完成')
    } else {
      console.error('未获取到token:', response)
      errorMessage.value = '登录失败：未获取到有效token'
    }
  } catch (error) {
    console.error('登录过程中发生错误:', error)
    console.error('错误响应:', error.response)
    console.error('错误状态:', error.response?.status)
    console.error('错误数据:', error.response?.data)
    
    // 处理错误
    if (error.response) {
      if (error.response.status === 401) {
        errorMessage.value = '用户名或密码错误'
      } else if (error.response.data) {
        errorMessage.value = error.response.data.detail || error.response.data.message || '登录失败'
      } else {
        errorMessage.value = `登录失败 (错误码: ${error.response.status})`
      }
    } else if (error.request) {
      errorMessage.value = '无法连接到服务器，请确保后端服务已启动'
    } else {
      errorMessage.value = '登录失败，请检查网络连接'
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.admin-login {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.login-container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  padding: 40px;
  width: 100%;
  max-width: 400px;
}

.login-header {
  text-align: center;
  margin-bottom: 30px;
}

.login-header h1 {
  color: #333;
  font-size: 24px;
  margin-bottom: 8px;
}

.login-header p {
  color: #666;
  font-size: 16px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #333;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
}

.form-actions {
  margin-top: 30px;
}

.login-btn {
  width: 100%;
  padding: 14px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-btn:hover {
  background: #5a6fd8;
}

.login-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.error-message {
  margin-top: 15px;
  padding: 10px;
  background: #fee;
  color: #d32f2f;
  border-radius: 4px;
  font-size: 14px;
}

.login-footer {
  margin-top: 30px;
  text-align: center;
  color: #999;
  font-size: 14px;
}

@media (max-width: 480px) {
  .login-container {
    padding: 30px;
  }
}
</style>