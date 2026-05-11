<template>
  <div class="product-detail">


    <div class="container">
      <!-- 加载状态 -->
      <div v-if="loading" class="loading-container">
        <div class="loading-spinner"></div>
        <p>加载商品信息中...</p>
      </div>
      
      <!-- 错误状态 -->
      <div v-else-if="error" class="error-container">
        <p>{{ error }}</p>
        <button class="btn btn-primary" @click="loadProductDetail">重试</button>
      </div>
      
      <!-- 商品主信息 -->
      <section v-else class="product-main">
        <div class="product-images">
          <div class="main-image">
            <img :src="product.image || 'https://via.placeholder.com/500'" :alt="product.name" />
          </div>
          <div class="thumbnails">
            <img :src="product.image || 'https://via.placeholder.com/100'" :alt="product.name" />
            <img :src="product.image || 'https://via.placeholder.com/100'" :alt="product.name" />
            <img :src="product.image || 'https://via.placeholder.com/100'" :alt="product.name" />
          </div>
        </div>
        <div class="product-info">
          <h1>{{ product.name }}</h1>
          <div class="product-tags">
            <span class="tag tag-orange">文创产品</span>
            <span class="tag tag-blue">满减</span>
          </div>
          <div class="product-price">
            <span class="current-price">¥{{ currentPrice }}</span>
            <span class="original-price">¥{{ Math.round(currentPrice * 1.3) }}</span>
            <span class="discount">{{ Math.round((currentPrice / (currentPrice * 1.3)) * 100) / 10 }}折</span>
          </div>
          <div class="product-stats">
            <span class="sales">销量：1280件</span>
            <span class="stock">库存：{{ product.stock }}件</span>
          </div>
          <div class="product-description">
            <h3>商品描述</h3>
            <p>{{ product.description }}</p>
          </div>
          <div class="product-specs">
              <h3>规格选择</h3>
              <div class="spec-options">
                <div class="spec-item">
                  <span class="spec-label">套装类型</span>
                  <div class="spec-values">
                    <button class="spec-value" :class="{ active: selectedSpec.type === 'basic' }" @click="selectSpec('type', 'basic')">基础版</button>
                    <button class="spec-value" :class="{ active: selectedSpec.type === 'premium' }" @click="selectSpec('type', 'premium')">高级版</button>
                  </div>
                </div>
                <div class="spec-item">
                  <span class="spec-label">图案主题</span>
                  <div class="spec-values">
                    <button class="spec-value" :class="{ active: selectedSpec.theme === 'lucky' }" @click="selectSpec('theme', 'lucky')">吉祥如意</button>
                    <button class="spec-value" :class="{ active: selectedSpec.theme === 'manchu' }" @click="selectSpec('theme', 'manchu')">满族风情</button>
                    <button class="spec-value" :class="{ active: selectedSpec.theme === 'seasonal' }" @click="selectSpec('theme', 'seasonal')">四季花卉</button>
                  </div>
                </div>
              </div>
            </div>
          <div class="product-quantity">
                <span class="quantity-label">数量</span>
                <div class="quantity-control">
                  <button class="quantity-btn minus" @click="decreaseQuantity">-</button>
                  <input type="number" class="quantity-input" v-model="quantity" min="1" />
                  <button class="quantity-btn plus" @click="increaseQuantity">+</button>
                </div>
              </div>
              <div class="product-actions">
                <button class="btn btn-primary" @click="buyNow">预订</button>
              </div>
        </div>
      </section>

      <!-- 规格参数 -->
      <section v-if="!loading && !error" class="product-specs">
        <h2>规格参数</h2>
        <div class="specs-table">
          <table>
            <tbody>
              <tr>
                <td class="spec-name">品牌</td>
                <td class="spec-value">吉韵遗风</td>
              </tr>
              <tr>
                <td class="spec-name">产地</td>
                <td class="spec-value">{{ product.origin || '吉林省' }}</td>
              </tr>
              <tr>
                <td class="spec-name">材质</td>
                <td class="spec-value">特种剪纸纸、优质剪刀、刻板</td>
              </tr>
              <tr>
                <td class="spec-name">包装</td>
                <td class="spec-value">精美礼盒包装</td>
              </tr>
              <tr>
                <td class="spec-name">重量</td>
                <td class="spec-value">约500g</td>
              </tr>
              <tr>
                <td class="spec-name">尺寸</td>
                <td class="spec-value">30cm × 20cm × 5cm</td>
              </tr>
              <tr>
                <td class="spec-name">适用人群</td>
                <td class="spec-value">手工艺爱好者、文化收藏者、礼品赠送</td>
              </tr>
              <tr>
                <td class="spec-name">保质期</td>
                <td class="spec-value">12个月</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 非遗溯源 -->
      <section v-if="!loading && !error" class="heritage-origin">
        <h2>非遗溯源</h2>
        <div class="origin-content">
          <div class="inheritor-info">
            <h3>传承人信息</h3>
            <div class="inheritor-card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Elderly%20Chinese%20woman%20paper%20cutting%20artist&image_size=portrait_4_3" alt="王阿姨" />
              <div class="inheritor-details">
                <h4>王淑兰 师傅</h4>
                <p class="inheritor-title">满族剪纸技艺传承人</p>
                <p class="inheritor-bio">王师傅从事满族剪纸艺术已有40余年，是国家级非物质文化遗产传承人。她的作品多次在国内外展览中获奖，代表作品包括《满族风情》、《吉祥如意》等系列。</p>
              </div>
            </div>
          </div>
          <div class="craft-process">
            <h3>制作工艺</h3>
            <div class="process-steps">
              <div class="process-step">
                <div class="step-number">1</div>
                <div class="step-content">
                  <h4>选材</h4>
                  <p>选用优质特种剪纸纸，确保纸张韧性好、色彩鲜艳、不易褪色。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">2</div>
                <div class="step-content">
                  <h4>设计</h4>
                  <p>根据满族传统图案和现代审美，设计出具有满族特色的剪纸图案。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">3</div>
                <div class="step-content">
                  <h4>刻板</h4>
                  <p>使用传统工艺制作刻板，确保图案清晰、线条流畅。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">4</div>
                <div class="step-content">
                  <h4>剪纸</h4>
                  <p>由经验丰富的剪纸艺人手工剪制，确保每一件作品都精美绝伦。</p>
                </div>
              </div>
              <div class="process-step">
                <div class="step-number">5</div>
                <div class="step-content">
                  <h4>装裱</h4>
                  <p>对完成的剪纸作品进行精心装裱，便于收藏和展示。</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 用户评价 -->
      <section v-if="!loading && !error" class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-list">
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@文化爱好者</span>
                  <span class="review-date">2026-04-10</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>这套剪纸工具非常好，材料质量上乘，教程详细易懂。我按照教程做了几个作品，非常有成就感。包装也很精美，是送礼的好选择。</p>
              <div class="review-images">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20made%20paper%20cutting%20art&image_size=portrait_4_3" alt="用户作品" />
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Paper%20cutting%20tools%20set&image_size=portrait_4_3" alt="工具展示" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@手工艺人</span>
                  <span class="review-date">2026-04-08</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>作为一名手工艺人，我对这套剪纸套装的质量非常满意。纸张的韧性很好，剪刀锋利，图案设计精美。最重要的是，它传承了满族的传统文化，非常有意义。</p>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@礼品选购</span>
                  <span class="review-date">2026-04-05</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>买给外国朋友的礼物，他们非常喜欢！包装精美，附带的介绍资料也很详细，让外国朋友了解了中国的传统文化。剪纸的质量也很好，非常满意。</p>
            </div>
          </div>
        </div>
      </section>


    </div>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import orderAPI from '../api/orders'
import { productAPI } from '../api/products'

const router = useRouter()
const route = useRoute()

const showBackToTop = ref(false)
const quantity = ref(1)
const selectedSpec = ref({
  type: 'basic',
  theme: 'lucky'
})
const loading = ref(false)
const error = ref('')
const product = ref({
  id: '',
  name: '',
  description: '',
  price: 0,
  stock: 0,
  origin: '',
  image: ''
})

// 获取当前价格
const currentPrice = computed(() => {
  return product.value.price || 128
})

// 增加数量
const increaseQuantity = () => {
  quantity.value++
}

// 减少数量
const decreaseQuantity = () => {
  if (quantity.value > 1) {
    quantity.value--
  }
}

// 选择规格
const selectSpec = (key, value) => {
  selectedSpec.value[key] = value
}

// 加载商品详情
const loadProductDetail = async () => {
  try {
    loading.value = true
    error.value = ''
    
    const productId = route.params.id
    if (!productId) {
      throw new Error('商品ID不存在')
    }
    
    const response = await productAPI.getProductDetail(productId)
    product.value = response
    console.log('商品详情加载成功:', product.value)
  } catch (err) {
    console.error('加载商品详情失败:', err)
    error.value = err.message || '加载商品信息失败，请稍后重试'
  } finally {
    loading.value = false
  }
}

// 加入购物车
const addToCart = () => {
  // 这里可以实现加入购物车的逻辑
  alert('已加入购物车')
}

// 立即购买
const buyNow = async () => {
  try {
    // 检查用户是否登录
    const user = JSON.parse(localStorage.getItem('user'))
    if (!user) {
      alert('请先登录再进行预订')
      router.push('/login')
      return
    }
    
    // 生成订单ID
    const orderId = 'ORD' + Date.now()
    
    // 获取规格名称
    const specType = selectedSpec.value.type === 'basic' ? '基础版' : '高级版'
    const specTheme = {
      lucky: '吉祥如意',
      manchu: '满族风情',
      seasonal: '四季花卉'
    }[selectedSpec.value.theme]
    
    // 创建订单对象
    const order = {
      id: orderId,
      type: 'product',
      item: product.value.name,
      price: currentPrice.value,
      totalPrice: currentPrice.value * quantity.value,
      quantity: quantity.value,
      spec: {
        type: specType,
        theme: specTheme
      },
      status: '待付款',
      createdAt: new Date().toISOString()
    }
    
    // 保存订单到后端数据库
    const orderData = {
      order_id: orderId,
      item: product.value.name,
      price: currentPrice.value,
      quantity: quantity.value,
      total_price: currentPrice.value * quantity.value,
      status: '待付款',
      spec: {
        type: specType,
        theme: specTheme
      }
    }
    
    // 调用API创建订单
    const response = await orderAPI.createOrder(orderData)
    console.log('订单创建成功:', response)
    
    // 保存订单到localStorage
    saveOrder(order)
    
    // 跳转到我的页面
    router.push('/profile')
  } catch (error) {
    console.error('创建订单失败:', error)
    // 显示更具体的错误信息
    if (error.response) {
      // 服务器返回错误
      if (error.response.status === 401) {
        alert('请先登录再进行预订')
        router.push('/login')
      } else {
        alert(`创建订单失败: ${error.response.data.error || error.response.statusText}`)
      }
    } else if (error.request) {
      // 请求发送成功但没有收到响应
      alert('创建订单失败: 服务器无响应，请检查网络连接')
    } else {
      // 其他错误
      alert(`创建订单失败: ${error.message}`)
    }
  }
}

// 保存订单到localStorage
const saveOrder = (order) => {
  const orders = JSON.parse(localStorage.getItem('orders') || '[]')
  orders.push(order)
  localStorage.setItem('orders', JSON.stringify(orders))
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

onMounted(() => {
  // 加载商品详情
  loadProductDetail()
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.product-detail {
  background-color: var(--bg-light);
  min-height: 100vh;
}



.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 48px 24px;
}

/* 加载状态 */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 500px;
  text-align: center;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 32px;
  box-shadow: var(--shadow);
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid var(--primary-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* 错误状态 */
.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 500px;
  text-align: center;
  color: var(--danger-color);
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 32px;
  box-shadow: var(--shadow);
}

.error-container p {
  margin-bottom: 20px;
  font-size: 16px;
}

section {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 32px;
  box-shadow: var(--shadow);
}

section h2 {
  font-size: 24px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--primary-color);
}

section h3 {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
  margin: 24px 0 16px;
}

/* 商品主信息 */
.product-main {
  display: flex;
  gap: 48px;
}

.product-images {
  flex: 0 0 500px;
}

.main-image {
  width: 100%;
  height: 500px;
  border-radius: var(--radius-md);
  overflow: hidden;
  margin-bottom: 16px;
}

.main-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.thumbnails {
  display: flex;
  gap: 12px;
}

.thumbnails img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: var(--transition);
  border: 2px solid transparent;
}

.thumbnails img:hover {
  border-color: var(--primary-color);
  transform: scale(1.05);
}

.product-info {
  flex: 1;
}

.product-info h1 {
  font-size: 28px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 16px;
}

.product-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}

.tag {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.tag-orange {
  background-color: var(--accent-orange-light);
  color: var(--accent-orange);
}

.tag-blue {
  background-color: var(--accent-blue-light);
  color: var(--accent-blue);
}

.product-price {
  display: flex;
  align-items: baseline;
  gap: 16px;
  margin-bottom: 16px;
}

.current-price {
  font-size: 32px;
  font-weight: 600;
  color: var(--accent-orange);
}

.original-price {
  font-size: 16px;
  color: var(--text-light);
  text-decoration: line-through;
}

.discount {
  font-size: 14px;
  color: var(--accent-orange);
  background-color: var(--accent-orange-light);
  padding: 2px 8px;
  border-radius: 12px;
}

.product-stats {
  display: flex;
  gap: 24px;
  margin-bottom: 24px;
  font-size: 14px;
  color: var(--text-medium);
}

.product-description {
  margin-bottom: 24px;
}

.product-description p {
  line-height: 1.5;
  color: var(--text-medium);
}

.product-specs {
  margin-bottom: 24px;
}

.spec-item {
  margin-bottom: 16px;
}

.spec-label {
  display: block;
  font-weight: 500;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.spec-values {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.spec-value {
  padding: 8px 16px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  background-color: var(--bg-light);
  cursor: pointer;
  transition: var(--transition);
}

.spec-value:hover {
  border-color: var(--primary-color);
}

.spec-value.active {
  border-color: var(--primary-color);
  background-color: var(--primary-light);
  color: var(--primary-color);
}

.product-quantity {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}

.quantity-label {
  font-weight: 500;
  color: var(--text-dark);
}

.quantity-control {
  display: flex;
  align-items: center;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.quantity-btn {
  width: 40px;
  height: 40px;
  border: none;
  background-color: var(--bg-light);
  cursor: pointer;
  font-size: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}

.quantity-btn:hover {
  background-color: var(--primary-light);
}

.quantity-input {
  width: 60px;
  height: 40px;
  border: none;
  text-align: center;
  font-size: 16px;
  outline: none;
}

.product-actions {
  display: flex;
  gap: 16px;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: var(--radius-md);
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
  flex: 1;
}

.btn-primary {
  background-color: var(--primary-color);
  color: var(--white);
}

.btn-primary:hover {
  background-color: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
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

/* 规格参数 */
.specs-table table {
  width: 100%;
  border-collapse: collapse;
}

.specs-table tr {
  border-bottom: 1px solid var(--border-color);
}

.specs-table td {
  padding: 12px;
}

.spec-name {
  width: 150px;
  font-weight: 500;
  color: var(--text-dark);
  background-color: var(--bg-light);
}

.spec-value {
  color: var(--text-medium);
}

/* 非遗溯源 */
.origin-content {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.inheritor-card {
  display: flex;
  gap: 24px;
  background-color: var(--bg-light);
  padding: 24px;
  border-radius: var(--radius-md);
}

.inheritor-card img {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: var(--radius-md);
  flex-shrink: 0;
}

.inheritor-details h4 {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
}

.inheritor-title {
  font-size: 14px;
  color: var(--primary-color);
  margin-bottom: 12px;
}

.inheritor-bio {
  line-height: 1.5;
  color: var(--text-medium);
}

.process-steps {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.process-step {
  display: flex;
  gap: 24px;
  background-color: var(--bg-light);
  padding: 20px;
  border-radius: var(--radius-md);
}

.step-number {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: var(--primary-color);
  color: var(--white);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
}

.step-content h4 {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-dark);
}

.step-content p {
  line-height: 1.5;
  color: var(--text-medium);
  margin: 0;
}

/* 用户评价 */
.reviews-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 32px;
  flex-wrap: wrap;
  gap: 24px;
}

.rating-overall {
  display: flex;
  align-items: baseline;
  gap: 16px;
  margin-bottom: 16px;
}

.rating-score {
  font-size: 32px;
  font-weight: 600;
  color: var(--accent-orange);
}

.rating-stars {
  font-size: 18px;
}

.rating-count {
  font-size: 14px;
  color: var(--text-medium);
}

.rating-details {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rating-item {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
}

.rating-item span:first-child {
  width: 40px;
  color: var(--text-medium);
}

.rating-bar {
  flex: 1;
  height: 8px;
  background-color: var(--bg-light);
  border-radius: 4px;
  overflow: hidden;
}

.rating-fill {
  height: 100%;
  background-color: var(--accent-orange);
  transition: width 0.3s ease;
}

.rating-item span:last-child {
  width: 40px;
  color: var(--text-medium);
  text-align: right;
}

.review-filter {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 8px 16px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  background-color: var(--white);
  cursor: pointer;
  transition: var(--transition);
  font-size: 14px;
}

.filter-btn:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
}

.filter-btn.active {
  background-color: var(--primary-color);
  color: var(--white);
  border-color: var(--primary-color);
}

.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-bottom: 32px;
}

.review-item {
  padding: 24px;
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-info img {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.user-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.user-name {
  font-weight: 500;
  color: var(--text-dark);
}

.review-date {
  font-size: 12px;
  color: var(--text-light);
}

.review-rating {
  font-size: 14px;
}

.review-content p {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.review-images {
  display: flex;
  gap: 12px;
}

.review-images img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: var(--radius-sm);
}

.review-pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
}

.page-btn {
  padding: 8px 16px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  background-color: var(--white);
  cursor: pointer;
  transition: var(--transition);
  font-size: 14px;
}

.page-btn:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
}

.page-btn.active {
  background-color: var(--primary-color);
  color: var(--white);
  border-color: var(--primary-color);
}

/* 关联推荐 */
.related-recommendations h3 {
  margin-top: 32px;
  margin-bottom: 16px;
}

.recommend-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 24px;
}

.recommend-card {
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: var(--transition);
}

.recommend-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.recommend-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.recommend-card h4 {
  padding: 16px;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
}

.recommend-card p {
  padding: 0 16px 16px;
  font-weight: 600;
  color: var(--accent-orange);
  margin-bottom: 12px;
}

.recommend-card .btn {
  margin: 0 16px 16px;
  width: calc(100% - 32px);
  flex: none;
}

/* 回到顶部按钮 */
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

/* 响应式 */
@media (max-width: 768px) {
  .container {
    padding: 24px 16px;
  }
  
  .product-main {
    flex-direction: column;
    gap: 24px;
  }
  
  .product-images {
    flex: none;
    width: 100%;
  }
  
  .main-image {
    height: 300px;
  }
  
  .product-info h1 {
    font-size: 24px;
  }
  
  .reviews-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .process-step {
    flex-direction: column;
    gap: 16px;
  }
  
  .step-number {
    align-self: flex-start;
  }
  
  section {
    padding: 20px;
  }
  
  .back-to-top {
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
}
</style>