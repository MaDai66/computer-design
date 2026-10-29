<template>
  <div class="smart-tour" :style="{ '--bg-image': `url(${backgroundImage})` }">
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1>智游吉林</h1>
        <p>智能推荐路线，探索非遗文化</p>
      </div>
    </section>

    <!-- 智能搜索栏 -->
    <section class="search-section">
      <div class="container">
        <div class="search-box">
          <input 
            type="text" 
            placeholder="搜索目的地、非遗体验..." 
            class="search-input" 
            v-model="searchKeyword"
            @keyup.enter="searchRoutes"
          />
          <button class="search-btn" @click="searchRoutes">
            <span>🔍</span>
          </button>
          <button v-if="searchKeyword" class="clear-btn" @click="clearSearch">
            <span>✕</span>
          </button>
        </div>

      </div>
    </section>

    <!-- 地图/列表切换 -->
    <section class="content-section">
      <div class="container">
        <!-- 加载状态 -->
        <div v-if="loading" class="loading-state">
          <p>加载中...</p>
        </div>

        <!-- 错误状态 -->
        <div v-else-if="error" class="error-state">
          <p>{{ error }}</p>
          <button class="btn btn-secondary" @click="fetchRoutes">重新加载</button>
        </div>

        <!-- 搜索结果 -->
        <div v-else-if="showSearchResults" class="search-results">
          <div class="search-results-header">
            <h2>搜索结果</h2>
            <button class="btn btn-secondary" @click="clearSearch">清除搜索</button>
          </div>
          <div v-if="filteredRoutes.length > 0" class="search-results-list">
            <div class="route-card" v-for="route in filteredRoutes" :key="route.id">
              <img :src="route.image" :alt="route.name" />
              <div class="route-content">
                <div class="route-header">
                  <h3>{{ route.name }}</h3>
                  <button class="favorite-btn">❤️</button>
                </div>
                <div class="route-info">
                  <span class="info-item">{{ route.days }}天</span>
                  <span class="info-item">{{ route.experienceCount }}个非遗体验点</span>
                  <span class="info-item">{{ route.difficulty }}</span>
                </div>
                <p class="route-description">{{ route.description }}</p>
                <div class="route-footer">
                  <span class="price">¥{{ route.price }}/人起</span>
                  <button class="btn btn-primary" @click="viewRouteDetail(route)">查看详情</button>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="no-results">
            <p>没有找到相关路线，请尝试其他关键词</p>
          </div>
        </div>

        <!-- 列表模式 -->
        <div v-else class="route-list">
          <div class="route-card" v-for="route in routes" :key="route.id">
            <img :src="route.image" :alt="route.name" />
            <div class="route-content">
              <div class="route-header">
                <h3>{{ route.name }}</h3>
                <button class="favorite-btn">❤️</button>
              </div>
              <div class="route-info">
                <span class="info-item">{{ route.days }}天</span>
                <span class="info-item">{{ route.experienceCount }}个非遗体验点</span>
                <span class="info-item">{{ route.difficulty }}</span>
              </div>
              <p class="route-description">{{ route.description }}</p>
              <div class="route-footer">
                <span class="price">¥{{ route.price }}/人起</span>
                <button class="btn btn-primary" @click="viewRouteDetail(route)">查看详情</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { tourAPI } from '@/api/tours'
import backgroundImage from '@/assets/beijing.png'

const router = useRouter()
const showBackToTop = ref(false)
const searchKeyword = ref('')
const showSearchResults = ref(false)
const routes = ref([])
const loading = ref(false)
const error = ref(null)
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

// 从后端获取路线数据
const fetchRoutes = async () => {
  loading.value = true
  error.value = null
  try {
    const response = await tourAPI.getTourList()
    const getImageUrl = (imagePath) => {
      if (!imagePath) return '/image/default-tour.jpeg'
      if (imagePath.startsWith('http')) return imagePath
      return apiBaseUrl + imagePath
    }
    routes.value = response.results.map(tour => ({
      id: tour.id,
      name: tour.name,
      image: getImageUrl(tour.image),
      days: parseInt(tour.duration) || 1,
      experienceCount: tour.experience_points || 0,
      difficulty: '中等',
      description: tour.description,
      price: parseFloat(tour.price) || 0
    }))
  } catch (err) {
    console.error('获取路线数据失败:', err)
    error.value = '加载路线数据失败，请稍后重试'
  } finally {
    loading.value = false
  }
}

const searchRoutes = () => {
  showSearchResults.value = true
}

const clearSearch = () => {
  searchKeyword.value = ''
  showSearchResults.value = false
}

const filteredRoutes = computed(() => {
  if (!searchKeyword.value) return []
  const keyword = searchKeyword.value.toLowerCase()
  return routes.value.filter(route => {
    return route.name.toLowerCase().includes(keyword) ||
           route.description.toLowerCase().includes(keyword) ||
           route.difficulty.toLowerCase().includes(keyword)
  })
})

const viewRouteDetail = (route) => {
  // 跳转到统一的旅游详情页，传递路线ID
  router.push(`/tour-detail/${route.id}`)
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  fetchRoutes()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Smart Tour Container */
.smart-tour {
  position: relative;
  min-height: 100vh;
}

.smart-tour::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: var(--bg-image);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.3;
  z-index: -1;
  animation: slideInFromLeft 1.5s ease-out;
}

@keyframes slideInFromLeft {
  0% {
    transform: translateX(-100%);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 0.3;
  }
}

/* Page Header */
.page-header {
  background-color: var(--primary-color);
  color: var(--white);
  padding: 64px 0;
  text-align: center;
}

.page-header h1 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--white);
}

.page-header p {
  font-size: 18px;
  margin-bottom: 0;
}

/* Search Section */
.search-section {
  background-color: rgba(255, 255, 255, 0.95);
  padding: 32px 0;
  margin-top: -20px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  position: relative;
  z-index: 10;
}

.search-box {
  display: flex;
  max-width: 600px;
  margin: 0 auto 24px;
  border-radius: 40px;
  overflow: hidden;
  box-shadow: var(--shadow);
}

.search-input {
  flex: 1;
  padding: 16px 24px;
  border: none;
  outline: none;
  font-size: 16px;
}

.search-btn {
  background-color: var(--primary-color);
  color: var(--white);
  border: none;
  padding: 0 24px;
  cursor: pointer;
  transition: var(--transition);
}

.search-btn:hover {
  background-color: var(--primary-dark);
}

.clear-btn {
  background-color: var(--text-light);
  color: var(--text-dark);
  border: none;
  padding: 0 16px;
  cursor: pointer;
  transition: var(--transition);
  border-radius: 0 40px 40px 0;
}

.clear-btn:hover {
  background-color: var(--text-medium);
  color: var(--white);
}

/* Loading & Error States */
.loading-state,
.error-state {
  text-align: center;
  padding: 48px 24px;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
}

.loading-state p,
.error-state p {
  font-size: 16px;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.error-state p {
  color: var(--orange);
}

/* Search Results */
.search-results {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 32px;
  box-shadow: var(--shadow);
}

.search-results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.search-results-header h2 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 0;
  color: var(--text-dark);
}

.search-results-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.no-results {
  text-align: center;
  padding: 48px 24px;
  color: var(--text-medium);
}

.no-results p {
  margin-bottom: 0;
  font-size: 16px;
}


/* Content Section */
.content-section {
  padding: 48px 0;
}



/* Route List */
.route-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.route-card {
  display: flex;
  gap: 24px;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.route-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.route-card img {
  width: 300px;
  height: 200px;
  object-fit: cover;
  flex-shrink: 0;
}

.route-content {
  flex: 1;
  padding: 24px;
}

.route-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.route-header h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 0;
}

.favorite-btn {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  transition: var(--transition);
}

.favorite-btn:hover {
  transform: scale(1.2);
}

.route-info {
  display: flex;
  gap: 24px;
  margin-bottom: 16px;
  font-size: 14px;
  color: var(--text-medium);
}

.route-description {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 24px;
  line-height: 1.5;
}

.route-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price {
  font-size: 18px;
  font-weight: 600;
  color: var(--orange);
}



/* Responsive */
@media (max-width: 768px) {
  .page-header {
    padding: 48px 0;
  }
  
  .page-header h1 {
    font-size: 28px;
  }
  
  .route-card {
    flex-direction: column;
  }
  
  .route-card img {
    width: 100%;
    height: 200px;
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