<template>
  <div class="smart-tour">
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
        <!-- 搜索结果 -->
        <div v-if="showSearchResults" class="search-results">
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

const router = useRouter()
const showBackToTop = ref(false)
const searchKeyword = ref('')
const showSearchResults = ref(false)

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
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
  return routes.filter(route => {
    return route.name.toLowerCase().includes(keyword) ||
           route.description.toLowerCase().includes(keyword) ||
           route.difficulty.toLowerCase().includes(keyword)
  })
})

const viewRouteDetail = (route) => {
  // 根据路线名称跳转到对应的详情页面
  if (route.name.includes('朝鲜族')) {
    router.push('/korean-village-tour-detail')
  } else if (route.name.includes('查干湖')) {
    router.push('/chagan-lake-tour-detail')
  } else if (route.name.includes('松花湖')) {
    router.push('/songhua-lake-tour-detail')
  } else {
    // 其他路线跳转到通用的路线详情页
    router.push('/tour-route-detail')
  }
}

const routes = [
  {
    id: 1,
    name: '长白山满族寻根2日游',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbai%20Mountain%20Manchu%20cultural%20tour&image_size=landscape_16_9',
    days: 2,
    experienceCount: 3,
    difficulty: '中等',
    description: '探访满族发源地，体验传统手工艺，感受长白山自然美景。',
    price: 688
  },
  {
    id: 2,
    name: '朝鲜族民俗村1日游',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20ethnic%20village%20cultural%20tour%20in%20Jilin&image_size=landscape_16_9',
    days: 1,
    experienceCount: 4,
    difficulty: '轻松',
    description: '感受朝鲜族传统文化，品尝特色美食，体验传统手工艺。',
    price: 298
  },
  {
    id: 3,
    name: '查干湖冬捕3日游',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20tour&image_size=landscape_16_9',
    days: 3,
    experienceCount: 2,
    difficulty: '中等',
    description: '体验千年冬捕文化，感受北国风光，品尝新鲜湖鱼。',
    price: 988
  },
  {
    id: 4,
    name: '松花湖生态文化2日游',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Songhua%20Lake%20ecological%20tour&image_size=landscape_16_9',
    days: 2,
    experienceCount: 3,
    difficulty: '轻松',
    description: '游览松花湖美景，体验传统渔业文化，参与生态保护活动。',
    price: 588
  }
]

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
  background-color: var(--white);
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