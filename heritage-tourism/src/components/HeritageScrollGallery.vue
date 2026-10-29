<template>
  <section class="heritage-scroll-gallery">
    <!-- 左侧固定区域 -->
    <div class="left-panel">
      <div class="panel-decoration top"></div>
      <div class="panel-content">
        <div class="decorative-line"></div>
        <h2 class="panel-title">国家级非物质文化遗产代表性项目名录</h2>
        <div class="decorative-line"></div>
      </div>
      <div class="panel-decoration bottom"></div>
    </div>
    
    <!-- 右侧滚动区域 -->
    <div class="right-scroll-container" ref="scrollContainer">
      <div class="scroll-track" ref="trackRef">
        <div 
          v-for="(item, index) in galleryItems" 
          :key="item.id" 
          class="gallery-item"
          :class="{ active: activeIndex === index }"
          @mouseenter="handleItemHover(index)"
        >
          <div class="item-inner" :style="{ background: item.bgColor }">
            <div class="item-pattern"></div>
            <img :src="item.image" :alt="item.title" class="item-image" />
            <div class="item-link" @click="handleItemClick(item)">
              <div class="item-content">
                <div class="item-decoration"></div>
                <span class="item-title">{{ item.title }}</span>
                <div class="item-divider"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import img1 from '../assets/shouye/1.png'
import img2 from '../assets/shouye/2.png'
import img3 from '../assets/shouye/3.png'
import img4 from '../assets/shouye/4.png'
import img5 from '../assets/shouye/5.png'

const scrollContainer = ref(null)
const trackRef = ref(null)
const activeIndex = ref(0)

const galleryItems = [
  {
    id: 1,
    title: '智游',
    image: img1,
    bgColor: 'linear-gradient(180deg, #F5E6D3 0%, #E8D4BC 100%)',
    path: '/smart-tour'
  },
  {
    id: 2,
    title: '遗珍',
    image: img2,
    bgColor: 'linear-gradient(180deg, #8B5A2B 0%, #6B4A1B 100%)',
    path: '/heritage'
  },
  {
    id: 3,
    title: '乡宿',
    image: img3,
    bgColor: 'linear-gradient(180deg, #2C3E50 0%, #1C2E3E 100%)',
    path: '/homestay'
  },
  {
    id: 4,
    title: '吉礼',
    image: img4,
    bgColor: 'linear-gradient(180deg, #8B2635 0%, #6B1F29 100%)',
    path: '/gifts'
  },
  {
    id: 5,
    title: '个人中心',
    image: img5,
    bgColor: 'linear-gradient(180deg, #7B3F00 0%, #5B2F00 100%)',
    path: '/profile'
  },

]

const handleItemHover = (index) => {
  activeIndex.value = index
}

const handleItemClick = (item) => {
  if (item.path === '/profile') {
    const token = localStorage.getItem('token')
    if (!token) {
      window.location.href = '/login'
      return
    }
  }
  window.location.href = item.path
}
</script>

<style scoped>
.heritage-scroll-gallery {
  width: 100%;
  height: 100vh;
  display: flex;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  position: relative;
  overflow: hidden;
}

/* 左侧固定面板 */
.left-panel {
  width: 250px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg, #1E4A3D 0%, #0E3A2D 100%);
  position: relative;
  height: 100%;
  box-sizing: border-box;
}

.panel-decoration {
  position: absolute;
  width: 80px;
  height: 60px;
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.panel-decoration.top {
  top: 20px;
  border-bottom: none;
}

.panel-decoration.bottom {
  bottom: 20px;
  border-top: none;
}

.panel-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 20px;
}

.decorative-line {
  width: 40px;
  height: 60px;
  background: repeating-linear-gradient(
    0deg,
    rgba(255, 255, 255, 0.3) 0px,
    rgba(255, 255, 255, 0.3) 2px,
    transparent 2px,
    transparent 8px
  );
}

.panel-title {
  writing-mode: vertical-rl;
  font-size: 18px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  letter-spacing: 6px;
  margin: 20px 0;
  font-family: 'STKaiti', 'KaiTi', serif;
}

/* 右侧滚动区域 */
.right-scroll-container {
  flex: 1;
  overflow: hidden;
  height: 100vh;
  display: flex;
}

.right-scroll-container::-webkit-scrollbar {
  display: none;
}

.scroll-track {
  display: flex;
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
}

.gallery-item {
  flex: 1;
  height: 100%;
  margin: 0;
  transition: flex 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275),
              transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275), 
              z-index 0s linear;
  cursor: pointer;
  position: relative;
}

.gallery-item:first-child {
  margin-left: 0;
}

.gallery-item:last-child {
  margin-right: 0;
}

.gallery-item:hover,
.gallery-item.active {
  flex: 1.8;
  z-index: 10;
}

.heritage-scroll-gallery:hover .gallery-item:not(:hover):not(.active) {
  flex: 0.9;
}

.item-inner {
  width: 100%;
  height: 100%;
  position: relative;
  border-radius: 0;
  overflow: hidden;
  box-shadow: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.item-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='40' cy='40' r='35' fill='none' stroke='rgba(255,255,255,0.05)' stroke-width='1'/%3E%3Ccircle cx='40' cy='40' r='25' fill='none' stroke='rgba(255,255,255,0.05)' stroke-width='1'/%3E%3Ccircle cx='40' cy='40' r='15' fill='none' stroke='rgba(255,255,255,0.05)' stroke-width='1'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 2;
}

.item-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: left center;
  background: inherit;
  transition: object-position 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border-radius: 0;
}

.gallery-item:hover .item-image,
.gallery-item.active .item-image {
  object-position: center center;
}

.item-link {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 80px;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: linear-gradient(90deg, transparent 0%, rgba(0, 0, 0, 0.4) 100%);
  padding: 20px 15px;
  z-index: 3;
  text-decoration: none;
}

.item-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.item-decoration {
  width: 30px;
  height: 1px;
  background: rgba(255, 255, 255, 0.4);
  margin-bottom: 15px;
}

.item-title {
  writing-mode: vertical-rl;
  font-size: 14px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.9);
  letter-spacing: 3px;
  font-family: 'STKaiti', 'KaiTi', serif;
  white-space: nowrap;
}

.item-divider {
  width: 20px;
  height: 40px;
  background: repeating-linear-gradient(
    0deg,
    rgba(255, 255, 255, 0.3) 0px,
    rgba(255, 255, 255, 0.3) 2px,
    transparent 2px,
    transparent 6px
  );
  margin: 15px 0;
}

@media (max-width: 768px) {
  .left-panel {
    display: none;
  }
  
  .gallery-item {
    flex: 0 0 280px;
    margin-right: -40px;
  }
  
  .gallery-item:first-child {
    margin-left: 20px;
  }
  
  .gallery-item:last-child {
    margin-right: 20px;
  }
  
  .item-content {
    width: 60px;
    padding: 15px 10px;
  }
  
  .item-title {
    font-size: 12px;
  }
}
</style>
