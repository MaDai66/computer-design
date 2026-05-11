<template>
  <div class="product-detail">
    <div class="container">
      <section class="product-main">
        <div class="product-header">
          <h1>长白山天然蜂蜜</h1>
          <div class="product-tags">
            <span class="tag tag-orange">原产地</span>
            <span class="tag tag-green">助农</span>
          </div>
          <div class="product-price">
            <span class="price">¥88 / 瓶</span>
            <span class="stock">库存: 800瓶</span>
          </div>
          <div class="product-stats">
            <span class="sales">销量: 1890瓶</span>
            <span class="rating">⭐⭐⭐⭐⭐ 4.9 (450条评价)</span>
          </div>
        </div>
        <div class="product-images">
          <div class="main-image">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbai%20Mountain%20natural%20honey%20Jilin%20agricultural%20product&image_size=landscape_16_9" alt="长白山天然蜂蜜" />
          </div>
          <div class="gallery">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Honey%20jar%20glass%20container%20natural%20product&image_size=portrait_4_3" alt="蜂蜜特写" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Bees%20collecting%20nectar%20in%20flower%20field&image_size=portrait_4_3" alt="蜜蜂采蜜" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Honey%20harvesting%20process%20traditional%20method&image_size=portrait_4_3" alt="蜂蜜采集" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Honey%20tasting%20natural%20sweet%20product&image_size=portrait_4_3" alt="蜂蜜品尝" />
          </div>
        </div>
      </section>

      <section class="product-description">
        <h2>商品描述</h2>
        <div class="description-content">
          <p>长白山天然蜂蜜采自长白山原始森林，由野生蜜蜂采集多种野花的花蜜酿制而成，无任何添加，保持了蜂蜜的天然营养成分。本品色泽金黄，口感醇厚，甜而不腻，是纯天然的健康食品。</p>
          <p>长白山天然蜂蜜富含多种维生素、矿物质和氨基酸，具有润肠通便、增强免疫力、美容养颜等功效。是日常保健、调味烹饪的理想选择。</p>
        </div>
      </section>

      <section class="product-specs">
        <h2>规格参数</h2>
        <div class="specs-content">
          <table class="specs-table">
            <tbody>
            <tr>
              <th>规格</th>
              <td>500g/瓶</td>
            </tr>
            <tr>
              <th>产地</th>
              <td>吉林省长白山</td>
            </tr>
            <tr>
              <th>采集方式</th>
              <td>野生蜜蜂天然采集</td>
            </tr>
            <tr>
              <th>储存方式</th>
              <td>阴凉干燥处保存</td>
            </tr>
            <tr>
              <th>保质期</th>
              <td>24个月</td>
            </tr>
            <tr>
              <th>包装</th>
              <td>玻璃瓶装</td>
            </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="product-origin">
        <h2>产地溯源</h2>
        <div class="origin-content">
          <div class="farmer-info">
            <h3>长白山养蜂人</h3>
            <p>本品由长白山当地养蜂人精心培育的野生蜜蜂采集酿制，采用传统养蜂方法，不使用任何化学药物，确保蜂蜜的纯天然品质。养蜂人严格遵循自然规律，保护蜜蜂和生态环境。</p>
          </div>
          <div class="process-info">
            <h3>采集流程</h3>
            <ol>
              <li>蜜蜂在长白山原始森林中采集多种野花的花蜜</li>
              <li>蜜蜂将花蜜带回蜂巢酿制</li>
              <li>养蜂人采用传统方法采集蜂蜜</li>
              <li>经过过滤、装瓶等工序</li>
              <li>密封包装，保持新鲜</li>
            </ol>
          </div>
        </div>
      </section>

      <section class="product-quality">
        <h2>质检报告</h2>
        <div class="quality-content">
          <p>本品经过严格的质量检测，符合国家蜂蜜质量标准。检测项目包括水分含量、蔗糖含量、重金属含量、微生物指标等，确保产品安全可靠。</p>
          <div class="quality-image">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Quality%20inspection%20report%20certificate%20honey&image_size=landscape_16_9" alt="质检报告" />
          </div>
        </div>
      </section>

      <section class="purchase-section">
        <h2>购买</h2>
        <div class="purchase-content">
          <div class="price-info">
            <span class="current-price">¥88</span>
            <span class="original-price">¥118</span>
            <span class="discount">7.5折</span>
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
            <span class="rating-score">4.9</span>
            <span class="rating-stars">⭐⭐⭐⭐⭐</span>
            <span class="rating-count">450条评价</span>
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
                  <span class="user-name">@养生达人</span>
                  <span class="review-date">2026-04-10</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>长白山天然蜂蜜真的非常好！颜色金黄，口感醇厚，甜而不腻，有淡淡的花香。用来泡水喝，味道很棒。包装也很精美，送人体面。非常推荐！</p>
              <div class="review-images">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Honey%20jar%20glass%20container%20natural%20product&image_size=portrait_4_3" alt="蜂蜜特写" />
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Honey%20tasting%20natural%20sweet%20product&image_size=portrait_4_3" alt="蜂蜜品尝" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@健康生活</span>
                  <span class="review-date">2026-04-05</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>第一次购买长白山天然蜂蜜，收到后非常满意。蜂蜜的质量很好，口感纯正，没有添加剂的味道。每天早上用温水冲泡一杯，感觉很舒服。价格也很合理，比超市买的蜂蜜好很多。会回购的！</p>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@美食爱好者</span>
                  <span class="review-date">2026-03-28</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>用长白山天然蜂蜜做烘焙，味道非常好！蜂蜜的甜度适中，有浓郁的花香，做出来的蛋糕和面包口感特别好。包装也很精美，玻璃瓶装，看起来很高档。非常满意的一次购物！</p>
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
          <h3>购买长白山天然蜂蜜</h3>
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
      item: '长白山天然蜂蜜',
      price: 88,
      quantity: purchaseForm.value.quantity,
      total_price: 88 * purchaseForm.value.quantity,
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