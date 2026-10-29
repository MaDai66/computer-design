<template>
  <div class="settings">
    <div class="settings-header">
      <h2>系统设置</h2>
    </div>

    <!-- 设置选项卡 -->
    <div class="settings-tabs">
      <button 
        v-for="tab in settingTabs" 
        :key="tab.id"
        :class="['tab-btn', { active: activeTab === tab.id }]"
        @click="activeTab = tab.id"
      >
        {{ tab.name }}
      </button>
    </div>

    <!-- 基本设置 -->
    <div v-if="activeTab === 'basic'" class="settings-section">
      <div class="section-header">
        <h3>基本设置</h3>
      </div>
      <div class="settings-form">
        <div class="form-group">
          <label>网站名称</label>
          <input type="text" v-model="settings.siteName" placeholder="请输入网站名称" />
        </div>
        <div class="form-group">
          <label>网站描述</label>
          <textarea v-model="settings.siteDescription" placeholder="请输入网站描述" rows="3"></textarea>
        </div>
        <div class="form-group">
          <label>网站Logo</label>
          <input type="file" @change="handleLogoUpload" />
          <div v-if="settings.logo" class="logo-preview">
            <img :src="settings.logo" alt="Logo" />
          </div>
        </div>
        <div class="form-group">
          <label>联系方式</label>
          <input type="text" v-model="settings.contactPhone" placeholder="请输入联系电话" />
        </div>
        <div class="form-group">
          <label>邮箱地址</label>
          <input type="email" v-model="settings.contactEmail" placeholder="请输入邮箱地址" />
        </div>
      </div>
    </div>

    <!-- 邮件设置 -->
    <div v-if="activeTab === 'email'" class="settings-section">
      <div class="section-header">
        <h3>邮件设置</h3>
      </div>
      <div class="settings-form">
        <div class="form-group">
          <label>SMTP服务器</label>
          <input type="text" v-model="settings.smtpHost" placeholder="请输入SMTP服务器地址" />
        </div>
        <div class="form-group">
          <label>SMTP端口</label>
          <input type="number" v-model="settings.smtpPort" placeholder="请输入SMTP端口" />
        </div>
        <div class="form-group">
          <label>发件人邮箱</label>
          <input type="email" v-model="settings.smtpEmail" placeholder="请输入发件人邮箱" />
        </div>
        <div class="form-group">
          <label>邮箱密码</label>
          <input type="password" v-model="settings.smtpPassword" placeholder="请输入邮箱密码" />
        </div>
        <div class="form-group">
          <label>启用SSL</label>
          <label class="checkbox-label">
            <input type="checkbox" v-model="settings.smtpSSL" />
            <span></span>
          </label>
        </div>
      </div>
    </div>

    <!-- 安全设置 -->
    <div v-if="activeTab === 'security'" class="settings-section">
      <div class="section-header">
        <h3>安全设置</h3>
      </div>
      <div class="settings-form">
        <div class="form-group">
          <label>登录尝试次数限制</label>
          <input type="number" v-model="settings.loginAttempts" placeholder="请输入登录尝试次数" />
        </div>
        <div class="form-group">
          <label>登录锁定时间(分钟)</label>
          <input type="number" v-model="settings.lockoutMinutes" placeholder="请输入锁定时间" />
        </div>
        <div class="form-group">
          <label>密码过期天数</label>
          <input type="number" v-model="settings.passwordExpireDays" placeholder="请输入密码过期天数" />
        </div>
        <div class="form-group">
          <label>启用双因素认证</label>
          <label class="checkbox-label">
            <input type="checkbox" v-model="settings.twoFactorAuth" />
            <span></span>
          </label>
        </div>
      </div>
    </div>

    <!-- 存储设置 -->
    <div v-if="activeTab === 'storage'" class="settings-section">
      <div class="section-header">
        <h3>存储设置</h3>
      </div>
      <div class="settings-form">
        <div class="form-group">
          <label>上传文件大小限制(MB)</label>
          <input type="number" v-model="settings.maxFileSize" placeholder="请输入文件大小限制" />
        </div>
        <div class="form-group">
          <label>允许的文件类型</label>
          <input type="text" v-model="settings.allowedFileTypes" placeholder="例如: jpg,png,gif" />
        </div>
        <div class="form-group">
          <label>图片压缩质量</label>
          <input type="range" v-model="settings.imageQuality" min="10" max="100" />
          <span class="range-value">{{ settings.imageQuality }}%</span>
        </div>
      </div>
    </div>

    <!-- 保存按钮 -->
    <div class="settings-actions">
      <button class="btn btn-secondary" @click="resetSettings">重置</button>
      <button class="btn btn-primary" @click="saveSettings">保存设置</button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const activeTab = ref('basic')
const isSaving = ref(false)

const settingTabs = [
  { id: 'basic', name: '基本设置' },
  { id: 'email', name: '邮件设置' },
  { id: 'security', name: '安全设置' },
  { id: 'storage', name: '存储设置' }
]

// 设置数据
const settings = reactive({
  siteName: '吉韵遗风',
  siteDescription: '吉林非遗旅游文化平台',
  logo: '',
  contactPhone: '400-123-4567',
  contactEmail: 'contact@example.com',
  smtpHost: 'smtp.example.com',
  smtpPort: 587,
  smtpEmail: 'noreply@example.com',
  smtpPassword: '',
  smtpSSL: true,
  loginAttempts: 5,
  lockoutMinutes: 15,
  passwordExpireDays: 90,
  twoFactorAuth: false,
  maxFileSize: 10,
  allowedFileTypes: 'jpg,png,gif,pdf,doc,docx',
  imageQuality: 80
})

// 处理Logo上传
const handleLogoUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      settings.logo = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

// 重置设置
const resetSettings = () => {
  settings.siteName = '吉韵遗风'
  settings.siteDescription = '吉林非遗旅游文化平台'
  settings.logo = ''
  settings.contactPhone = '400-123-4567'
  settings.contactEmail = 'contact@example.com'
  settings.smtpHost = 'smtp.example.com'
  settings.smtpPort = 587
  settings.smtpEmail = 'noreply@example.com'
  settings.smtpPassword = ''
  settings.smtpSSL = true
  settings.loginAttempts = 5
  settings.lockoutMinutes = 15
  settings.passwordExpireDays = 90
  settings.twoFactorAuth = false
  settings.maxFileSize = 10
  settings.allowedFileTypes = 'jpg,png,gif,pdf,doc,docx'
  settings.imageQuality = 80
}

// 保存设置
const saveSettings = async () => {
  isSaving.value = true
  try {
    // 模拟保存操作
    await new Promise(resolve => setTimeout(resolve, 1000))
    alert('设置保存成功！')
  } catch (error) {
    console.error('保存设置失败:', error)
    alert('保存失败，请重试')
  } finally {
    isSaving.value = false
  }
}
</script>

<style scoped>
.settings {
  width: 100%;
}

.settings-header {
  margin-bottom: 30px;
}

.settings-header h2 {
  margin: 0;
  color: #333;
  font-size: 24px;
}

/* 设置选项卡 */
.settings-tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  border-bottom: 1px solid #e0e6ed;
  padding-bottom: 10px;
}

.tab-btn {
  padding: 10px 20px;
  border: none;
  background: none;
  cursor: pointer;
  font-size: 14px;
  color: #666;
  border-bottom: 3px solid transparent;
  transition: all 0.3s;
}

.tab-btn:hover {
  color: #3498db;
}

.tab-btn.active {
  color: #3498db;
  border-bottom-color: #3498db;
  font-weight: 500;
}

/* 设置区域 */
.settings-section {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

.section-header {
  margin-bottom: 20px;
}

.section-header h3 {
  margin: 0;
  color: #333;
  font-size: 18px;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
}

/* 设置表单 */
.settings-form {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  color: #333;
  font-weight: 500;
  font-size: 14px;
}

.form-group input,
.form-group textarea {
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.form-group textarea {
  resize: vertical;
}

.form-group input[type="range"] {
  padding: 0;
}

.range-value {
  font-size: 14px;
  color: #666;
}

/* Logo预览 */
.logo-preview {
  margin-top: 10px;
  width: 100px;
  height: 100px;
  border-radius: 4px;
  overflow: hidden;
}

.logo-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 复选框样式 */
.checkbox-label {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.checkbox-label input[type="checkbox"] {
  width: 18px;
  height: 18px;
}

/* 操作按钮 */
.settings-actions {
  display: flex;
  justify-content: flex-end;
  gap: 15px;
}

.btn {
  padding: 10px 20px;
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

/* 响应式设计 */
@media (max-width: 768px) {
  .settings-form {
    grid-template-columns: 1fr;
  }
  
  .settings-tabs {
    flex-wrap: wrap;
  }
  
  .settings-actions {
    flex-direction: column;
  }
}
</style>