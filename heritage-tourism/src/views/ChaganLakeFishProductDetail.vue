<template>
  <div class="product-detail">
    <div class="container">
      <section class="product-main">
        <div class="product-header">
          <h1>查干湖有机鱼</h1>
          <div class="product-tags">
            <span class="tag tag-blue">有机食品</span>
            <span class="tag tag-green">助农</span>
          </div>
          <div class="product-price">
            <span class="price">¥168 / 条</span>
            <span class="stock">库存: 500条</span>
          </div>
          <div class="product-stats">
            <span class="sales">销量: 1560条</span>
            <span class="rating">⭐⭐⭐⭐⭐ 4.7 (156条评价)</span>
          </div>
        </div>
        <div class="product-images">
          <div class="main-image">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20organic%20fish%20fresh%20water&image_size=landscape_16_9" alt="查干湖有机鱼" />
          </div>
          <div class="gallery">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20fish%20from%20Chagan%20Lake&image_size=portrait_4_3" alt="查干湖有机鱼" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20catch&image_size=portrait_4_3" alt="查干湖有机鱼" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20water%20fish%20organic%20product&image_size=portrait_4_3" alt="查干湖有机鱼" />
          </div>
        </div>
      </section>

      <section class="product-description">
        <h2>商品描述</h2>
        <div class="description-content">
          <p>查干湖有机鱼是吉林查干湖的特色产品，以其鲜美的口感和丰富的营养而闻名。来自查干湖天然水域，有机养殖，无添加，肉质鲜美，营养丰富，是冬季进补的佳品。</p>
          <p>本品采用传统捕捞方式，确保鱼肉的新鲜度和品质。每一条鱼都经过严格的质量检测，确保安全可靠。</p>
        </div>
      </section>

      <section class="product-specs">
        <h2>规格参数</h2>
        <div class="specs-content">
          <table class="specs-table">
            <tbody>
            <tr>
              <th>规格</th>
              <td>2-3斤/条</td>
            </tr>
            <tr>
              <th>品种</th>
              <td>胖头鱼</td>
            </tr>
            <tr>
              <th>保质期</th>
              <td>冷冻保存12个月</td>
            </tr>
            <tr>
              <th>储存方式</th>
              <td>冷冻</td>
            </tr>
            <tr>
              <th>产地</th>
              <td>吉林省查干湖</td>
            </tr>
            <tr>
              <th>食用方法</th>
              <td>清蒸、红烧、煮汤等</td>
            </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="product-origin">
        <h2>产地溯源</h2>
        <div class="origin-content">
          <div class="farmer-info">
            <h3>查干湖生态环境</h3>
            <p>查干湖是吉林省最大的天然湖泊，水质清澈，生态环境优美，为鱼类提供了良好的生长环境。湖中鱼类天然生长，不使用任何人工饲料，保证了鱼肉的纯天然品质。</p>
          </div>
          <div class="process-info">
            <h3>捕捞流程</h3>
            <ol>
              <li>冬季冰面捕捞</li>
              <li>新鲜处理</li>
              <li>快速冷冻</li>
              <li>包装运输</li>
            </ol>
          </div>
        </div>
      </section>



      <section class="purchase-section">
        <h2>购买</h2>
        <div class="purchase-content">
          <div class="price-info">
            <span class="current-price">¥168</span>
            <span class="original-price">¥198</span>
            <span class="discount">15% OFF</span>
          </div>
          <div class="quantity-control">
            <label>数量</label>
            <div class="quantity-input">
              <button class="btn-minus" @click="decreaseQuantity">&minus;</button>
              <input type="number" v-model="quantity" min="1" />
              <button class="btn-plus" @click="increaseQuantity">&plus;</button>
            </div>
          </div>
          <div class="purchase-buttons">
            <button class="btn btn-secondary add-to-cart">加入购物车</button>
            <button class="btn btn-primary buy-now" @click="openPurchaseModal">立即购买</button>
          </div>
        </div>
      </section>

      <section class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-header">
          <div class="rating-overall">
            <span class="rating-score">4.7</span>
            <span class="rating-stars">⭐⭐⭐⭐⭐</span>
            <span class="rating-count">156条评价</span>
          </div>
          <div class="review-filter">
            <button class="filter-btn active">全部评价</button>
            <button class="filter-btn">好评</button>
            <button class="filter-btn">中评</button>
            <button class="filter-btn">差评</button>
            <button class="filter-btn">有图</button>
          </div>
        </div>
        <div class="reviews-list">
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@美食爱好者</span>
                  <span class="review-date">2026-04-10</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>查干湖有机鱼非常新鲜，肉质鲜嫩，没有腥味。清蒸之后味道非常好，家人都很喜欢。价格也很合理，比超市买的鱼新鲜很多。非常推荐！</p>
              <div class="review-images">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Steamed%20fish%20dish&image_size=portrait_4_3" alt="清蒸鱼" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@厨师</span>
                  <span class="review-date">2026-04-05</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>作为一名厨师，我对食材的要求很高。查干湖有机鱼的品质非常好，肉质鲜嫩，口感细腻。用来做红烧鱼和鱼头汤都非常美味。非常满意！</p>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@家庭主妇</span>
                  <span class="review-date">2026-03-28</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>买给家人的，家人都很喜欢。鱼很新鲜，没有腥味，做出来的汤很鲜美。包装也很用心，收到的时候还是冷冻状态。非常推荐！</p>
            </div>
          </div>
        </div>
      </section>
    </div>

    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>

    <div v-if="showPurchaseModal" class="modal-overlay" @click="closePurchaseModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>购买查干湖有机鱼</h3>
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
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import orderAPI from '../api/orders'

const router = useRouter()

const showBackToTop = ref(false)
const quantity = ref(1)
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

const increaseQuantity = () => {
  quantity.value++
  purchaseForm.value.quantity = quantity.value
}

const decreaseQuantity = () => {
  if (quantity.value > 1) {
    quantity.value--
    purchaseForm.value.quantity = quantity.value
  }
}

const openPurchaseModal = () => {
  // 检查用户是否登录
  const user = localStorage.getItem('user')
  if (!user) {
    alert('请先登录')
    router.push('/login')
    return
  }
  purchaseForm.value.quantity = quantity.value
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
      item: '查干湖有机鱼',
      price: 168,
      quantity: purchaseForm.value.quantity,
      total_price: 168 * purchaseForm.value.quantity,
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
  background-color: var(--bg-light);
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 48px 24px;
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
  padding-bottom: 16px;
  border-bottom: 2px solid var(--primary-color);
}

.product-header h1 {
  font-size: 32px;
  font-weight: 700;
  color: var(--text-dark);
  margin-bottom: 16px;
}

.product-tags {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

.tag {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
}

.tag-orange {
  background-color: var(--accent-orange-light);
  color: var(--accent-orange);
}

.tag-green {
  background-color: var(--accent-green-light);
  color: var(--accent-green);
}

.tag-blue {
  background-color: var(--accent-blue-light);
  color: var(--accent-blue);
}

.product-price {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 16px;
}

.price {
  font-size: 24px;
  font-weight: 700;
  color: var(--accent-orange);
}

.stock {
  font-size: 16px;
  color: var(--text-medium);
}

.product-stats {
  display: flex;
  align-items: center;
  gap: 24px;
  font-size: 14px;
  color: var(--text-medium);
}

.product-images {
  margin-bottom: 24px;
}

.main-image {
  width: 100%;
  height: 400px;
  border-radius: var(--radius-md);
  overflow: hidden;
  margin-bottom: 16px;
}

.main-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.gallery img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: var(--transition);
}

.gallery img:hover {
  transform: scale(1.05);
  box-shadow: var(--shadow-hover);
}

.description-content p {
  line-height: 1.6;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.description-content p:last-child {
  margin-bottom: 0;
}

.specs-table {
  width: 100%;
  border-collapse: collapse;
}

.specs-table th,
.specs-table td {
  padding: 12px;
  border-bottom: 1px solid var(--border-color);
}

.specs-table th {
  width: 150px;
  font-weight: 600;
  color: var(--text-dark);
  text-align: left;
  background-color: var(--bg-light);
}

.specs-table td {
  color: var(--text-medium);
}

.origin-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.farmer-info h3,
.process-info h3 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
}

.farmer-info p {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 0;
}

.process-info ol {
  padding-left: 20px;
  margin: 0;
}

.process-info li {
  margin-bottom: 8px;
  line-height: 1.4;
  color: var(--text-medium);
}

.process-info li:last-child {
  margin-bottom: 0;
}

.quality-content p {
  line-height: 1.6;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.quality-image {
  width: 100%;
  border-radius: var(--radius-md);
  overflow: hidden;
}

.quality-image img {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.purchase-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.price-info {
  display: flex;
  align-items: center;
  gap: 16px;
}

.current-price {
  font-size: 28px;
  font-weight: 700;
  color: var(--accent-orange);
}

.original-price {
  font-size: 18px;
  color: var(--text-light);
  text-decoration: line-through;
}

.discount {
  font-size: 14px;
  color: var(--accent-orange);
  background-color: var(--accent-orange-light);
  padding: 4px 8px;
  border-radius: 12px;
}

.quantity-control {
  display: flex;
  align-items: center;
  gap: 16px;
}

.quantity-control label {
  font-weight: 500;
  color: var(--text-dark);
}

.quantity-input {
  display: flex;
  align-items: center;
  gap: 8px;
}

.quantity-input button {
  width: 32px;
  height: 32px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  background-color: var(--white);
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}

.quantity-input button:hover {
  background-color: var(--bg-light);
  border-color: var(--primary-color);
}

.quantity-input input {
  width: 60px;
  height: 32px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  text-align: center;
  font-size: 16px;
}

.quantity-input input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(26, 188, 156, 0.2);
}

.purchase-buttons {
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

.reviews-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 16px;
}

.rating-overall {
  display: flex;
  align-items: center;
  gap: 12px;
}

.rating-score {
  font-size: 32px;
  font-weight: 700;
  color: var(--accent-orange);
}

.rating-stars {
  font-size: 16px;
  color: var(--accent-orange);
}

.rating-count {
  font-size: 14px;
  color: var(--text-medium);
}

.review-filter {
  display: flex;
  gap: 8px;
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
}

@media (max-width: 768px) {
  .container {
    padding: 24px 16px;
  }
  
  section {
    padding: 24px;
    margin-bottom: 24px;
  }
  
  .product-header h1 {
    font-size: 24px;
  }
  
  .main-image {
    height: 300px;
  }
  
  .gallery {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .origin-content {
    grid-template-columns: 1fr;
  }
  
  .purchase-buttons {
    flex-direction: column;
  }
  
  .reviews-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .modal-content {
    width: 95%;
  }
}

@media (max-width: 480px) {
  .gallery {
    grid-template-columns: 1fr;
  }
  
  .review-images {
    flex-direction: column;
  }
  
  .review-images img {
    width: 100%;
    height: auto;
  }
}
</style>