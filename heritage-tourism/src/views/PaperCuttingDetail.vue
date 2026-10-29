<template>
  <div class="activity-detail">
    <!-- 顶部导航 -->
    <div class="top-nav">
      <div class="container">
        <div class="breadcrumb">
          <router-link to="/">首页</router-link>
          <span>/</span>
          <router-link to="/heritage">遗珍</router-link>
          <span>/</span>
          <span class="current">满族剪纸艺术工作坊</span>
        </div>
      </div>
    </div>

    <div class="container">
      <!-- 活动主信息 -->
      <section class="activity-main">
        <div class="activity-header">
          <h1>满族剪纸艺术工作坊</h1>
          <div class="activity-tags">
            <router-link to="/heritage/calendar?date=2026-04-25" class="tag tag-orange">25 4月</router-link>
            <span class="tag tag-blue">非遗活动</span>
            <span class="tag tag-green">剪纸艺术</span>
          </div>
          <div class="activity-info">
            <div class="info-item">
              <span class="info-label">活动时间</span>
              <span class="info-value">2026年4月25日 14:00-16:30</span>
            </div>
            <div class="info-item">
              <span class="info-label">活动地点</span>
              <span class="info-value">吉林市满族文化中心</span>
            </div>
            <div class="info-item">
              <span class="info-label">活动费用</span>
              <span class="info-value">¥128/人</span>
            </div>
            <div class="info-item">
              <span class="info-label">剩余名额</span>
              <span class="info-value">15/30</span>
            </div>
          </div>
        </div>
        <div class="activity-images">
          <div class="main-image">
            <img :src="papercutting1" alt="满族剪纸艺术工作坊" />
          </div>
          <div class="gallery">
            <img :src="papercutting2" alt="剪纸工具和材料" />
            <img :src="papercutting3" alt="满族传统剪纸图案" />
            <img :src="papercutting4" alt="工作坊学习场景" />
            <img :src="papercutting5" alt="完成的剪纸作品" />
            <img :src="papercutting6" alt="剪纸创作过程" />
            <img :src="papercutting7" alt="传统剪纸工具" />
          </div>
        </div>
        <div class="activity-actions">
          <button class="btn btn-primary book-now">立即预订</button>
          <button class="btn btn-secondary share">分享</button>
          <button class="btn btn-secondary favorite">收藏</button>
        </div>
      </section>

      <!-- 活动介绍 -->
      <section class="activity-intro">
        <h2>活动介绍</h2>
        <div class="intro-content">
          <p>满族剪纸是国家级非物质文化遗产，有着悠久的历史和独特的艺术风格。本次工作坊邀请了满族剪纸传承人，带领大家了解剪纸的历史文化，学习基本的剪纸技巧，亲手制作精美的剪纸作品。</p>
          <p>满族剪纸以其独特的图案和精湛的技艺闻名，作品题材丰富，包括花鸟鱼虫、神话传说、日常生活等。通过本次工作坊，您将了解满族剪纸的发展历程、艺术特点和文化内涵，同时掌握基本的剪纸技巧。</p>
          <p>参加本次活动，您将有机会：</p>
          <ul>
            <li>了解满族剪纸的历史文化和艺术特点</li>
            <li>学习基本的剪纸技巧和方法</li>
            <li>亲手制作精美的剪纸作品</li>
            <li>与传承人面对面交流，了解剪纸背后的故事</li>
            <li>获得活动纪念证书和剪纸材料包</li>
          </ul>
        </div>
      </section>

      <!-- 流程安排 -->
      <section class="activity-schedule">
        <h2>流程安排</h2>
        <div class="schedule-timeline">
          <div class="schedule-item">
            <div class="schedule-time">13:30-14:00</div>
            <div class="schedule-content">
              <h3>集合签到</h3>
              <p>在吉林市满族文化中心门口集合，领取活动材料包</p>
            </div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">14:00-14:30</div>
            <div class="schedule-content">
              <h3>剪纸文化讲座</h3>
              <p>了解满族剪纸的历史发展、艺术特点和文化内涵</p>
            </div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">14:30-15:00</div>
            <div class="schedule-content">
              <h3>技巧讲解</h3>
              <p>传承人讲解基本的剪纸技巧和方法</p>
            </div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">15:00-16:00</div>
            <div class="schedule-content">
              <h3>实践创作</h3>
              <p>在传承人指导下，亲手制作剪纸作品</p>
            </div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">16:00-16:30</div>
            <div class="schedule-content">
              <h3>作品展示与交流</h3>
              <p>展示个人作品，与传承人及其他参与者交流</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 报名须知 -->
      <section class="activity-notes">
        <h2>报名须知</h2>
        <div class="notes-content">
          <div class="notes-section">
            <h3>费用说明</h3>
            <ul>
              <li>包含活动全程参与费用</li>
              <li>包含剪纸材料包（剪刀、彩纸、模板等）</li>
              <li>包含活动纪念证书</li>
              <li>包含茶点和饮品</li>
              <li>不含交通费用</li>
            </ul>
          </div>
          <div class="notes-section">
            <h3>注意事项</h3>
            <ul>
              <li>活动适合8岁以上人员参加</li>
              <li>请自带水杯</li>
              <li>活动过程中请注意安全，尤其是使用剪刀时</li>
              <li>请遵守现场秩序，服从工作人员安排</li>
              <li>请携带身份证等有效证件</li>
            </ul>
          </div>
          <div class="notes-section">
            <h3>退改政策</h3>
            <ul>
              <li>活动前7天可全额退款</li>
              <li>活动前3-6天退款50%</li>
              <li>活动前2天内不退款</li>
              <li>如因天气等不可抗力因素取消活动，将全额退款</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- 预订表单 -->
      <section class="booking-form">
        <h2>预订表单</h2>
        <form class="form-content" @submit="saveOrder">
          <div class="form-group">
            <label for="name">姓名</label>
            <input type="text" id="name" v-model="formData.name" placeholder="请输入您的姓名" required />
          </div>
          <div class="form-group">
            <label for="phone">手机号码</label>
            <input type="tel" id="phone" v-model="formData.phone" placeholder="请输入您的手机号码" required />
          </div>
          <div class="form-group">
            <label for="email">电子邮箱</label>
            <input type="email" id="email" v-model="formData.email" placeholder="请输入您的电子邮箱" />
          </div>
          <div class="form-group">
            <label for="date">选择日期</label>
            <input type="date" id="date" v-model="formData.date" value="2026-04-25" min="2026-04-25" max="2026-04-25" required />
          </div>
          <div class="form-group">
            <label for="count">参与人数</label>
            <input type="number" id="count" v-model="formData.count" min="1" max="5" value="1" required />
          </div>
          <div class="form-group">
            <label for="remarks">备注信息</label>
            <textarea id="remarks" v-model="formData.remarks" placeholder="请输入备注信息（可选）" rows="3"></textarea>
          </div>
          <div class="form-agreement">
            <input type="checkbox" id="agreement" required />
            <label for="agreement">我已阅读并同意<a href="#">活动须知</a>和<a href="#">隐私政策</a></label>
          </div>
          <button type="submit" class="btn btn-primary submit-btn">提交预订</button>
        </form>
      </section>

      <!-- 用户评价 -->
      <section class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-header">
          <div class="rating-overall">
            <span class="rating-score">4.8</span>
            <span class="rating-stars">⭐⭐⭐⭐⭐</span>
            <span class="rating-count">328条评价</span>
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
                <img src="/image/PaperCuttingDetail/user_avatar_1.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@艺术爱好者</span>
                  <span class="review-date">2025-12-20</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>非常棒的剪纸工作坊！传承人讲解得很详细，从剪纸的历史文化到具体的制作技巧，都讲得很清楚。材料包很齐全，剪刀质量也很好。我第一次尝试剪纸，在老师的指导下，居然做出了像样的作品，非常有成就感。强烈推荐给喜欢传统文化的朋友！</p>
              <div class="review-images">
                <img :src="papercutting4" alt="参与者与作品" />
                <img :src="papercutting5" alt="剪纸作品细节" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="/image/PaperCuttingDetail/user_avatar_2.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@文化探索者</span>
                  <span class="review-date">2025-12-15</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>这次工作坊让我对满族剪纸有了更深入的了解。传承人不仅教授了剪纸技巧，还分享了很多剪纸背后的文化故事，让我感受到了传统工艺的魅力。活动组织得很有序，环境也很舒适。我带孩子一起参加的，孩子也很喜欢，回家后还一直练习剪纸。</p>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="/image/PaperCuttingDetail/user_avatar_3.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@手作达人</span>
                  <span class="review-date">2025-12-10</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>作为一个手作爱好者，我参加过很多工作坊，这次的剪纸工作坊是最棒的之一。传承人技艺精湛，讲解耐心，材料质量也很好。我学到了很多剪纸技巧，回家后又买了更多材料继续练习。非常感谢这次活动，让我发现了剪纸的乐趣！</p>
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
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import papercutting1 from '@/assets/papercutting/1.png'
import papercutting2 from '@/assets/papercutting/2.png'
import papercutting3 from '@/assets/papercutting/3.png'
import papercutting4 from '@/assets/papercutting/4.png'
import papercutting5 from '@/assets/papercutting/5.png'
import papercutting6 from '@/assets/papercutting/6.png'
import papercutting7 from '@/assets/papercutting/7.png'

const showBackToTop = ref(false)
const router = useRouter()

// 表单数据
const formData = ref({
  name: '',
  phone: '',
  email: '',
  date: '2026-04-25',
  count: 1,
  remarks: ''
})

// 保存订单到localStorage
const saveOrder = (e) => {
  e.preventDefault()
  
  // 生成订单ID
  const orderId = '2026' + Date.now().toString().slice(-8)
  
  // 计算总价
  const totalPrice = 128 * formData.value.count
  
  // 订单数据
  const order = {
    orderId,
    title: '满族剪纸艺术工作坊',
    image: papercutting1,
    date: formData.value.date + ' 14:00-16:00',
    price: '¥128/人',
    quantity: formData.value.count,
    totalPrice,
    status: '待体验',
    createdAt: new Date().toISOString()
  }
  
  // 从localStorage读取现有订单
  let orders = []
  try {
    const storedOrders = localStorage.getItem('userOrders')
    if (storedOrders) {
      orders = JSON.parse(storedOrders)
    }
  } catch (error) {
    console.error('Error loading orders:', error)
  }
  
  // 添加新订单
  orders.unshift(order)
  
  // 保存回localStorage
  try {
    localStorage.setItem('userOrders', JSON.stringify(orders))
    alert('订单提交成功！')
    // 跳转到个人中心
    router.push('/profile')
  } catch (error) {
    console.error('Error saving order:', error)
    alert('订单提交失败，请重试')
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

.top-nav {
  background-color: var(--white);
  border-bottom: 1px solid var(--border-color);
  padding: 16px 0;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
}

.breadcrumb a {
  color: var(--text-medium);
  text-decoration: none;
  transition: var(--transition);
}

.breadcrumb a:hover {
  color: var(--primary-color);
}

.breadcrumb .current {
  color: var(--text-dark);
  font-weight: 500;
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
  padding-bottom: 12px;
  border-bottom: 2px solid var(--primary-color);
}

section h3 {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
  margin: 24px 0 16px;
}

/* 活动主信息 */
.activity-header {
  margin-bottom: 24px;
}

.activity-header h1 {
  font-size: 28px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 16px;
}

.activity-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}

.tag {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  text-decoration: none;
  transition: var(--transition);
}

.tag-orange {
  background-color: var(--accent-orange-light);
  color: var(--accent-orange);
}

.tag-orange:hover {
  background-color: var(--accent-orange);
  color: var(--white);
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
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.info-label {
  font-size: 14px;
  color: var(--text-medium);
}

.info-value {
  font-size: 16px;
  font-weight: 500;
  color: var(--text-dark);
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
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.gallery img {
  width: 100%;
  height: 180px;
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
  flex: 1;
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
  flex: 0 0 120px;
}

.btn-secondary:hover {
  background-color: var(--primary-color);
  color: var(--white);
}

/* 活动介绍 */
.intro-content p {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.intro-content ul {
  list-style: none;
  padding: 0;
  margin: 16px 0;
}

.intro-content li {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 8px;
  position: relative;
  padding-left: 20px;
}

.intro-content li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary-color);
  font-weight: 600;
}

/* 流程安排 */
.schedule-timeline {
  position: relative;
  padding-left: 120px;
}

.schedule-timeline::before {
  content: '';
  position: absolute;
  left: 60px;
  top: 0;
  bottom: 0;
  width: 2px;
  background-color: var(--border-color);
}

.schedule-item {
  position: relative;
  margin-bottom: 32px;
}

.schedule-item::before {
  content: '';
  position: absolute;
  left: -120px;
  top: 8px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: var(--primary-color);
  z-index: 1;
}

.schedule-time {
  position: absolute;
  left: -120px;
  top: 0;
  width: 100px;
  font-weight: 500;
  color: var(--text-dark);
}

.schedule-content h3 {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-dark);
}

.schedule-content p {
  line-height: 1.5;
  color: var(--text-medium);
  margin: 0;
}

/* 报名须知 */
.notes-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.notes-section {
  background-color: var(--bg-light);
  padding: 24px;
  border-radius: var(--radius-md);
}

.notes-section h3 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 16px;
  color: var(--text-dark);
}

.notes-section ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.notes-section li {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 8px;
  position: relative;
  padding-left: 20px;
}

.notes-section li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary-color);
  font-weight: 600;
}

/* 预订表单 */
.form-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
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
  outline: none;
  transition: var(--transition);
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px var(--primary-light);
}

.form-agreement {
  grid-column: 1 / -1;
  display: flex;
  align-items: flex-start;
  gap: 8px;
  margin-top: 8px;
}

.form-agreement input {
  margin-top: 4px;
}

.form-agreement label {
  font-size: 14px;
  color: var(--text-medium);
}

.form-agreement a {
  color: var(--primary-color);
  text-decoration: none;
}

.form-agreement a:hover {
  text-decoration: underline;
}

.submit-btn {
  grid-column: 1 / -1;
  margin-top: 16px;
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
  
  .activity-header h1 {
    font-size: 24px;
  }
  
  .activity-info {
    grid-template-columns: 1fr;
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
  
  .btn-secondary {
    flex: none;
  }
  
  .schedule-timeline {
    padding-left: 80px;
  }
  
  .schedule-timeline::before {
    left: 40px;
  }
  
  .schedule-item::before {
    left: -80px;
  }
  
  .schedule-time {
    left: -80px;
    width: 60px;
    font-size: 14px;
  }
  
  .form-content {
    grid-template-columns: 1fr;
  }
  
  .reviews-header {
    flex-direction: column;
    align-items: flex-start;
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