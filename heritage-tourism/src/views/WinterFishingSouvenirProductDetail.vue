<template>
  <div class="product-detail">
    <div class="container">
      <section class="product-main">
        <div class="product-header">
          <h1>查干湖冬捕纪念套装</h1>
          <div class="product-tags">
            <span class="tag tag-orange">文化纪念</span>
            <span class="tag tag-green">传统工艺</span>
          </div>
          <div class="product-price">
            <span class="price">¥198 / 套</span>
            <span class="stock">库存: 300套</span>
          </div>
          <div class="product-stats">
            <span class="sales">销量: 620套</span>
            <span class="rating">⭐⭐⭐⭐⭐ 4.7 (62条评价)</span>
          </div>
        </div>
        <div class="product-images">
          <div class="main-image">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20souvenir%20set%20with%20traditional%20fishing%20tools%20and%20cultural%20elements&image_size=landscape_16_9" alt="查干湖冬捕纪念套装" />
          </div>
          <div class="gallery">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20souvenir%20box%20open%20with%20coins%20and%20postcards&image_size=portrait_4_3" alt="查干湖冬捕纪念套装" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Traditional%20Chagan%20Lake%20winter%20fishing%20culture%20elements&image_size=portrait_4_3" alt="查干湖冬捕纪念套装" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Winter%20fishing%20memorial%20gift%20set%20with%20cultural%20booklet&image_size=portrait_4_3" alt="查干湖冬捕纪念套装" />
          </div>
        </div>
      </section>

      <section class="product-description">
        <h2>商品描述</h2>
        <div class="description-content">
          <p>查干湖冬捕纪念套装是为了纪念查干湖冬捕这一传统渔猎文化而设计的纪念品套装。包含多种冬捕主题纪念品，精美包装，适合收藏，具有文化价值和纪念意义。</p>
          <p>本品采用精美包装，设计独特，体现了查干湖冬捕的文化特色，是吉林旅游的最佳纪念品之一。</p>
        </div>
      </section>

      <section class="product-specs">
        <h2>规格参数</h2>
        <div class="specs-content">
          <table class="specs-table">
            <tbody>
            <tr>
              <th>规格</th>
              <td>1套</td>
            </tr>
            <tr>
              <th>包装尺寸</th>
              <td>长25cm × 宽18cm × 高6cm</td>
            </tr>
            <tr>
              <th>套装内容</th>
              <td>冬捕主题纪念币、冬捕文化明信片、冬捕主题钥匙扣、冬捕文化手册</td>
            </tr>
            <tr>
              <th>材质</th>
              <td>金属、纸质、塑料</td>
            </tr>
            <tr>
              <th>产地</th>
              <td>吉林省</td>
            </tr>
            <tr>
              <th>用途</th>
              <td>纪念收藏、礼品赠送</td>
            </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="product-origin">
        <h2>产地溯源</h2>
        <div class="origin-content">
          <div class="farmer-info">
            <h3>冬捕文化传承</h3>
            <p>查干湖冬捕是吉林传统渔猎文化的重要组成部分，已有上千年的历史。这套纪念品旨在传承和弘扬这一独特的文化遗产，让更多人了解和认识查干湖冬捕的文化价值。</p>
          </div>
          <div class="process-info">
            <h3>制作流程</h3>
            <ol>
              <li>设计创意方案</li>
              <li>精选材料</li>
              <li>精心制作</li>
              <li>质量检测</li>
              <li>精美包装</li>
            </ol>
          </div>
        </div>
      </section>



      <section class="purchase-section">
        <h2>购买</h2>
        <div class="purchase-content">
          <div class="price-info">
            <span class="current-price">¥198</span>
            <span class="original-price">¥258</span>
            <span class="discount">23% OFF</span>
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
            <span class="rating-count">62条评价</span>
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
                  <span class="user-name">@文化爱好者</span>
                  <span class="review-date">2026-04-10</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>查干湖冬捕纪念套装非常精美，包装漂亮，内容丰富。包含的纪念品都很有特色，体现了查干湖冬捕的文化元素。非常适合作为纪念收藏或礼品赠送。价格也很合理，非常推荐！</p>
              <div class="review-images">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20souvenir%20set%20open%20showing%20contents&image_size=portrait_4_3" alt="冬捕纪念套装打开" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@旅游爱好者</span>
                  <span class="review-date">2026-04-05</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>买给朋友的礼物，朋友非常喜欢。套装包装精美，内容丰富，设计独特。朋友说这是他收到的最有意义的旅游纪念品。非常满意！</p>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@收藏爱好者</span>
                  <span class="review-date">2026-03-28</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>作为一名收藏爱好者，我对这个纪念套装非常满意。它融合了查干湖冬捕的文化元素，设计精美，内容丰富。每一件纪念品都很有特色，体现了吉林的地域文化。非常推荐！</p>
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
          <h3>购买查干湖冬捕纪念套装</h3>
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
      item: '查干湖冬捕纪念套装',
      price: 198,
      quantity: purchaseForm.value.quantity,
      total_price: 198 * purchaseForm.value.quantity,
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