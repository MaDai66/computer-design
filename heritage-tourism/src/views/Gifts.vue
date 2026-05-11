<template>
  <div class="gifts">
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

    <!-- 商品网格 -->
    <section class="products-section">
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

const router = useRouter()
const showBackToTop = ref(false)
const activeCategory = ref('非遗手作')

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

// 切换分类
const switchCategory = (category) => {
  activeCategory.value = category
}

// 过滤后的商品
const filteredProducts = computed(() => {
  if (activeCategory.value === '助农专区') {
    return products.filter(product => product.assist)
  }
  return products.filter(product => product.category === activeCategory.value)
})

// 跳转到商品详情页面
const viewProductDetail = (product) => {
  // 根据商品名称跳转到对应的详情页面
  if (product.name.includes('人参')) {
    router.push('/ginseng-product-detail')
  } else if (product.name.includes('玉米')) {
    router.push('/corn-product-detail')
  } else if (product.name.includes('蜂蜜')) {
    router.push('/honey-product-detail')
  } else if (product.name.includes('泡菜')) {
    router.push('/kimchi-product-detail')

  } else if (product.name.includes('打糕')) {
    router.push('/korean-rice-cake-product-detail')
  } else if (product.name.includes('有机鱼')) {
    router.push('/chagan-lake-fish-product-detail')
  } else if (product.name.includes('咸鸭蛋')) {
    router.push('/songhua-lake-egg-product-detail')
  } else if (product.name.includes('文创礼盒')) {
    router.push('/cultural-gift-box-product-detail')
  } else if (product.name.includes('冬捕纪念套装')) {
    router.push('/winter-fishing-souvenir-product-detail')
  } else if (product.name.includes('风光摄影集')) {
    router.push('/scenery-photography-product-detail')
  } else {
    // 默认跳转到通用商品详情页面
    router.push('/product-detail')
  }
}

// 跳转到商品详情页面（从预订按钮）
const bookProduct = (product) => {
  viewProductDetail(product)
}

const products = [
  {
    id: 1,
    name: '满族剪纸艺术套装',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20art%20traditional%20craft%20Jilin&image_size=portrait_4_3',
    price: 128,
    originalPrice: 168,
    discount: 24,
    sales: 1280,
    assist: false,
    category: '非遗手作'
  },
  {
    id: 2,
    name: '长白山野生人参',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbai%20Mountain%20wild%20ginseng%20Jilin%20natural%20herb%20traditional%20medicine&image_size=landscape_16_9',
    price: 298,
    originalPrice: 398,
    discount: 25,
    sales: 890,
    assist: true,
    category: '地道农产'
  },
  {
    id: 3,
    name: '朝鲜族传统打糕',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20traditional%20rice%20cake%20rice%20dough&image_size=landscape_16_9',
    price: 45,
    originalPrice: null,
    discount: null,
    sales: 2350,
    assist: true,
    category: '地道农产'
  },
  {
    id: 4,
    name: '查干湖有机鱼',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20organic%20fish%20fresh%20water&image_size=landscape_16_9',
    price: 168,
    originalPrice: 198,
    discount: 15,
    sales: 1560,
    assist: true,
    category: '地道农产'
  },
  {
    id: 5,
    name: '松花湖咸鸭蛋',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Salted%20duck%20eggs%20traditional%20Chinese%20food&image_size=landscape_16_9',
    price: 68,
    originalPrice: 88,
    discount: 23,
    sales: 1890,
    assist: true,
    category: '地道农产'
  },
  {
    id: 6,
    name: '吉林玉米糁',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20organic%20corn%20agricultural%20products&image_size=landscape_16_9',
    price: 39.9,
    originalPrice: null,
    discount: null,
    sales: 3200,
    assist: true,
    category: '地道农产'
  },
  {
    id: 7,
    name: '长白山蜂蜜',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbai%20Mountain%20natural%20honey%20Jilin%20agricultural%20product&image_size=landscape_16_9',
    price: 88,
    originalPrice: 118,
    discount: 25,
    sales: 2100,
    assist: true,
    category: '地道农产'
  },
  {
    id: 8,
    name: '朝鲜族泡菜',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20traditional%20kimchi%20Jilin%20fermented%20food&image_size=landscape_16_9',
    price: 58,
    originalPrice: 68,
    discount: 15,
    sales: 1950,
    assist: true,
    category: '地道农产'
  },
  {
    id: 9,
    name: '吉林长白山旅游文创礼盒',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20cultural%20creative%20gift%20box%20Changbai%20Mountain&image_size=landscape_16_9',
    price: 268,
    originalPrice: 328,
    discount: 18,
    sales: 780,
    assist: false,
    category: '文创礼盒'
  },

  {
    id: 11,
    name: '查干湖冬捕纪念套装',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20souvenir%20set%20with%20traditional%20fishing%20tools%20and%20cultural%20elements&image_size=landscape_16_9',
    price: 198,
    originalPrice: 258,
    discount: 23,
    sales: 620,
    assist: true,
    category: '文创礼盒'
  },
  {
    id: 12,
    name: '松花湖风光摄影集',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Songhua%20Lake%20landscape%20photography%20album&image_size=landscape_16_9',
    price: 128,
    originalPrice: 168,
    discount: 24,
    sales: 450,
    assist: false,
    category: '文创礼盒'
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
  background-color: var(--bg-color);
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