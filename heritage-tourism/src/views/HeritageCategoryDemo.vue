<template>
  <div class="heritage-category-demo" ref="demoRef" @wheel="handleWheel">
    <!-- 背景竖条 -->
    <div class="background-stripes">
      <div v-for="(color, index) in stripeColors" :key="index" class="stripe" :style="{ backgroundColor: color }"></div>
    </div>
    
    <!-- 渐变遮罩 -->
    <div class="overlay-gradient"></div>
    
    <!-- 主内容区 -->
    <div class="content-wrapper">
      <!-- 标题 -->
      <div class="title-section" :class="{ 'animate-title': showAnimation }">
        <div class="vertical-title">
          <span class="title-text">国家级非物质文化遗产代表性项目名录</span>
        </div>
      </div>
      
      <!-- 分类卡片区域 -->
      <div class="category-cards">
        <div 
          v-for="(item, index) in categories" 
          :key="item.id"
          class="category-card"
          :class="[item.colorClass, `card-${index + 1}`, { 'animate-card': showAnimation }]"
          :style="getCardStyle(item)"
          @click="handleCardClick(item)"
        >
          <div class="card-corner corner-top-left"></div>
          <div class="card-corner corner-top-right"></div>
          <div class="card-corner corner-bottom-left"></div>
          <div class="card-corner corner-bottom-right"></div>
          
          <div class="card-icon">
            <svg :viewBox="item.svgViewBox" fill="none" stroke="currentColor" stroke-width="1.5">
              <path :d="item.svgPath" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          
          <div class="card-title">{{ item.title }}</div>
        </div>
      </div>
      
      <!-- 滚动提示 -->
      <div class="scroll-hint">
        <span class="scroll-text">向下滚动跳过</span>
        <div class="scroll-arrow"></div>
      </div>
      
      <!-- 底部热点推荐 -->
      <div class="hot-recommend" :class="{ 'animate-recommend': showAnimation }">
        <div class="recommend-content">
          <div class="recommend-label">热点推荐</div>
          <div class="recommend-items">
            <span v-for="(item, index) in hotItems" :key="index" class="recommend-item">
              <span class="item-dot">◆</span>
              {{ item }}
            </span>
          </div>
        </div>
        <button class="close-btn">×</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const showAnimation = ref(false)
const demoRef = ref(null)

const getCardStyle = (item) => {
  return {
    '--animation-delay': `${item.delay}s`,
    '--animation-direction': item.direction,
    '--card-height': item.height,
    '--card-width': item.width,
    '--card-left': item.left,
    '--card-top': item.top
  }
}

const handleWheel = (event) => {
  const demo = demoRef.value
  if (!demo) return
  
  const demoRect = demo.getBoundingClientRect()
  const demoHeight = demo.offsetHeight
  
  const isDemoInView = demoRect.top <= 100 && demoRect.bottom >= window.innerHeight * 0.3
  
  if (isDemoInView) {
    if (event.deltaY > 50) {
      event.preventDefault()
      window.scrollTo({
        top: demoHeight,
        behavior: 'smooth'
      })
    } else if (event.deltaY < -50 && window.scrollY > 50) {
      event.preventDefault()
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      })
    }
  }
}

const stripeColors = [
  '#1E4A3D', '#2D5A4D', '#3D6A5D', '#4D7A6D', '#5D8A7D',
  '#8B4536', '#9B5546', '#AB6556', '#BB7566', '#CB8576',
  '#4A5568', '#5A6578', '#6A7588', '#7A8598', '#8A95A8',
  '#2D5A4D', '#3D6A5D', '#4D7A6D', '#5D8A7D', '#6D9A8D',
  '#8B4536', '#9B5546', '#AB6556', '#BB7566', '#CB8576'
]

const categories = [
  {
    id: 1,
    title: '[民间文学]',
    colorClass: 'card-beige',
    svgViewBox: '0 0 60 80',
    svgPath: 'M10 60h40v-5H15v-30h30v-5H10v40zM15 50h30v-25H15v25z',
    width: '150px',
    height: '180px',
    left: '15%',
    top: '30%',
    delay: 0.1,
    direction: 'top'
  },
  {
    id: 2,
    title: '[传统音乐]',
    colorClass: 'card-red',
    svgViewBox: '0 0 60 80',
    svgPath: 'M22 10v60M28 10v60M25 65a15 15 0 100-30 15 15 0 000 30z',
    width: '140px',
    height: '160px',
    left: '28%',
    top: '50%',
    delay: 0.25,
    direction: 'bottom'
  },
  {
    id: 3,
    title: '[传统舞蹈]',
    colorClass: 'card-brown',
    svgViewBox: '0 0 60 80',
    svgPath: 'M30 5C20 15 15 30 15 50c0 15 5 25 15 30s15-10 15-25 5-35-15-45z',
    width: '160px',
    height: '200px',
    left: '35%',
    top: '15%',
    delay: 0.15,
    direction: 'top'
  },
  {
    id: 4,
    title: '[传统戏剧]',
    colorClass: 'card-blue',
    svgViewBox: '0 0 60 80',
    svgPath: 'M30 5L10 20v50l20 15 20-15V20L30 5zm-5 30a15 15 0 1010 0 15 15 0 00-10 0z',
    width: '150px',
    height: '180px',
    left: '45%',
    top: '40%',
    delay: 0.3,
    direction: 'bottom'
  },
  {
    id: 5,
    title: '[曲艺]',
    colorClass: 'card-light-blue',
    svgViewBox: '0 0 60 80',
    svgPath: 'M30 10c-10 5-15 15-15 30s5 25 15 30c10-5 15-15 15-30s-5-25-15-30zm0 15a10 15 0 110 30 10 15 0 010-30z',
    width: '140px',
    height: '220px',
    left: '52%',
    top: '65%',
    delay: 0.45,
    direction: 'bottom'
  },
  {
    id: 6,
    title: '[传统体育、游艺与杂技]',
    colorClass: 'card-red-accent',
    svgViewBox: '0 0 60 80',
    svgPath: 'M30 10l15 15-15 15-15-15 15-15zm0 25l15 15-15 15-15-15 15-15z',
    width: '150px',
    height: '170px',
    left: '55%',
    top: '30%',
    delay: 0.35,
    direction: 'top'
  },
  {
    id: 7,
    title: '[传统美术]',
    colorClass: 'card-green',
    svgViewBox: '0 0 60 80',
    svgPath: 'M30 10c-15 0-25 10-25 25s10 25 25 35 25-10 25-25-10-25-25-35zm0 15a10 15 0 110 30 10 15 0 010-30z',
    width: '160px',
    height: '190px',
    left: '65%',
    top: '45%',
    delay: 0.4,
    direction: 'bottom'
  },
  {
    id: 8,
    title: '[传统技艺]',
    colorClass: 'card-brown-accent',
    svgViewBox: '0 0 60 80',
    svgPath: 'M15 20h30v50H15V20zm5 10h20v30H20V30z',
    width: '140px',
    height: '170px',
    left: '78%',
    top: '20%',
    delay: 0.2,
    direction: 'top'
  },
  {
    id: 9,
    title: '[传统医药]',
    colorClass: 'card-red-dark',
    svgViewBox: '0 0 60 80',
    svgPath: 'M30 10c-10 5-15 15-15 30s5 25 15 30c10-5 15-15 15-30s-5-25-15-30zm0 10a5 20 0 110 40 5 20 0 010-40z',
    width: '150px',
    height: '200px',
    left: '82%',
    top: '60%',
    delay: 0.5,
    direction: 'bottom'
  },
  {
    id: 10,
    title: '[民俗]',
    colorClass: 'card-light-blue-accent',
    svgViewBox: '0 0 60 80',
    svgPath: 'M30 5l5 20h-10l5-20zm-5 25l5 15 5-15-5-15-5 15zm10 20l-5 15-5-15 5-15 5 15z',
    width: '160px',
    height: '180px',
    left: '92%',
    top: '40%',
    delay: 0.55,
    direction: 'top'
  }
]

const hotItems = ['太极拳', '欢欢喜喜过大年——蛇年春节专题', '二十四节气']

const handleCardClick = (item) => {
  console.log('Clicked:', item.title)
}

onMounted(() => {
  setTimeout(() => {
    showAnimation.value = true
  }, 100)
})
</script>

<style scoped>
.heritage-category-demo {
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  height: 100vh;
}

.background-stripes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  z-index: 1;
}

.stripe {
  flex: 1;
  min-width: 40px;
}

.overlay-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.3) 0%,
    rgba(0, 0, 0, 0.1) 30%,
    rgba(0, 0, 0, 0) 50%,
    rgba(0, 0, 0, 0.4) 80%,
    rgba(0, 0, 0, 0.6) 100%
  );
  z-index: 5;
}

.content-wrapper {
  position: relative;
  z-index: 10;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.title-section {
  position: fixed;
  left: 30px;
  top: 50%;
  transform: translateY(-50%) translateX(-50px);
  z-index: 20;
  opacity: 0;
}

.title-section.animate-title {
  animation: slideInLeft 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateY(-50%) translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateY(-50%) translateX(0);
  }
}

.vertical-title {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title-text {
  writing-mode: vertical-rl;
  font-size: 20px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  letter-spacing: 8px;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.4);
  font-family: 'STKaiti', 'KaiTi', serif;
}

.category-cards {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 100px;
}

.category-card {
  width: var(--card-width, 140px);
  height: var(--card-height, 180px);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: absolute;
  left: var(--card-left, 50%);
  top: var(--card-top, 50%);
  transform: translate(-50%, -50%);
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.1);
  opacity: 0;
}

.category-card.animate-card {
  animation: slideIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  animation-delay: var(--animation-delay);
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translate(-50%, calc(-50% + (var(--animation-direction) === 'top' ? -150px : 150px)));
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%);
  }
}

.category-card:hover {
  transform: translate(-50%, -50%) scale(1.08);
  z-index: 100 !important;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
}

.category-card.animate-card:hover {
  animation: none;
}

.card-corner {
  position: absolute;
  width: 12px;
  height: 12px;
  border-color: rgba(255, 255, 255, 0.4);
  border-style: solid;
  border-width: 0;
}

.corner-top-left {
  top: 8px;
  left: 8px;
  border-top-width: 2px;
  border-left-width: 2px;
}

.corner-top-right {
  top: 8px;
  right: 8px;
  border-top-width: 2px;
  border-right-width: 2px;
}

.corner-bottom-left {
  bottom: 8px;
  left: 8px;
  border-bottom-width: 2px;
  border-left-width: 2px;
}

.corner-bottom-right {
  bottom: 8px;
  right: 8px;
  border-bottom-width: 2px;
  border-right-width: 2px;
}

.card-icon {
  width: 50px;
  height: 50px;
  margin-bottom: 12px;
  color: rgba(255, 255, 255, 0.9);
}

.card-icon svg {
  width: 100%;
  height: 100%;
}

.card-title {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.95);
  text-align: center;
  font-weight: 500;
  letter-spacing: 1px;
}

/* 卡片颜色 */
.card-beige {
  background: linear-gradient(135deg, #D4C4A8 0%, #B8A488 100%);
}

.card-red {
  background: linear-gradient(135deg, #8B2635 0%, #6B1F29 100%);
}

.card-brown {
  background: linear-gradient(135deg, #C4A35A 0%, #A4834A 100%);
}

.card-blue {
  background: linear-gradient(135deg, #4A5568 0%, #3A4558 100%);
}

.card-light-blue {
  background: linear-gradient(135deg, #718096 0%, #516076 100%);
}

.card-red-accent {
  background: linear-gradient(135deg, #9B2226 0%, #7B1A1E 100%);
}

.card-green {
  background: linear-gradient(135deg, #2D6A4F 0%, #1D5A3F 100%);
}

.card-brown-accent {
  background: linear-gradient(135deg, #B08968 0%, #906948 100%);
}

.card-red-dark {
  background: linear-gradient(135deg, #720909 0%, #520707 100%);
}

.card-light-blue-accent {
  background: linear-gradient(135deg, #94A3B8 0%, #748398 100%);
}

/* 卡片位置错落 */
.card-1 { transform: translate(0, 30px); }
.card-2 { transform: translate(10px, 80px); }
.card-3 { transform: translate(-20px, 20px); }
.card-4 { transform: translate(30px, 60px); }
.card-5 { transform: translate(-10px, 100px); }
.card-6 { transform: translate(40px, 40px); }
.card-7 { transform: translate(-30px, 70px); }
.card-8 { transform: translate(20px, 90px); }
.card-9 { transform: translate(0, 50px); }
.card-10 { transform: translate(15px, 20px); }

/* 滚动提示 */
.scroll-hint {
  position: absolute;
  bottom: 140px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 20;
  color: var(--white);
}

.scroll-text {
  font-size: 14px;
  margin-bottom: 12px;
  opacity: 0.8;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.scroll-arrow {
  width: 24px;
  height: 40px;
  border: 2px solid rgba(255, 255, 255, 0.6);
  border-radius: 12px;
  position: relative;
  animation: bounce 2s ease-in-out infinite;
}

.scroll-arrow::before {
  content: '';
  position: absolute;
  top: 8px;
  left: 50%;
  transform: translateX(-50%);
  width: 6px;
  height: 6px;
  background-color: var(--white);
  border-radius: 50%;
  animation: scrollDown 1.5s ease-in-out infinite;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(10px);
  }
}

@keyframes scrollDown {
  0% {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
  }
  100% {
    transform: translateX(-50%) translateY(20px);
    opacity: 0;
  }
}

.hot-recommend {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(135deg, rgba(139, 69, 54, 0.95) 0%, rgba(109, 54, 40, 0.95) 100%);
  backdrop-filter: blur(10px);
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 30;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  transform: translateY(100%);
  opacity: 0;
}

.hot-recommend.animate-recommend {
  animation: slideInUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  animation-delay: 1.2s;
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(100%);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.recommend-content {
  display: flex;
  align-items: center;
  gap: 30px;
}

.recommend-label {
  font-size: 16px;
  font-weight: 600;
  color: #FFD700;
  letter-spacing: 2px;
}

.recommend-items {
  display: flex;
  gap: 40px;
}

.recommend-item {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.9);
  display: flex;
  align-items: center;
  gap: 8px;
}

.item-dot {
  color: #FFD700;
  font-size: 12px;
}

.close-btn {
  width: 32px;
  height: 32px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  background: transparent;
  color: rgba(255, 255, 255, 0.7);
  font-size: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}

@media (max-width: 768px) {
  .title-section {
    display: none;
  }
  
  .category-cards {
    padding: 80px 20px 120px;
    gap: 15px;
  }
  
  .category-card {
    width: 120px;
    height: 150px;
  }
  
  .card-icon {
    width: 40px;
    height: 40px;
  }
  
  .card-title {
    font-size: 12px;
  }
  
  .hot-recommend {
    padding: 15px 20px;
  }
  
  .recommend-content {
    gap: 20px;
  }
  
  .recommend-items {
    gap: 20px;
  }
  
  /* 移除错落效果，改为网格布局 */
  .card-1, .card-2, .card-3, .card-4, .card-5,
  .card-6, .card-7, .card-8, .card-9, .card-10 {
    transform: none;
  }
}
</style>