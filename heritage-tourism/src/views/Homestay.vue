<template>
  <div class="homestay" :style="{ '--bg-image': `url(${backgroundImage})` }">
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1>吉林乡宿</h1>
        <p>体验乡村生活，感受自然之美</p>
      </div>
    </section>

    <!-- 筛选侧边栏和内容区 -->
    <section class="content-section">
      <div class="container">
        <div class="homestay-content">
          <!-- 筛选侧边栏 -->
          <div class="filter-sidebar">
            <h3>筛选条件</h3>
            
            <!-- 所在区域 -->
            <div class="filter-group">
              <h4>所在区域</h4>
              <div class="filter-options">
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.areas.changbai" />
                  <span>长白山</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.areas.songhua" />
                  <span>松花湖</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.areas.chagan" />
                  <span>查干湖</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.areas.korean" />
                  <span>朝鲜族民俗村</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.areas.other" />
                  <span>其他</span>
                </label>
              </div>
            </div>
            
            <!-- 特色标签 -->
            <div class="filter-group">
              <h4>特色标签</h4>
              <div class="filter-options">
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.tags.hasHeritage" />
                  <span>非遗体验</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.tags.selfOperated" />
                  <span>农家自营</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.tags.hot" />
                  <span>热销</span>
                </label>
              </div>
            </div>
            
            <!-- 设施 -->
            <div class="filter-group">
              <h4>设施</h4>
              <div class="filter-options">
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.facilities.kang" />
                  <span>火炕</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.facilities.wifi" />
                  <span>WiFi</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.facilities.bathroom" />
                  <span>独立卫浴</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.facilities.parking" />
                  <span>停车场</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.facilities.restaurant" />
                  <span>餐厅</span>
                </label>
              </div>
            </div>
            
            <!-- 评分 -->
            <div class="filter-group">
              <h4>评分</h4>
              <div class="filter-options">
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.rating.fourPointFive" />
                  <span>4.5分以上</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.rating.four" />
                  <span>4分以上</span>
                </label>
                <label class="filter-option">
                  <input type="checkbox" v-model="filters.rating.threePointFive" />
                  <span>3.5分以上</span>
                </label>
              </div>
            </div>
            
            <div class="filter-buttons">
              <button class="btn btn-secondary reset-btn" @click="resetFilters">重置</button>
              <button class="btn btn-primary filter-btn" @click="applyFilters">应用筛选</button>
            </div>
          </div>
          
          <!-- 农家院列表 -->
          <div class="homestay-list">
            <div class="homestay-card" v-for="homestay in homestays" :key="homestay.id" @click="viewHomestayDetail(homestay.id)" style="cursor: pointer;">
              <img :src="homestay.image" :alt="homestay.name" />
              <div class="homestay-info">
                <div class="homestay-header">
                  <h3>{{ homestay.name }}</h3>
                  <button class="favorite-btn" @click.stop>❤️</button>
                </div>
                <div class="homestay-meta">
                  <span class="rating">{{ homestay.rating }}⭐</span>
                  <span class="location">{{ homestay.location }}</span>
                  <span class="distance">{{ homestay.distance }}km</span>
                </div>
                <div class="homestay-tags">
                  <span class="tag tag-red" v-if="homestay.hasHeritage">非遗体验</span>
                  <span class="tag tag-green" v-if="homestay.selfOperated">农家自营</span>
                  <span class="tag tag-orange" v-if="homestay.hot">热销</span>
                </div>
                <p class="homestay-description">{{ homestay.description }}</p>
                <div class="homestay-footer">
                  <div class="price-info">
                    <span class="price">¥{{ homestay.price }}/晚</span>
                    <span class="price-unit">起</span>
                  </div>
                  <button class="btn btn-primary" @click.stop="viewHomestayDetail(homestay.id)">查看详情</button>
                </div>
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
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import backgroundImage from '@/assets/beijing.png'

const router = useRouter()
const showBackToTop = ref(false)
const loading = ref(false)
const error = ref('')
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

// 筛选条件
const filters = ref({
  areas: {
    changbai: false,
    songhua: false,
    chagan: false,
    korean: false,
    other: false
  },
  tags: {
    hasHeritage: false,
    selfOperated: false,
    hot: false
  },
  facilities: {
    kang: false,
    wifi: false,
    bathroom: false,
    parking: false,
    restaurant: false
  },
  rating: {
    fourPointFive: false,
    four: false,
    threePointFive: false
  }
})

// 原始农家院数据
const originalHomestays = ref([
  {
    id: 1,
    name: '长白山脚下农家院',
    image: '/image/Homestay/372127531b22cf3b11b561b712ab9aae.jpeg',
    rating: 4.8,
    location: '长白山景区附近',
    distance: 5,
    hasHeritage: true,
    selfOperated: true,
    hot: true,
    description: '位于长白山脚下，环境优美，提供满族剪纸体验，正宗农家菜。',
    price: 280,
    area: 'changbai',
    experiences: ['paperCutting'],
    facilities: ['kang', 'wifi', 'bathroom', 'parking', 'restaurant']
  },
  {
    id: 2,
    name: '松花湖生态农家院',
    image: '/image/Homestay/5e722f3174856920f5a95763187cfabe.jpeg',
    rating: 4.6,
    location: '松花湖景区',
    distance: 10,
    hasHeritage: true,
    selfOperated: true,
    hot: false,
    description: '松花湖边的生态农家院，提供传统渔业体验，湖景房。',
    price: 320,
    area: 'songhua',
    experiences: ['fishing'],
    facilities: ['wifi', 'bathroom', 'parking', 'restaurant']
  },
  {
    id: 3,
    name: '朝鲜族民俗村农家院',
    image: '/image/Homestay/fb02a59c68ee0050700468e4f137cc0d.jpeg',
    rating: 4.9,
    location: '朝鲜族民俗村',
    distance: 15,
    hasHeritage: true,
    selfOperated: true,
    hot: true,
    description: '朝鲜族特色农家院，提供打糕制作、朝鲜服装体验，正宗朝鲜美食。',
    price: 260,
    area: 'korean',
    experiences: ['riceCake'],
    facilities: ['kang', 'wifi', 'bathroom', 'parking', 'restaurant']
  },
  {
    id: 4,
    name: '查干湖冬捕农家院',
    image: '/image/Homestay/87d003eb75a414662e86f3c2231ba9b4.jpeg',
    rating: 4.7,
    location: '查干湖景区',
    distance: 20,
    hasHeritage: true,
    selfOperated: true,
    hot: true,
    description: '查干湖边的农家院，冬季提供冬捕体验，特色鱼宴。',
    price: 300,
    area: 'chagan',
    experiences: ['winterFishing'],
    facilities: ['kang', 'wifi', 'bathroom', 'parking', 'restaurant']
  }
])

// 过滤后的农家院数据
const homestays = ref([...originalHomestays.value])

// 获取图片URL
const getImageUrl = (imagePath) => {
  if (!imagePath) return '/image/Homestay/default.jpg'
  if (imagePath.startsWith('http')) return imagePath
  if (imagePath.startsWith('/media')) return apiBaseUrl + imagePath
  if (imagePath.startsWith('/image')) return imagePath
  return apiBaseUrl + imagePath
}

// 获取农家院数据
const fetchHomestays = async () => {
  loading.value = true
  error.value = ''
  try {
    const response = await axios.get(`${apiBaseUrl}/api/homestay/`)
    const data = response.data.results || response.data || []
    
    if (data.length > 0) {
      originalHomestays.value = data.map(item => ({
        id: item.id,
        name: item.name,
        image: getImageUrl(item.image),
        rating: parseFloat(item.rating) || 0,
        location: item.location || '',
        distance: item.distance || 0,
        hasHeritage: item.has_heritage || false,
        selfOperated: item.self_operated || false,
        hot: item.hot || false,
        description: item.description || '',
        price: parseFloat(item.price) || 0,
        area: item.area || 'other',
        experiences: item.experiences || [],
        facilities: item.facilities || []
      }))
      homestays.value = [...originalHomestays.value]
    }
  } catch (err) {
    console.error('获取农家院数据失败:', err)
    error.value = '获取农家院数据失败，使用本地数据'
  } finally {
    loading.value = false
  }
}

// 应用筛选
const applyFilters = () => {
  let filtered = [...originalHomestays.value]
  
  // 按区域筛选
  const selectedAreas = Object.entries(filters.value.areas)
    .filter(([_, value]) => value)
    .map(([key]) => key)
  
  if (selectedAreas.length > 0) {
    filtered = filtered.filter(homestay => selectedAreas.includes(homestay.area))
  }
  
  // 按特色标签筛选
  const selectedTags = Object.entries(filters.value.tags)
    .filter(([_, value]) => value)
    .map(([key]) => key)
  
  if (selectedTags.length > 0) {
    filtered = filtered.filter(homestay => {
      return selectedTags.every(tag => {
        if (tag === 'hasHeritage') return homestay.hasHeritage
        if (tag === 'selfOperated') return homestay.selfOperated
        if (tag === 'hot') return homestay.hot
        return true
      })
    })
  }
  
  // 按设施筛选
  const selectedFacilities = Object.entries(filters.value.facilities)
    .filter(([_, value]) => value)
    .map(([key]) => key)
  
  if (selectedFacilities.length > 0) {
    filtered = filtered.filter(homestay => 
      selectedFacilities.every(facility => homestay.facilities.includes(facility))
    )
  }
  
  // 按评分筛选
  const selectedRatings = Object.entries(filters.value.rating)
    .filter(([_, value]) => value)
    .map(([key]) => key)
  
  if (selectedRatings.length > 0) {
    filtered = filtered.filter(homestay => {
      // 如果选择了多个评分选项，使用最高的评分标准
      if (selectedRatings.includes('fourPointFive')) {
        return homestay.rating >= 4.5
      } else if (selectedRatings.includes('four')) {
        return homestay.rating >= 4.0
      } else if (selectedRatings.includes('threePointFive')) {
        return homestay.rating >= 3.5
      }
      return true
    })
  }
  
  // 确保至少显示一个农家院，如果筛选结果为空，显示所有农家院
  if (filtered.length === 0) {
    let fallbackFiltered = [...originalHomestays.value]
    
    if (selectedAreas.length > 0) {
      fallbackFiltered = fallbackFiltered.filter(homestay => selectedAreas.includes(homestay.area))
    }
    
    if (fallbackFiltered.length === 0 && selectedTags.length > 0) {
      fallbackFiltered = originalHomestays.value.filter(homestay => {
        return selectedTags.some(tag => {
          if (tag === 'hasHeritage') return homestay.hasHeritage
          if (tag === 'selfOperated') return homestay.selfOperated
          if (tag === 'hot') return homestay.hot
          return true
        })
      })
    }
    
    if (fallbackFiltered.length === 0 && selectedFacilities.length > 0) {
      fallbackFiltered = originalHomestays.value.filter(homestay => 
        selectedFacilities.every(facility => homestay.facilities.includes(facility))
      )
    }
    
    if (fallbackFiltered.length === 0 && selectedRatings.length > 0) {
      fallbackFiltered = originalHomestays.value.filter(homestay => {
        if (selectedRatings.includes('fourPointFive')) {
          return homestay.rating >= 4.5
        } else if (selectedRatings.includes('four')) {
          return homestay.rating >= 4.0
        } else if (selectedRatings.includes('threePointFive')) {
          return homestay.rating >= 3.5
        }
        return true
      })
    }
    
    if (fallbackFiltered.length === 0) {
      fallbackFiltered = [...originalHomestays.value]
    }
    
    filtered = fallbackFiltered
  }
  
  homestays.value = filtered
}

// 重置筛选
const resetFilters = () => {
  Object.keys(filters.value).forEach(group => {
    Object.keys(filters.value[group]).forEach(key => {
      filters.value[group][key] = false
    })
  })
  homestays.value = [...originalHomestays.value]
}

// 全选/全不选
const toggleAll = (group, value) => {
  Object.keys(filters.value[group]).forEach(key => {
    filters.value[group][key] = value
  })
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

// 查看农家院详情
const viewHomestayDetail = (homestayId) => {
  router.push(`/homestay-detail/${homestayId}`)
}

onMounted(() => {
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
  // 获取农家院数据
  fetchHomestays()
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Homestay Container */
.homestay {
  position: relative;
  min-height: 100vh;
}

.homestay::before {
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

/* Content Section */
.content-section {
  padding: 64px 0;
}

.homestay-content {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 32px;
}

/* Filter Sidebar */
.filter-sidebar {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow);
  position: sticky;
  top: 100px;
  height: fit-content;
}

.filter-sidebar h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 24px;
}

.filter-group {
  margin-bottom: 24px;
}

.filter-group h4 {
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 12px;
  color: var(--text-dark);
}

.filter-options {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.filter-option {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-size: 14px;
  color: var(--text-medium);
  transition: var(--transition);
}

.filter-option:hover {
  color: var(--primary-color);
}

.filter-option input[type="checkbox"] {
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.filter-buttons {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}

.filter-btn, .reset-btn {
  flex: 1;
}

.reset-btn {
  background-color: transparent;
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
}

.reset-btn:hover {
  background-color: var(--primary-color);
  color: var(--white);
}

/* Homestay List */
.homestay-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.homestay-card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 24px;
}

.homestay-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.homestay-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.homestay-info {
  padding: 24px;
}

.homestay-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}

.homestay-header h3 {
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

.homestay-meta {
  display: flex;
  gap: 16px;
  margin-bottom: 12px;
  font-size: 14px;
  color: var(--text-medium);
}

.homestay-tags {
  margin-bottom: 12px;
}

.homestay-description {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 24px;
  line-height: 1.5;
}

.homestay-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price-info {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.price {
  font-size: 20px;
  font-weight: 600;
  color: var(--orange);
}

.price-unit {
  font-size: 14px;
  color: var(--text-medium);
}

/* Responsive */
@media (max-width: 768px) {
  .page-header {
    padding: 48px 0;
  }
  
  .page-header h1 {
    font-size: 28px;
  }
  
  .content-section {
    padding: 48px 0;
  }
  
  .homestay-content {
    grid-template-columns: 1fr;
  }
  
  .filter-sidebar {
    position: static;
    margin-bottom: 24px;
  }
  
  .homestay-card {
    grid-template-columns: 1fr;
  }
  
  .homestay-card img {
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