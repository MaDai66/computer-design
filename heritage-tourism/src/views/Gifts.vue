<template>
  <div class="gifts" :style="{ '--bg-image': `url(${backgroundImage})` }">
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1>吉礼商城</h1>
        <p>非遗文创与特色农产品</p>
      </div>
    </section>

    <!-- 商品分类 -->
    <section class="category-section">
      <div class="container">
        <div class="category-tabs">
          <button class="category-tab" :class="{ active: activeCategory === '非遗手作' }" @click="switchCategory('非遗手作')">非遗手作</button>
          <button class="category-tab" :class="{ active: activeCategory === '地道农产' }" @click="switchCategory('地道农产')">地道农产</button>
          <button class="category-tab" :class="{ active: activeCategory === '文创礼盒' }" @click="switchCategory('文创礼盒')">文创礼盒</button>
          <button class="category-tab" :class="{ active: activeCategory === '助农专区' }" @click="switchCategory('助农专区')">助农专区</button>
        </div>
      </div>
    </section>

    <!-- 加载状态 -->
    <section v-if="loading" class="products-section">
      <div class="container">
        <div class="loading-state">
          <p>加载中...</p>
        </div>
      </div>
    </section>

    <!-- 错误状态 -->
    <section v-else-if="error" class="products-section">
      <div class="container">
        <div class="error-state">
          <p>{{ error }}</p>
          <button class="btn btn-secondary" @click="fetchProducts">重新加载</button>
        </div>
      </div>
    </section>

    <!-- 商品网格 -->
    <section v-else class="products-section">
      <div class="container">
        <div class="products-grid">
          <div class="product-card" v-for="product in filteredProducts" :key="product.id" @click="viewProductDetail(product)" style="cursor: pointer;">
            <div class="product-image">
              <img :src="product.image" :alt="product.name" />
              <span v-if="product.assist" class="assist-tag">爱心助农</span>
            </div>
            <div class="product-info">
              <h3>{{ product.name }}</h3>
              <div class="product-price">
                <span class="price">¥{{ product.price }}</span>
                <span v-if="product.originalPrice" class="original-price">¥{{ product.originalPrice }}</span>
              </div>
              <div class="product-footer">
                <span class="sales">销量 {{ product.sales }}</span>
                <button class="btn btn-primary add-to-cart" @click.stop="bookProduct(product)">预订</button>
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
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { productAPI } from '@/api/products'
import backgroundImage from '@/assets/beijing.png'

const router = useRouter()
const showBackToTop = ref(false)
const activeCategory = ref('非遗手作')
const products = ref([])
const loading = ref(false)
const error = ref('')
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

// 获取图片URL（处理相对路径）
const getImageUrl = (imagePath) => {
  if (!imagePath) return '/image/Gifts/default.jpg'
  if (imagePath.startsWith('http')) return imagePath
  if (imagePath.startsWith('/media')) return apiBaseUrl + imagePath
  if (imagePath.startsWith('/image')) return imagePath
  return apiBaseUrl + imagePath
}

// 获取产品列表
const fetchProducts = async () => {
  loading.value = true
  error.value = ''
  try {
    const response = await productAPI.getProductList()
    products.value = response.results || response || []
    // 处理图片路径和字段映射
    products.value = products.value.map(product => ({
      id: product.id,
      name: product.name,
      description: product.description,
      image: getImageUrl(product.image),
      price: parseFloat(product.price),
      originalPrice: product.original_price ? parseFloat(product.original_price) : null,
      discount: product.discount,
      sales: product.sales_count || 0,
      assist: (product.tags && product.tags.includes('助农')) || false,
      category: mapCategory(product.category),
      rating: product.rating,
      reviewCount: product.review_count,
      origin: product.origin,
      stock: product.stock
    }))
  } catch (err) {
    console.error('获取产品列表失败:', err)
    error.value = '获取产品列表失败，请稍后重试'
  } finally {
    loading.value = false
  }
}

// 分类映射函数
const mapCategory = (dbCategory) => {
  const categoryMap = {
    
    '生鲜水产': '地道农产',
    '新鲜果蔬': '地道农产',
    '文创礼品': '文创礼盒',
    '工艺品': '非遗手作'
  }
  return categoryMap[dbCategory] || dbCategory
}

// 切换分类
const switchCategory = (category) => {
  activeCategory.value = category
}

// 过滤后的商品
const filteredProducts = computed(() => {
  if (activeCategory.value === '助农专区') {
    return products.value.filter(product => product.assist)
  }
  return products.value.filter(product => product.category === activeCategory.value)
})

// 跳转到商品详情页面
const viewProductDetail = (product) => {
  const id = product.id
  if (product.name.includes('人参')) {
    router.push(`/ginseng-product-detail/${id}`)
  } else if (product.name.includes('玉米')) {
    router.push(`/corn-product-detail/${id}`)
  } else if (product.name.includes('蜂蜜')) {
    router.push(`/honey-product-detail/${id}`)
  } else if (product.name.includes('泡菜')) {
    router.push(`/kimchi-product-detail/${id}`)
  } else if (product.name.includes('打糕')) {
    router.push(`/korean-rice-cake-product-detail/${id}`)
  } else if (product.name.includes('有机鱼')) {
    router.push(`/chagan-lake-fish-product-detail/${id}`)
  } else if (product.name.includes('咸鸭蛋')) {
    router.push(`/songhua-lake-egg-product-detail/${id}`)
  } else if (product.name.includes('文创礼盒')) {
    router.push(`/cultural-gift-box-product-detail/${id}`)
  } else if (product.name.includes('冬捕纪念套装')) {
    router.push(`/winter-fishing-souvenir-product-detail/${id}`)
  } else if (product.name.includes('风光摄影集')) {
    router.push(`/scenery-photography-product-detail/${id}`)
  } else {
    router.push(`/product-detail/${id}`)
  }
}

// 跳转到商品详情页面（从预订按钮）
const bookProduct = (product) => {
  viewProductDetail(product)
}

onMounted(() => {
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
  // 获取产品列表
  fetchProducts()
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Gifts Container */
.gifts {
  position: relative;
  min-height: 100vh;
}

.gifts::before {
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

/* Loading & Error States */
.loading-state,
.error-state {
  text-align: center;
  padding: 64px 24px;
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

/* Category Section */
.category-section {
  background-color: var(--white);
  padding: 24px 0;
  border-bottom: 1px solid var(--border-color);
  position: sticky;
  top: 80px;
  z-index: 100;
}

.category-tabs {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  padding: 0 var(--spacing-lg);
}

.category-tab {
  padding: 12px 24px;
  border: none;
  background: none;
  font-size: 16px;
  font-weight: 500;
  color: var(--text-medium);
  cursor: pointer;
  transition: var(--transition);
  white-space: nowrap;
  position: relative;
}

.category-tab:hover {
  color: var(--primary-color);
}

.category-tab.active {
  color: var(--primary-color);
  font-weight: 600;
}

.category-tab.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 24px;
  right: 24px;
  height: 2px;
  background-color: var(--primary-color);
  border-radius: 1px;
}

/* Products Section */
.products-section {
  padding: 64px 0;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.product-card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.product-image {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: var(--transition);
}

.product-card:hover .product-image img {
  transform: scale(1.05);
}

.discount-tag {
  position: absolute;
  top: 12px;
  left: 12px;
  background-color: var(--red);
  color: var(--white);
  padding: 4px 8px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 600;
}

.assist-tag {
  position: absolute;
  top: 12px;
  right: 12px;
  background-color: var(--orange);
  color: var(--white);
  padding: 4px 8px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-weight: 600;
}

.product-info {
  padding: 16px;
}

.product-info h3 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.product-price {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin-bottom: 12px;
}

.price {
  font-size: 18px;
  font-weight: 600;
  color: var(--orange);
}

.original-price {
  font-size: 14px;
  color: var(--text-light);
  text-decoration: line-through;
}

.product-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sales {
  font-size: 12px;
  color: var(--text-light);
}

.add-to-cart {
  padding: 6px 12px;
  font-size: 14px;
  border-radius: 20px;
}

/* Responsive */
@media (max-width: 768px) {
  .page-header {
    padding: 48px 0;
  }
  
  .page-header h1 {
    font-size: 28px;
  }
  
  .category-section {
    top: 70px;
  }
  
  .category-tabs {
    padding: 0 var(--spacing-md);
  }
  
  .category-tab {
    padding: 8px 16px;
    font-size: 14px;
  }
  
  .products-section {
    padding: 48px 0;
  }
  
  .products-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
  }
  
  .product-image {
    height: 150px;
  }
  
  .product-info {
    padding: 12px;
  }
  
  .product-info h3 {
    font-size: 14px;
  }
  
  .price {
    font-size: 16px;
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