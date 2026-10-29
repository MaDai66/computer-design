<template>
  <div class="activity-detail">

    <div class="container">
      <!-- 活动主信息 -->
      <section class="activity-main">
        <div class="activity-header">
          <h1>查干湖冬捕开网仪式</h1>
          <div class="activity-tags">
            <span class="tag tag-orange">非遗活动</span>
            <span class="tag tag-blue">冬捕文化</span>
            <span class="tag tag-green">特色体验</span>
          </div>
          <div class="activity-info">
            <div class="info-item">
              <span class="info-label">活动时间：</span>
              <span class="info-value">2026年4月15日 08:00-12:00</span>
            </div>
            <div class="info-item">
              <span class="info-label">活动地点：</span>
              <span class="info-value">吉林省松原市查干湖景区</span>
            </div>
            <div class="info-item">
              <span class="info-label">活动费用：</span>
              <span class="info-value">¥288/人</span>
            </div>
            <div class="info-item">
              <span class="info-label">活动人数：</span>
              <span class="info-value">限300人</span>
            </div>
          </div>
        </div>
        <div class="activity-images">
          <div class="main-image">
            <img src="/image/ChaganLakeOpeningCeremony/5a5701a8aa8d5e21e73b1b2391f1ea28.jpeg" alt="查干湖冬捕开网仪式" />
          </div>
          <div class="gallery">
            <img src="/image/ChaganLakeOpeningCeremony/8efea36a0e7a2985dbe449f10f612318.jpeg" alt="查干湖冬捕拉网" />
            <img src="/image/ChaganLakeOpeningCeremony/a8991b81a8646d94ce2065c55b28197b.jpeg" alt="查干湖冬捕祭祀仪式" />
            <img src="/image/ChaganLakeOpeningCeremony/7cb99e2d0662a0949666edb779281368.jpeg" alt="查干湖鲜鱼" />
            <img :src="chaganhu1" alt="查干湖冬景" />
          </div>
        </div>
        <div class="activity-actions">
          <button class="btn btn-primary book-now" @click="openBookingModal">立即预订</button>
        </div>
      </section>

      <!-- 活动介绍 -->
      <section class="activity-intro">
        <h2>活动介绍</h2>
        <div class="intro-content">
          <p>查干湖冬捕开网仪式是国家级非物质文化遗产，历史悠久，是中国北方渔猎文化的重要组成部分。每年冬季，查干湖都会举行盛大的冬捕开网仪式，吸引了来自全国各地的游客前来观看。</p>
          <p>冬捕开网仪式包括传统的祭湖醒网仪式，由萨满法师主持，祈求丰收和平安。仪式结束后，渔民们会开始凿冰、下网、拉网，展示传统的冬捕技艺。</p>
          <p>本次活动将为您提供观捕席位，让您近距离观看冬捕全过程，感受千年渔猎文化的魅力。同时，您还可以品尝新鲜的查干湖鱼，体验东北冬季特色民俗。</p>
        </div>
      </section>

      <!-- 流程安排 -->
      <section class="activity-schedule">
        <h2>流程安排</h2>
        <div class="schedule-content">
          <div class="schedule-item">
            <div class="schedule-time">07:30-08:00</div>
            <div class="schedule-activity">
              <h3>集合签到</h3>
              <p>在查干湖景区指定地点集合，领取观捕凭证</p>
            </div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">08:00-09:00</div>
            <div class="schedule-activity">
              <h3>祭湖醒网仪式</h3>
              <p>观看传统的祭湖醒网仪式，由萨满法师主持，祈求丰收和平安</p>
            </div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">09:00-10:30</div>
            <div class="schedule-activity">
              <h3>冬捕过程</h3>
              <p>观看渔民凿冰、下网、拉网的全过程，感受传统冬捕技艺</p>
            </div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">10:30-11:30</div>
            <div class="schedule-activity">
              <h3>鲜鱼品尝</h3>
              <p>品尝刚捕捞的新鲜查干湖鱼，享受特色美食</p>
            </div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">11:30-12:00</div>
            <div class="schedule-activity">
              <h3>自由活动</h3>
              <p>自由活动，购买特色纪念品，拍照留念</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 报名须知 -->
      <section class="activity-notes">
        <h2>报名须知</h2>
        <div class="notes-content">
          <ul>
            <li>活动费用包含观捕席位、祭湖醒网仪式观看、冬捕过程观看、鲜鱼品尝</li>
            <li>活动费用不包含往返交通、个人消费等其他费用</li>
            <li>活动当天请穿着保暖衣物，如羽绒服、保暖裤、防滑鞋等</li>
            <li>请携带身份证等有效证件</li>
            <li>活动当天请准时集合，逾期不候</li>
            <li>因天气等不可抗力因素导致活动无法进行，将全额退款</li>
            <li>活动名额有限，先到先得</li>
          </ul>
        </div>
      </section>

      <!-- 预订表单 -->
      <section class="booking-form-section">
        <h2>预订表单</h2>
        <div class="form-content">
          <div class="form-group">
            <label for="booking-name">姓名</label>
            <input type="text" id="booking-name" v-model="bookingForm.name" placeholder="请输入您的姓名" />
          </div>
          <div class="form-group">
            <label for="booking-phone">手机号码</label>
            <input type="tel" id="booking-phone" v-model="bookingForm.phone" placeholder="请输入您的手机号码" />
          </div>
          <div class="form-group">
            <label for="booking-email">电子邮箱</label>
            <input type="email" id="booking-email" v-model="bookingForm.email" placeholder="请输入您的电子邮箱" />
          </div>
          <div class="form-group">
            <label for="booking-participants">参与人数</label>
            <input type="number" id="booking-participants" v-model="bookingForm.participants" min="1" value="1" />
          </div>
          <div class="form-group">
            <label for="booking-notes">备注信息</label>
            <textarea id="booking-notes" v-model="bookingForm.notes" placeholder="请输入备注信息（可选）"></textarea>
          </div>
          <div class="form-group checkbox-group">
            <input type="checkbox" id="booking-agree" v-model="bookingForm.agree" />
            <label for="booking-agree">我已阅读并同意活动的须知和隐私政策</label>
          </div>
          <button class="btn btn-primary submit-booking" @click="submitBooking" :disabled="!bookingForm.agree">提交预订</button>
        </div>
      </section>

      <!-- 用户评价 -->
      <section class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-header">
          <div class="rating-overall">
            <span class="rating-score">4.9</span>
            <span class="rating-stars">⭐⭐⭐⭐⭐</span>
            <span class="rating-count">860条评价</span>
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
                <img src="/image/UserAvatar/1.jpg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@旅行爱好者</span>
                  <span class="review-date">2026-01-15</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>查干湖冬捕开网仪式太震撼了！祭湖醒网仪式充满了神秘的萨满文化色彩，非常有特色。冬捕过程也很壮观，看到那么多鱼被拉上来，非常激动。鲜鱼品尝环节也很棒，刚捕捞的鱼非常新鲜，味道鲜美。活动组织得很有序，导游讲解也很专业。非常推荐！</p>
              <div class="review-images">
                <img src="/image/ChaganLakeOpeningCeremony/ac2bfa5d470f7c93799f1706c1eec9f7.jpeg" alt="冬捕仪式" />
                <img src="/image/ChaganLakeOpeningCeremony/7cb99e2d0662a0949666edb779281368.jpeg" alt="鲜鱼" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="/image/UserAvatar/2.jpg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@摄影爱好者</span>
                  <span class="review-date">2026-01-10</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>查干湖的冬景太美了！湖面结冰后一片雪白，非常适合拍照。冬捕开网仪式很有特色，特别是祭湖醒网仪式，非常壮观。冬捕过程也很震撼，看到渔民们齐心协力拉网，非常感动。鲜鱼也非常好吃，推荐大家来体验一下！</p>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="/image/UserAvatar/3.jpg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@家庭出游</span>
                  <span class="review-date">2025-12-25</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>带孩子一起参加的，孩子非常喜欢冬捕开网仪式。看到那么多鱼被拉上来，孩子很兴奋。活动组织得很有序，导游对孩子也很有耐心，讲解生动有趣。鲜鱼也非常好吃，特别是刚捕捞上来的胖头鱼，味道鲜美。非常推荐家庭出游！</p>
            </div>
          </div>
        </div>

      </section>
    </div>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>

    <!-- 预订模态框 -->
    <div v-if="showBookingModal" class="modal-overlay" @click="closeBookingModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>预订查干湖冬捕开网仪式</h3>
          <button class="close-btn" @click="closeBookingModal">&times;</button>
        </div>
        <div class="modal-body">
          <div class="form-group">
            <label for="modal-name">姓名</label>
            <input type="text" id="modal-name" v-model="bookingForm.name" placeholder="请输入您的姓名" />
          </div>
          <div class="form-group">
            <label for="modal-phone">手机号码</label>
            <input type="tel" id="modal-phone" v-model="bookingForm.phone" placeholder="请输入您的手机号码" />
          </div>
          <div class="form-group">
            <label for="modal-email">电子邮箱</label>
            <input type="email" id="modal-email" v-model="bookingForm.email" placeholder="请输入您的电子邮箱" />
          </div>
          <div class="form-group">
            <label for="modal-participants">参与人数</label>
            <input type="number" id="modal-participants" v-model="bookingForm.participants" min="1" value="1" />
          </div>
          <div class="form-group">
            <label for="modal-notes">备注信息</label>
            <textarea id="modal-notes" v-model="bookingForm.notes" placeholder="请输入备注信息（可选）"></textarea>
          </div>
          <div class="form-group checkbox-group">
            <input type="checkbox" id="modal-agree" v-model="bookingForm.agree" />
            <label for="modal-agree">我已阅读并同意活动的须知和隐私政策</label>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" @click="closeBookingModal">取消</button>
          <button class="btn btn-primary" @click="submitBooking" :disabled="!bookingForm.agree">提交预订</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import chaganhu1 from '@/assets/chaganhu/1.png'

const router = useRouter()
const showBackToTop = ref(false)

// 预订模态框
const showBookingModal = ref(false)

// 预订表单
const bookingForm = ref({
  name: '',
  phone: '',
  email: '',
  participants: 1,
  notes: '',
  agree: false
})

// 打开预订模态框
const openBookingModal = () => {
  showBookingModal.value = true
}

// 关闭预订模态框
const closeBookingModal = () => {
  showBookingModal.value = false
}

// 保存订单到localStorage
const saveOrder = (order) => {
  try {
    // 从localStorage读取现有订单
    const storedOrders = localStorage.getItem('orders')
    let orders = []
    if (storedOrders) {
      orders = JSON.parse(storedOrders)
    }
    
    // 添加新订单
    orders.push(order)
    
    // 保存回localStorage
    localStorage.setItem('orders', JSON.stringify(orders))
  } catch (error) {
    console.error('Error saving order:', error)
  }
}

// 提交预订
const submitBooking = () => {
  if (!bookingForm.value.agree) return
  
  // 生成订单ID
  const orderId = 'ORD' + Date.now()
  
  // 创建订单对象
  const order = {
    id: orderId,
    type: 'activity',
    item: '查干湖冬捕开网仪式',
    price: 288,
    totalPrice: 288 * bookingForm.value.participants,
    participants: bookingForm.value.participants,
    date: '2026-04-15',
    status: 'pending',
    createdAt: new Date().toISOString()
  }
  
  // 保存订单到localStorage
  saveOrder(order)
  
  // 关闭模态框
  closeBookingModal()
  
  // 跳转到我的页面
  router.push('/profile')
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
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.activity-detail {
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

/* 活动主信息 */
.activity-header h1 {
  font-size: 32px;
  font-weight: 700;
  color: var(--text-dark);
  margin-bottom: 16px;
}

.activity-tags {
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

.tag-blue {
  background-color: var(--accent-blue-light);
  color: var(--accent-blue);
}

.tag-green {
  background-color: var(--accent-green-light);
  color: var(--accent-green);
}

.activity-info {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  margin-bottom: 24px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.info-label {
  font-weight: 500;
  color: var(--text-dark);
}

.info-value {
  color: var(--text-medium);
}

.activity-images {
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

.activity-actions {
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

/* 活动介绍 */
.intro-content p {
  line-height: 1.6;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.intro-content p:last-child {
  margin-bottom: 0;
}

/* 流程安排 */
.schedule-item {
  display: flex;
  gap: 24px;
  margin-bottom: 24px;
  position: relative;
}

.schedule-item:not(:last-child)::before {
  content: '';
  position: absolute;
  left: 60px;
  top: 40px;
  bottom: -24px;
  width: 2px;
  background-color: var(--border-color);
}

.schedule-time {
  width: 120px;
  font-weight: 500;
  color: var(--text-dark);
  flex-shrink: 0;
  position: relative;
}

.schedule-time::before {
  content: '';
  position: absolute;
  left: 60px;
  top: 8px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: var(--primary-color);
  z-index: 1;
}

.schedule-activity h3 {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-dark);
}

.schedule-activity p {
  line-height: 1.5;
  color: var(--text-medium);
  margin: 0;
}

/* 报名须知 */
.notes-content ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.notes-content li {
  margin-bottom: 12px;
  position: relative;
  padding-left: 20px;
  line-height: 1.4;
  color: var(--text-medium);
}

.notes-content li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary-color);
  font-weight: bold;
}

.notes-content li:last-child {
  margin-bottom: 0;
}

/* 预订表单 */
.form-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 500;
  color: var(--text-dark);
}

.form-group input,
.form-group textarea {
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
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
  min-height: 80px;
}

.checkbox-group {
  flex-direction: row;
  align-items: flex-start;
  gap: 8px;
}

.checkbox-group input[type="checkbox"] {
  width: auto;
  margin-top: 2px;
}

.submit-booking {
  align-self: flex-start;
  margin-top: 8px;
}

/* 用户评价 */
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
  
  .activity-header h1 {
    font-size: 24px;
  }
  
  .activity-info {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .main-image {
    height: 250px;
  }
  
  .gallery {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .activity-actions {
    flex-direction: column;
  }
  
  .schedule-item {
    flex-direction: column;
    gap: 12px;
  }
  
  .schedule-time {
    width: 100%;
  }
  
  .schedule-time::before {
    left: 0;
  }
  
  .schedule-item:not(:last-child)::before {
    left: 0;
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