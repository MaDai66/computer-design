<template>
  <div class="ar-interaction">
    <!-- 顶部导航 -->
    <header class="ar-header">
      <div class="container">
        <div class="header-content">
          <button class="back-btn" @click="goBack">返回</button>
          <h1>AR非遗互动</h1>
          <div class="header-actions">
            <button class="help-btn">帮助</button>
          </div>
        </div>
      </div>
    </header>

    <!-- 主视觉区 -->
    <main class="ar-main">
      <div class="container">
        <!-- PC端引导 -->
        <div v-if="isPC" class="pc-guide">
          <div class="guide-content">
            <h2>用手机体验AR</h2>
            <p>扫描下方二维码，用手机打开体验</p>
            <div class="qrcode">
              <img src="/src/assets/QQ20260416-094938.png" alt="AR体验二维码" />
              <img src="/src/assets/展示.png" alt="AR体验二维码" />
            </div>
            <p class="qrcode-desc">或直接在手机浏览器中输入：<br />https://www.kivicube.com/face-scenes/2pcx1ZeTnrynLZPGZQnoZauZ7Ljy2Mgu</p>
          </div>
        </div>

        <!-- 移动端体验 -->
        <div v-else class="mobile-experience">
          <!-- 体验模式选择 -->
          <div class="experience-modes">
            <button 
              class="mode-btn" 
              :class="{ 'active': selectedMode === 'image' }" 
              @click="selectMode('image')"
            >
              图像识别AR
            </button>
            <button 
              class="mode-btn" 
              :class="{ 'active': selectedMode === 'space' }" 
              @click="selectMode('space')"
            >
              空间AR
            </button>
          </div>

          <!-- 图像识别AR -->
          <div v-if="selectedMode === 'image'" class="image-ar">
            <h3>图像识别AR</h3>
            <p>扫描下方图片，体验AR效果</p>
            <div class="recognition-image">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20pattern%20AR%20recognition&image_size=square" alt="满族剪纸纹样" />
              <div class="image-overlay">
                <span class="scan-hint">请用手机扫描此图</span>
              </div>
            </div>
            <div class="ar-features">
              <div class="feature-item">
                <span class="feature-icon">🎭</span>
                <p>满族剪纸动画</p>
              </div>
              <div class="feature-item">
                <span class="feature-icon">💃</span>
                <p>朝鲜族农乐舞</p>
              </div>
              <div class="feature-item">
                <span class="feature-icon">🎨</span>
                <p>非遗文化介绍</p>
              </div>
            </div>
          </div>

          <!-- 空间AR -->
          <div v-if="selectedMode === 'space'" class="space-ar">
            <h3>空间AR</h3>
            <p>将非遗模型放置在现实空间中</p>
            <div class="space-ar-preview">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=AR%20inkstone%20in%20real%20space&image_size=landscape_16_9" alt="空间AR预览" />
            </div>
            <button class="start-ar-btn" @click="startSpaceAR">开始空间AR</button>
            <div class="ar-features">
              <div class="feature-item">
                <span class="feature-icon">🖋️</span>
                <p>松花砚3D模型</p>
              </div>
              <div class="feature-item">
                <span class="feature-icon">🍚</span>
                <p>打糕制作流程</p>
              </div>
              <div class="feature-item">
                <span class="feature-icon">🔍</span>
                <p>360°查看细节</p>
              </div>
            </div>
          </div>

          <!-- 分享功能 -->
          <div class="share-section">
            <h3>分享体验</h3>
            <p>拍照/录屏分享，生成非遗AR海报</p>
            <div class="share-buttons">
              <button class="share-btn">
                <span class="share-icon">📷</span>
                拍照分享
              </button>
              <button class="share-btn">
                <span class="share-icon">🎥</span>
                录屏分享
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- 底部区域 -->
    <footer class="ar-footer">
      <div class="container">
        <div class="footer-content">
          <div class="ar-info">
            <h3>AR体验说明</h3>
            <ul>
              <li>确保手机摄像头正常工作</li>
              <li>在光线充足的环境中体验</li>
              <li>保持手机稳定，距离识别图约30cm</li>
              <li>空间AR需要较大的平面空间</li>
            </ul>
          </div>
          <div class="related-links">
            <h3>相关链接</h3>
            <button class="link-btn" @click="goToExperience">非遗体验课预订</button>
            <button class="link-btn" @click="goToProducts">AR同款文创</button>
          </div>
        </div>
      </div>
    </footer>

    <!-- 体验完成弹窗 -->
    <div v-if="showCouponModal" class="coupon-modal">
      <div class="modal-content">
        <button class="close-modal" @click="closeCouponModal">&times;</button>
        <div class="coupon-header">
          <span class="coupon-icon">🎁</span>
          <h3>恭喜完成AR体验</h3>
        </div>
        <div class="coupon-body">
          <p>获得线下体验优惠券</p>
          <div class="coupon-code">
            <span class="code">AR2026</span>
            <span class="discount">立减50元</span>
          </div>
          <p class="coupon-desc">适用于所有非遗手作课</p>
        </div>
        <button class="book-now-btn" @click="bookOfflineExperience">立即预约</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const selectedMode = ref('image')
const showCouponModal = ref(false)

// 判断是否为PC端
const isPC = computed(() => {
  return window.innerWidth >= 768
})

// 返回上一页
const goBack = () => {
  router.back()
}

// 选择体验模式
const selectMode = (mode) => {
  selectedMode.value = mode
}

// 开始空间AR
const startSpaceAR = () => {
  // 模拟请求相机权限
  console.log('请求相机权限...')
  setTimeout(() => {
    console.log('相机权限已授予')
    // 这里可以集成真实的AR库，如AR.js等
    alert('空间AR已启动，请将摄像头对准平面区域')
  }, 1000)
}

// 跳转到体验课预订
const goToExperience = () => {
  router.push('/experience-booking')
}

// 跳转到文创产品
const goToProducts = () => {
  router.push('/gifts')
}

// 关闭优惠券弹窗
const closeCouponModal = () => {
  showCouponModal.value = false
}

// 预约线下体验
const bookOfflineExperience = () => {
  router.push('/booking')
}

// 模拟体验完成后显示优惠券
onMounted(() => {
  // 模拟用户完成AR体验后显示优惠券
  setTimeout(() => {
    // 这里可以根据实际AR体验完成情况来触发
    // showCouponModal.value = true
  }, 30000)
})
</script>

<style scoped>
/* 全局样式 */
.ar-interaction {
  min-height: 100vh;
  background-color: var(--bg-color);
}

/* 顶部导航 */
.ar-header {
  background-color: var(--primary-color);
  color: var(--white);
  padding: 16px 0;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.back-btn,
.help-btn {
  background: none;
  border: none;
  color: var(--white);
  font-size: 16px;
  cursor: pointer;
  padding: 8px 16px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.back-btn:hover,
.help-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.ar-header h1 {
  font-size: 24px;
  font-weight: 700;
  margin: 0;
}

/* 主视觉区 */
.ar-main {
  padding: 64px 0;
}

/* PC端引导 */
.pc-guide {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 600px;
}

.guide-content {
  background-color: var(--white);
  padding: 48px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  text-align: center;
  max-width: 500px;
  width: 100%;
}

.guide-content h2 {
  margin-top: 0;
  margin-bottom: 16px;
  color: var(--text-dark);
}

.guide-content p {
  margin-bottom: 32px;
  color: var(--text-medium);
}

.qrcode {
  display: flex;
  justify-content: center;
  gap: 25px;
  margin-bottom: 20px;
}

.qrcode img {
  width: 200px;
  height: 200px;
  object-fit: contain;
}

.qrcode-desc {
  font-size: 14px;
  color: var(--text-light);
}

/* 移动端体验 */
.mobile-experience {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  padding: 32px;
}

/* 体验模式选择 */
.experience-modes {
  display: flex;
  gap: 16px;
  margin-bottom: 32px;
}

.mode-btn {
  flex: 1;
  padding: 16px;
  border: 2px solid var(--border-color);
  background-color: var(--white);
  border-radius: var(--radius-md);
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

.mode-btn:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
}

.mode-btn.active {
  background-color: var(--primary-color);
  color: var(--white);
  border-color: var(--primary-color);
}

/* 图像识别AR */
.image-ar h3,
.space-ar h3 {
  margin-top: 0;
  margin-bottom: 16px;
  color: var(--text-dark);
}

.image-ar p,
.space-ar p {
  margin-bottom: 24px;
  color: var(--text-medium);
}

.recognition-image {
  position: relative;
  margin-bottom: 32px;
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow);
}

.recognition-image img {
  width: 100%;
  max-width: 400px;
  height: auto;
  display: block;
  margin: 0 auto;
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
}

.scan-hint {
  color: var(--white);
  font-size: 18px;
  font-weight: 600;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

/* 空间AR */
.space-ar-preview {
  margin-bottom: 24px;
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow);
}

.space-ar-preview img {
  width: 100%;
  height: auto;
  display: block;
}

.start-ar-btn {
  display: block;
  width: 100%;
  padding: 16px;
  background-color: var(--primary-color);
  color: var(--white);
  border: none;
  border-radius: var(--radius-md);
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-bottom: 32px;
}

.start-ar-btn:hover {
  background-color: var(--primary-dark);
}

/* AR功能 */
.ar-features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 16px;
  margin-bottom: 32px;
}

.feature-item {
  text-align: center;
  padding: 16px;
  background-color: var(--bg-color);
  border-radius: var(--radius-md);
}

.feature-icon {
  font-size: 32px;
  display: block;
  margin-bottom: 8px;
}

.feature-item p {
  margin: 0;
  font-size: 14px;
  color: var(--text-medium);
}

/* 分享功能 */
.share-section {
  margin-top: 48px;
  padding-top: 32px;
  border-top: 1px solid var(--border-color);
}

.share-section h3 {
  margin-top: 0;
  margin-bottom: 16px;
  color: var(--text-dark);
}

.share-section p {
  margin-bottom: 24px;
  color: var(--text-medium);
}

.share-buttons {
  display: flex;
  gap: 16px;
}

.share-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 16px;
  background-color: var(--bg-color);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s;
}

.share-btn:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
}

.share-icon {
  font-size: 18px;
}

/* 底部区域 */
.ar-footer {
  background-color: var(--white);
  padding: 48px 0;
  border-top: 1px solid var(--border-color);
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 32px;
}

.ar-info h3,
.related-links h3 {
  margin-top: 0;
  margin-bottom: 16px;
  color: var(--text-dark);
}

.ar-info ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.ar-info li {
  padding: 8px 0;
  color: var(--text-medium);
  position: relative;
  padding-left: 20px;
}

.ar-info li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary-color);
  font-weight: bold;
}

.related-links {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.link-btn {
  padding: 12px 24px;
  background-color: var(--bg-color);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s;
  text-align: center;
}

.link-btn:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
}

/* 优惠券弹窗 */
.coupon-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: var(--white);
  padding: 32px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  max-width: 400px;
  width: 90%;
  position: relative;
  text-align: center;
}

.close-modal {
  position: absolute;
  top: 12px;
  right: 12px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.coupon-header {
  margin-bottom: 24px;
}

.coupon-icon {
  font-size: 48px;
  display: block;
  margin-bottom: 16px;
}

.coupon-header h3 {
  margin: 0;
  color: var(--text-dark);
}

.coupon-body {
  margin-bottom: 32px;
}

.coupon-body p {
  margin: 0 0 16px 0;
  color: var(--text-medium);
}

.coupon-code {
  background-color: var(--primary-color);
  color: var(--white);
  padding: 16px;
  border-radius: var(--radius-md);
  margin-bottom: 16px;
  font-size: 24px;
  font-weight: 700;
}

.coupon-desc {
  font-size: 14px;
  color: var(--text-light);
}

.book-now-btn {
  width: 100%;
  padding: 16px;
  background-color: var(--primary-color);
  color: var(--white);
  border: none;
  border-radius: var(--radius-md);
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
}

.book-now-btn:hover {
  background-color: var(--primary-dark);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .ar-main {
    padding: 32px 0;
  }
  
  .mobile-experience {
    padding: 24px;
  }
  
  .experience-modes {
    flex-direction: column;
  }
  
  .ar-features {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .share-buttons {
    flex-direction: column;
  }
  
  .footer-content {
    grid-template-columns: 1fr;
  }
}
</style>