<template>
  <div class="login">
    <div class="login-bg"></div>
    
    <div class="login-container">
      <div class="login-left">
        <div class="decorative-image">
          <img src="/profile/04.jpg" alt="非遗文化" />
          <div class="image-overlay">
            <div class="image-title">非遗传承</div>
            <div class="image-subtitle">探索中华五千年文化遗产 · 传承匠心技艺</div>
          </div>
        </div>
        
        <div class="decorative-elements">
          <div class="fan fan-left"></div>
          <div class="fan fan-right"></div>
          <div class="petals">
            <span v-for="i in 8" :key="i" class="petal" :class="`petal-${i}`"></span>
          </div>
        </div>
      </div>
      
      <div class="login-right">
        <div class="login-card">
          <div class="card-decoration-top"></div>
          
          <div class="login-header">
            <div class="logo-section">
              <div class="logo">
                <img src="/aji.png" alt="阿吉" />
              </div>
            </div>
            <h1>非遗传承</h1>
            <p class="subtitle">传承千年文化，守护匠心技艺</p>
          </div>
          
          <div class="welcome-text">
            <h2>欢迎回来</h2>
          </div>
          
          <div class="login-form">
            <form @submit.prevent="login">
              <div class="form-group">
                <div class="input-wrapper">
                  <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="#C28B4E" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" stroke-linecap="round" stroke-linejoin="round"/>
                    <circle cx="12" cy="7" r="4" />
                  </svg>
                  <input 
                    type="text" 
                    id="username" 
                    v-model="form.username" 
                    placeholder="请输入用户名" 
                    required 
                  />
                </div>
              </div>
              
              <div class="form-group">
                <div class="input-wrapper">
                  <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="#C28B4E" stroke-width="2">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2" stroke-linecap="round"/>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4" stroke-linecap="round"/>
                  </svg>
                  <input 
                    type="password" 
                    id="password" 
                    v-model="form.password" 
                    placeholder="请输入密码" 
                    required 
                  />
                </div>
              </div>
              
              <div class="form-actions">
                <button type="submit" class="btn btn-primary" :disabled="loading">
                  <span v-if="loading" class="loading-spinner"></span>
                  {{ loading ? '登录中...' : '登录' }}
                </button>
              </div>
              
              <div class="form-footer">
                <div class="forgot-password">
                  <a href="#" @click.prevent="showForgotPassword">忘记密码？</a>
                </div>
                <p>还没有账号？ <router-link to="/register">立即注册</router-link></p>
              </div>
            </form>
          </div>
          
          <div class="card-decoration-bottom"></div>
        </div>
        
        <div class="copyright">
          © 2024 吉韵遗风 - 非遗文化旅游平台
        </div>
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
    const loginResponse = await userAPI.login(form.value)
    console.log('登录成功，响应数据:', loginResponse)
    
    localStorage.setItem('token', loginResponse.access)
    
    const fullUserData = {
      id: loginResponse.user.id || '',
      username: loginResponse.user.username || '',
      email: loginResponse.user.email || '',
      phone: loginResponse.user.phone || '',
      nickname: loginResponse.user.nickname || '',
      avatar: loginResponse.user.avatar || ''
    }
    
    localStorage.setItem('user', JSON.stringify(fullUserData))
    console.log('已保存完整用户数据到localStorage:', fullUserData)
    
    router.push('/')
  } catch (error) {
    console.error('登录失败:', error)
    alert('登录失败，请检查用户名和密码')
  } finally {
    loading.value = false
  }
}

const showForgotPassword = () => {
  alert('忘记密码功能开发中')
}
</script>
feiy
<style scoped>
.login {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  padding: 20px;
}

.login-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('/profile/bg.jpg') center/cover no-repeat;
  opacity: 0.15;
  z-index: 0;
}

.login-container {
  display: flex;
  width: 100%;
  max-width: 1000px;
  height: 560px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(156, 47, 47, 0.15);
  overflow: hidden;
  position: relative;
  z-index: 1;
}

.login-left {
  width: 45%;
  position: relative;
  overflow: hidden;
  background: linear-gradient(135deg, rgba(156, 47, 47, 0.05) 0%, rgba(194, 139, 78, 0.05) 100%);
}

.decorative-image {
  width: 100%;
  height: 100%;
  position: relative;
}

.decorative-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 30px;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.6));
  text-align: center;
}

.image-title {
  font-size: 28px;
  font-weight: 700;
  color: #FAF6EB;
  margin-bottom: 8px;
  font-family: 'STKaiti', 'KaiTi', serif;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.image-subtitle {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.8);
  font-family: 'STKaiti', 'KaiTi', serif;
}

.decorative-elements {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.fan {
  position: absolute;
  width: 120px;
  height: 60px;
  background: linear-gradient(90deg, rgba(156, 47, 47, 0.1) 0%, rgba(194, 139, 78, 0.1) 100%);
  border-radius: 60px 60px 0 0;
}

.fan-left {
  top: -10px;
  left: -30px;
  transform: rotate(-30deg);
}

.fan-right {
  bottom: -10px;
  right: -30px;
  transform: rotate(30deg);
}

.petals {
  position: absolute;
  top: 20%;
  left: 10%;
}

.petal {
  position: absolute;
  width: 12px;
  height: 12px;
  background: rgba(255, 182, 193, 0.6);
  border-radius: 50%;
  animation: float-petal 4s ease-in-out infinite;
}

.petal-1 { top: 0; left: 0; animation-delay: 0s; }
.petal-2 { top: 30px; left: 50px; animation-delay: 0.5s; }
.petal-3 { top: 60px; left: 20px; animation-delay: 1s; }
.petal-4 { top: 90px; left: 70px; animation-delay: 1.5s; }
.petal-5 { top: 120px; left: 30px; animation-delay: 2s; }
.petal-6 { top: 150px; left: 80px; animation-delay: 2.5s; }
.petal-7 { top: 180px; left: 40px; animation-delay: 3s; }
.petal-8 { top: 210px; left: 60px; animation-delay: 3.5s; }

@keyframes float-petal {
  0%, 100% {
    opacity: 0;
    transform: translateY(0) rotate(0deg);
  }
  50% {
    opacity: 1;
    transform: translateY(-20px) rotate(180deg);
  }
}

.login-right {
  width: 55%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
  position: relative;
}

.login-card {
  width: 100%;
  max-width: 360px;
  background: rgba(250, 246, 235, 0.6);
  border-radius: 20px;
  padding: 40px;
  position: relative;
  border: 1px solid rgba(194, 139, 78, 0.1);
}

.card-decoration-top {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #9C2F2F 0%, #C28B4E 30%, #FFD700 50%, #C28B4E 70%, #9C2F2F 100%);
  border-radius: 20px 20px 0 0;
}

.card-decoration-bottom {
  position: absolute;
  bottom: 0;
  left: 20%;
  right: 20%;
  height: 2px;
  background: linear-gradient(90deg, transparent 0%, rgba(194, 139, 78, 0.3) 50%, transparent 100%);
  border-radius: 0 0 2px 2px;
}

.login-header {
  text-align: center;
  margin-bottom: 30px;
}

.logo-section {
  margin-bottom: 16px;
}

.logo {
  width: 56px;
  height: 56px;
  margin: 0 auto;
  background: linear-gradient(135deg, #FAF6EB 0%, #E8D5B8 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 3px solid rgba(194, 139, 78, 0.3);
  box-shadow: 0 4px 16px rgba(194, 139, 78, 0.2);
}

.login-header h1 {
  font-size: 28px;
  font-weight: 700;
  color: #2C5C4D;
  margin: 0 0 8px;
  font-family: 'STKaiti', 'KaiTi', serif;
  letter-spacing: 2px;
}

.subtitle {
  font-size: 13px;
  color: #C28B4E;
  margin: 0;
  font-family: 'STKaiti', 'KaiTi', serif;
}

.welcome-text {
  text-align: center;
  margin-bottom: 30px;
}

.welcome-text h2 {
  font-size: 20px;
  font-weight: 600;
  color: #2C5C4D;
  margin: 0;
}

.login-form {
  width: 100%;
}

.form-group {
  margin-bottom: 20px;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 14px;
  width: 18px;
  height: 18px;
  z-index: 1;
}

.form-group input {
  width: 100%;
  padding: 14px 14px 14px 48px;
  border: 1.5px solid rgba(194, 139, 78, 0.25);
  border-radius: 26px;
  font-size: 14px;
  background: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease;
  outline: none;
}

.form-group input:focus {
  border-color: #C28B4E;
  box-shadow: 0 0 0 3px rgba(194, 139, 78, 0.1);
  background: #fff;
}

.form-group input::placeholder {
  color: rgba(194, 139, 78, 0.5);
}

.form-actions {
  margin-bottom: 20px;
}

.btn-primary {
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg, #9C2F2F 0%, #C28B4E 100%);
  color: white;
  border: none;
  border-radius: 26px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  box-shadow: 0 4px 16px rgba(156, 47, 47, 0.3);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(156, 47, 47, 0.4);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.form-footer {
  text-align: center;
}

.forgot-password {
  margin-bottom: 12px;
}

.forgot-password a {
  font-size: 13px;
  color: #C28B4E;
  text-decoration: none;
  transition: color 0.3s;
}

.forgot-password a:hover {
  color: #9C2F2F;
  text-decoration: underline;
}

.form-footer p {
  font-size: 13px;
  color: #666;
  margin: 0;
}

.form-footer a {
  color: #9C2F2F;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.form-footer a:hover {
  color: #C28B4E;
  text-decoration: underline;
}

.copyright {
  margin-top: 24px;
  font-size: 12px;
  color: rgba(194, 139, 78, 0.6);
}

@media (max-width: 768px) {
  .login-container {
    flex-direction: column;
    height: auto;
    max-width: 400px;
  }
  
  .login-left {
    width: 100%;
    height: 200px;
  }
  
  .login-right {
    width: 100%;
    padding: 30px 20px;
  }
  
  .login-card {
    padding: 30px 24px;
  }
  
  .image-title {
    font-size: 22px;
  }
  
  .image-subtitle {
    font-size: 12px;
  }
  
  .login-header h1 {
    font-size: 24px;
  }
  
  .decorative-elements {
    display: none;
  }
}
</style>