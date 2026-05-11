<template>
  <div class="product-detail">
    <!-- 商品信息 -->
    <section class="product-info-section">
      <div class="container">
        <div class="product-info">
          <div class="product-images">
            <div class="main-image">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Songhua%20Lake%20landscape%20photography%20album&image_size=landscape_16_9" alt="松花湖风光摄影集" />
            </div>
            <div class="thumbnails">
              <div class="thumbnail active">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Landscape%20photography%20album%20close%20up&image_size=square" alt="松花湖风光摄影集" />
              </div>
              <div class="thumbnail">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Professional%20photography%20album&image_size=square" alt="松花湖风光摄影集" />
              </div>
              <div class="thumbnail">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Scenic%20landscape%20photographs&image_size=square" alt="松花湖风光摄影集" />
              </div>
            </div>
          </div>
          <div class="product-details">
            <h1>松花湖风光摄影集</h1>
            <div class="product-rating">
              <span class="rating">4.9</span>
              <div class="stars">
                <span class="star active">★</span>
                <span class="star active">★</span>
                <span class="star active">★</span>
                <span class="star active">★</span>
                <span class="star active">★</span>
              </div>
              <span class="review-count">(45 评价)</span>
            </div>
            <div class="product-price">
              <span class="price">¥128</span>
              <span class="original-price">¥168</span>
              <span class="discount">24% OFF</span>
            </div>
            <div class="product-sales">
              <span>销量: 450</span>
            </div>
            <div class="product-description">
              <p>松花湖风光摄影集，收录了松花湖四季美景，由专业摄影师拍摄，是收藏和送礼的佳品。</p>
            </div>
            <div class="product-actions">
              <button class="btn btn-primary buy-now" @click="openPurchaseModal">立即购买</button>
              <button class="btn btn-secondary add-to-cart">加入购物车</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 商品详情 -->
    <section class="product-details-section">
      <div class="container">
        <div class="details-tabs">
          <button class="tab active">商品详情</button>
          <button class="tab">规格参数</button>
          <button class="tab">用户评价</button>
        </div>
        <div class="tab-content">
          <div class="product-description">
            <h2>商品详情</h2>
            <p>松花湖风光摄影集收录了松花湖四季的美丽景色，由专业摄影师精心拍摄，展现了松花湖的自然之美。</p>
            <h3>产品特点</h3>
            <ul>
              <li>收录松花湖四季美景</li>
              <li>由专业摄影师拍摄</li>
              <li>高质量印刷，精美装订</li>
              <li>收藏和送礼的佳品</li>
            </ul>
            <h3>摄影集内容</h3>
            <ul>
              <li>春季：松花湖苏醒</li>
              <li>夏季：湖光山色</li>
              <li>秋季：层林尽染</li>
              <li>冬季：冰雪世界</li>
            </ul>
            <h3>规格信息</h3>
            <p>尺寸：28cm × 21cm</p>
            <p>页数：80页</p>
            <p>装订：精装</p>
          </div>
        </div>
      </div>
    </section>


  </div>

  <!-- 购买模态框 -->
  <div v-if="showPurchaseModal" class="modal-overlay" @click="closePurchaseModal">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h3>购买松花湖风光摄影集</h3>
        <button class="close-btn" @click="closePurchaseModal">&times;</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label for="purchase-name">姓名</label>
          <input type="text" id="purchase-name" v-model="purchaseForm.name" placeholder="请输入您的姓名" />
        </div>
        <div class="form-group">
          <label for="purchase-phone">手机号码</label>
          <input type="tel" id="purchase-phone" v-model="purchaseForm.phone" placeholder="请输入您的手机号码" />
        </div>
        <div class="form-group">
          <label for="purchase-email">电子邮箱</label>
          <input type="email" id="purchase-email" v-model="purchaseForm.email" placeholder="请输入您的电子邮箱" />
        </div>
        <div class="form-group">
          <label for="purchase-address">收货地址</label>
          <textarea id="purchase-address" v-model="purchaseForm.address" placeholder="请输入您的收货地址" rows="3"></textarea>
        </div>
        <div class="form-group">
          <label for="purchase-quantity">购买数量</label>
          <input type="number" id="purchase-quantity" v-model="purchaseForm.quantity" min="1" />
        </div>
        <div class="form-group checkbox-group">
          <input type="checkbox" id="purchase-agree" v-model="purchaseForm.agree" />
          <label for="purchase-agree">我已阅读并同意购买协议和隐私政策</label>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" @click="closePurchaseModal">取消</button>
        <button class="btn btn-primary" @click="submitPurchase" :disabled="!purchaseForm.agree">确认购买</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import orderAPI from '../api/orders'

const router = useRouter()
const showBackToTop = ref(false)
const showPurchaseModal = ref(false)
const purchaseForm = ref({
  name: '',
  phone: '',
  email: '',
  address: '',
  quantity: 1,
  agree: false
})
const loading = ref(false)

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

const openPurchaseModal = () => {
  // 检查用户是否登录
  const user = localStorage.getItem('user')
  if (!user) {
    alert('请先登录')
    router.push('/login')
    return
  }
  showPurchaseModal.value = true
}

const closePurchaseModal = () => {
  showPurchaseModal.value = false
}

const submitPurchase = async () => {
  if (!purchaseForm.value.agree) return
  
  try {
    loading.value = true
    const orderId = 'ORD' + Date.now()
    const orderData = {
      order_id: orderId,
      item: '松花湖风光摄影集',
      price: 128,
      quantity: purchaseForm.value.quantity,
      total_price: 128 * purchaseForm.value.quantity,
      status: '待付款'
    }
    
    await orderAPI.createOrder(orderData)
    alert('购买成功！')
    showPurchaseModal.value = false
    
    // 跳转到我的页面
    router.push('/profile')
  } catch (error) {
    console.error('购买失败:', error)
    alert('购买失败，请稍后重试')
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.product-detail {
  padding-bottom: 60px;
}

.product-info-section {
  background-color: var(--light-bg);
  padding: 40px 0;
}

.product-info {
  display: flex;
  gap: 40px;
  align-items: flex-start;
}

.product-images {
  flex: 1;
  max-width: 500px;
}

.main-image {
  margin-bottom: 20px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.main-image img {
  width: 100%;
  height: auto;
  display: block;
}

.thumbnails {
  display: flex;
  gap: 12px;
}

.thumbnail {
  flex: 1;
  border-radius: 4px;
  overflow: hidden;
  cursor: pointer;
  border: 2px solid transparent;
  transition: border-color 0.3s;
}

.thumbnail.active {
  border-color: var(--primary-color);
}

.thumbnail img {
  width: 100%;
  height: auto;
  display: block;
}

.product-details {
  flex: 1;
  max-width: 500px;
}

.product-details h1 {
  font-size: 28px;
  margin-bottom: 16px;
  color: var(--text-primary);
}

.product-rating {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  gap: 12px;
}

.rating {
  font-size: 20px;
  font-weight: 600;
  color: var(--primary-color);
}

.stars {
  display: flex;
  gap: 4px;
}

.star {
  color: #ddd;
  font-size: 16px;
}

.star.active {
  color: #ffc107;
}

.review-count {
  color: var(--text-secondary);
  font-size: 14px;
}

.product-price {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.price {
  font-size: 32px;
  font-weight: 700;
  color: var(--primary-color);
}

.original-price {
  font-size: 20px;
  color: var(--text-secondary);
  text-decoration: line-through;
}

.discount {
  background-color: #ff4d4f;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
}

.product-sales {
  margin-bottom: 20px;
  color: var(--text-secondary);
  font-size: 14px;
}

.product-description {
  margin-bottom: 30px;
  line-height: 1.6;
  color: var(--text-primary);
}

.product-actions {
  display: flex;
  gap: 16px;
}

.buy-now {
  flex: 1;
  background-color: var(--primary-color);
  color: white;
  border: none;
  padding: 16px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
}

.buy-now:hover {
  background-color: var(--primary-hover);
}

.add-to-cart {
  flex: 1;
  background-color: white;
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
  padding: 16px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.add-to-cart:hover {
  background-color: var(--primary-color);
  color: white;
}

.product-details-section {
  padding: 60px 0;
  border-top: 1px solid var(--border-color);
}

.details-tabs {
  display: flex;
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 30px;
}

.tab {
  padding: 16px 32px;
  background: none;
  border: none;
  font-size: 16px;
  font-weight: 500;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.3s;
  border-bottom: 3px solid transparent;
}

.tab.active {
  color: var(--primary-color);
  border-bottom-color: var(--primary-color);
}

.tab-content {
  line-height: 1.6;
  color: var(--text-primary);
}

.tab-content h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

.tab-content h3 {
  font-size: 18px;
  margin: 20px 0 12px;
}

.tab-content ul {
  margin: 12px 0;
  padding-left: 24px;
}

.tab-content li {
  margin-bottom: 8px;
}

.related-products-section {
  padding: 60px 0;
  background-color: var(--light-bg);
}

.related-products-section h2 {
  font-size: 24px;
  margin-bottom: 30px;
  text-align: center;
}

.related-products {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 30px;
}

.related-product {
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
}

.related-product:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.related-product img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.related-product h3 {
  padding: 16px;
  font-size: 16px;
  margin: 0;
}

.related-product p {
  padding: 0 16px 16px;
  font-size: 18px;
  font-weight: 600;
  color: var(--primary-color);
  margin: 0;
}

@media (max-width: 768px) {
  .product-info {
    flex-direction: column;
    align-items: center;
  }
  
  .product-images,
  .product-details {
    max-width: 100%;
    width: 100%;
  }
  
  .product-actions {
    flex-direction: column;
  }
  
  .related-products {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .related-products {
    grid-template-columns: 1fr;
  }
}

/* 模态框样式 */
.modal-overlay {
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
  border-radius: var(--radius-lg);
  width: 90%;
  max-width: 500px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: var(--shadow-lg);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px;
  border-bottom: 1px solid var(--border-color);
}

.modal-header h3 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  color: var(--text-dark);
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: var(--text-medium);
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius);
  transition: var(--transition);
}

.close-btn:hover {
  background-color: var(--bg-light);
  color: var(--text-dark);
}

.modal-body {
  padding: 24px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--text-dark);
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  font-size: 16px;
  transition: var(--transition);
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(26, 188, 156, 0.2);
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.checkbox-group {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.checkbox-group input {
  margin-top: 2px;
  width: auto;
}

.checkbox-group label {
  margin-bottom: 0;
  flex: 1;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  padding: 24px;
  border-top: 1px solid var(--border-color);
}

.modal-footer .btn {
  flex: 1;
  max-width: 120px;
  padding: 12px 24px;
  border: none;
  border-radius: var(--radius-md);
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.btn-primary {
  background-color: var(--primary-color);
  color: var(--white);
}

.btn-primary:hover {
  background-color: var(--primary-hover);
}

.btn-secondary {
  background-color: var(--white);
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
}

.btn-secondary:hover {
  background-color: var(--primary-light);
}

/* 响应式 */
@media (max-width: 768px) {
  .modal-content {
    width: 95%;
  }
  
  .modal-header,
  .modal-body,
  .modal-footer {
    padding: 16px;
  }
}
</style>