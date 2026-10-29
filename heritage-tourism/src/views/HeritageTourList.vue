<template>
  <div class="heritage-tour-list">
    <div class="container">
      <h1 class="page-title">非遗主题游</h1>
      
      <div class="tour-items">
        <div class="tour-item" v-for="(item, index) in tourItems" :key="index">
          <div class="item-image">
            <img :src="item.image" :alt="item.title" />
          </div>
          <div class="item-content">
            <h3 class="item-title">{{ item.title }}</h3>
            <div class="item-info">
              <span class="tour-days">{{ item.days }}</span>
              <span class="tour-experience">{{ item.experienceCount }}个非遗体验点</span>
            </div>
            <p class="item-description">{{ item.description }}</p>
            <div class="item-footer">
              <span class="item-price">{{ item.price }}</span>
              <button class="btn btn-secondary">查看详情</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const showBackToTop = ref(false)

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}


onMounted(() => {
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.heritage-tour-list {
  padding: 48px 0;
  background-color: var(--bg-light);
}

.page-title {
  font-size: 28px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 32px;
  text-align: center;
}

.tour-items {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.tour-item {
  display: flex;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.tour-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}

.item-image {
  flex: 0 0 400px;
}

.item-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-content {
  flex: 1;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.item-title {
  font-size: 20px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 12px;
}

.item-info {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
}

.tour-days,
.tour-experience {
  font-size: 14px;
  color: var(--text-medium);
  padding: 4px 12px;
  background-color: var(--bg-light);
  border-radius: 20px;
}

.item-description {
  font-size: 14px;
  color: var(--text-medium);
  line-height: 1.5;
  margin-bottom: 20px;
}

.item-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.item-price {
  font-size: 18px;
  font-weight: 600;
  color: var(--accent-orange);
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: var(--radius-md);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.btn-secondary {
  background-color: transparent;
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
}

.btn-secondary:hover {
  background-color: var(--primary-color);
  color: var(--white);
}

/* Responsive */
@media (max-width: 768px) {
  .tour-item {
    flex-direction: column;
  }
  
  .item-image {
    flex: 0 0 200px;
  }
  
  .item-content {
    padding: 20px;
  }
  
  .page-title {
    font-size: 24px;
  }
  
  .item-title {
    font-size: 18px;
  }
  
  .back-to-top {
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
}

/* Back to Top Button */
.back-to-top {
  position: fixed;
  bottom: 32px;
  right: 32px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: var(--primary-color);
  color: var(--white);
  border: none;
  font-size: 20px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: var(--shadow-hover);
  transition: var(--transition);
  z-index: 100;
}

.back-to-top:hover {
  background-color: var(--primary-dark);
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}
</style>