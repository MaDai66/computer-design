<template>
  <div class="product-detail">
    <div class="container">
      <section class="product-main">
        <div class="product-header">
          <h1>吉林有机玉米</h1>
          <div class="product-tags">
            <span class="tag tag-orange">原产地</span>
            <span class="tag tag-green">助农</span>
          </div>
          <div class="product-price">
            <span class="price">¥39.9 / 5斤</span>
            <span class="stock">库存: 1000斤</span>
          </div>
          <div class="product-stats">
            <span class="sales">销量: 2560斤</span>
            <span class="rating">⭐⭐⭐⭐⭐ 4.8 (520条评价)</span>
          </div>
        </div>
        <div class="product-images">
          <div class="main-image">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20organic%20corn%20agricultural%20products&image_size=landscape_16_9" alt="吉林有机玉米" />
          </div>
          <div class="gallery">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20corn%20cobs%20on%20the%20stalk&image_size=portrait_4_3" alt="玉米特写" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Corn%20farm%20field%20Jilin%20China&image_size=portrait_4_3" alt="玉米种植" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Organic%20corn%20packaging%20natural%20style&image_size=portrait_4_3" alt="玉米包装" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Corn%20cooking%20boiled%20corn%20ears&image_size=portrait_4_3" alt="玉米烹饪" />
          </div>
        </div>
      </section>

      <section class="product-description">
        <h2>商品描述</h2>
        <div class="description-content">
          <p>吉林有机玉米是吉林省的特产，采用有机种植方式，不使用化肥和农药，保证玉米的纯天然品质。本品来自吉林肥沃的黑土地，阳光充足，水源纯净，种植出的玉米口感香甜，营养丰富。</p>
          <p>吉林有机玉米富含膳食纤维、维生素和矿物质，是健康饮食的理想选择。煮食口感软糯香甜，是家庭日常饮食的美味食材。</p>
        </div>
      </section>

      <section class="product-specs">
        <h2>规格参数</h2>
        <div class="specs-content">
          <table class="specs-table">
            <tbody>
            <tr>
              <th>规格</th>
              <td>5斤装（约8-10根）</td>
            </tr>
            <tr>
              <th>产地</th>
              <td>吉林省</td>
            </tr>
            <tr>
              <th>种植方式</th>
              <td>有机种植</td>
            </tr>
            <tr>
              <th>储存方式</th>
              <td>阴凉干燥处保存</td>
            </tr>
            <tr>
              <th>保质期</th>
              <td>7天（新鲜）</td>
            </tr>
            <tr>
              <th>包装</th>
              <td>环保真空包装</td>
            </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="product-origin">
        <h2>产地溯源</h2>
        <div class="origin-content">
          <div class="farmer-info">
            <h3>吉林农户</h3>
            <p>本品由吉林当地农户种植，采用传统有机种植方式，不使用化肥和农药，确保玉米的纯天然品质。农户严格遵循有机种植规范，保护土壤和生态环境。</p>
          </div>
          <div class="process-info">
            <h3>种植流程</h3>
            <ol>
              <li>选择优质有机玉米种子</li>
              <li>在吉林肥沃的黑土地上种植</li>
              <li>采用有机肥料和天然防治方法</li>
              <li>人工采摘，确保新鲜</li>
              <li>真空包装，保持新鲜</li>
            </ol>
          </div>
        </div>
      </section>

      <section class="product-quality">
        <h2>质检报告</h2>
        <div class="quality-content">
          <p>本品经过严格的质量检测，符合有机食品标准。检测项目包括农药残留、重金属含量、微生物指标等，确保产品安全可靠。</p>
          <div class="quality-image">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Quality%20inspection%20report%20certificate%20organic%20corn&image_size=landscape_16_9" alt="质检报告" />
          </div>
        </div>
      </section>

      <section class="purchase-section">
        <h2>购买</h2>
        <div class="purchase-content">
          <div class="price-info">
            <span class="current-price">¥39.9</span>
            <span class="original-price">¥49.9</span>
            <span class="discount">8折</span>
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
            <span class="rating-score">4.8</span>
            <span class="rating-stars">⭐⭐⭐⭐⭐</span>
            <span class="rating-count">520条评价</span>
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
                  <span class="user-name">@健康生活</span>
                  <span class="review-date">2026-04-10</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>吉林有机玉米非常好吃，口感香甜软糯，煮出来的玉米香气四溢。包装也很新鲜，收到的时候玉米还是很嫩的。价格也很合理，比超市买的有机玉米便宜很多。非常推荐！</p>
              <div class="review-images">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20corn%20cobs%20on%20the%20stalk&image_size=portrait_4_3" alt="玉米特写" />
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Corn%20cooking%20boiled%20corn%20ears&image_size=portrait_4_3" alt="玉米烹饪" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@美食爱好者</span>
                  <span class="review-date">2026-04-05</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>第一次购买吉林有机玉米，收到后非常满意。玉米颗粒饱满，颜色金黄，煮出来的味道香甜，比普通玉米好吃很多。包装也很用心，真空包装保持了玉米的新鲜度。会回购的！</p>
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
              <p>给孩子买的，孩子非常喜欢吃。玉米很新鲜，没有农药残留，吃着放心。煮起来也很方便，15分钟就好了。价格也很实惠，比超市便宜。非常满意的一次购物！</p>
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
          <h3>购买吉林有机玉米</h3>
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
const showPurchaseModal = ref(false)
const loading = ref(false)

const purchaseForm = ref({
  name: '',
  phone: '',
  email: '',
  address: '',
  quantity: 1,
  agree: false
})

const quantity = ref(1)

const decreaseQuantity = () => {
  if (quantity.value > 1) {
    quantity.value--
  }
}

const increaseQuantity = () => {
  quantity.value++
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
      item: '吉林有机玉米',
      price: 39.9,
      quantity: purchaseForm.value.quantity,
      total_price: parseFloat((39.9 * purchaseForm.value.quantity).toFixed(2)),
      status: '待付款'
    }
    
    await orderAPI.createOrder(orderData)
    alert('购买成功！')
    closePurchaseModal()
    router.push('/profile')
  } catch (error) {
    console.error('购买失败:', error)
    alert('购买失败，请稍后重试')
  } finally {
    loading.value = false
  }
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
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: var(--text-medium);
  cursor: pointer;
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

.modal-body .form-group {
  margin-bottom: 16px;
}

.modal-body label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--text-dark);
}

.modal-body input,
.modal-body textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  font-size: 14px;
  transition: var(--transition);
}

.modal-body input:focus,
.modal-body textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(26, 188, 156, 0.2);
}

.modal-body textarea {
  resize: vertical;
  min-height: 80px;
}

.checkbox-group {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.checkbox-group input[type="checkbox"] {
  width: auto;
  margin-top: 2px;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  padding: 24px;
  border-top: 1px solid var(--border-color);
}

.modal-footer .btn {
  min-width: 100px;
}

@media (max-width: 768px) {
  .container {
    padding: 24px 16px;
  }
  
  .product-header h1 {
    font-size: 24px;
  }
  
  .main-image {
    height: 250px;
  }
  
  .gallery {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .origin-content {
    grid-template-columns: 1fr;
  }
  
  .quality-image img {
    height: 200px;
  }
  
  .purchase-buttons {
    flex-direction: column;
  }
  
  .back-to-top {
    bottom: 20px;
    right: 20px;
  }
  
  .modal-content {
    width: 95%;
    margin: 20px;
  }
  
  .modal-header,
  .modal-body,
  .modal-footer {
    padding: 16px;
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