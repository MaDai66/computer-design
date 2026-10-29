<template>
  <div class="tour-route-detail">
    <div v-if="loading" class="loading-overlay">
      <div class="loading">加载中...</div>
    </div>
    <div v-else-if="error" class="error-message">{{ error }}</div>

    <div class="container">
      <!-- 路线主信息 -->
      <section class="route-main">
        <div class="route-header">
          <h1>{{ tour?.name || '加载中...' }}</h1>
          <div class="route-tags">
            <span v-for="tag in tour?.tags" :key="tag" class="tag" :class="getTagClass(tag)">
              {{ tag }}
            </span>
          </div>
          <div class="route-price">
            <span class="price">¥{{ tour?.price || 688 }} / 人起</span>
            <span class="duration">{{ tour?.duration || '2 天 1 晚' }}</span>
          </div>
          <div class="route-stats">
            <span class="rating">⭐⭐⭐⭐⭐ {{ tour?.rating || 4.9 }} ({{ tour?.review_count || 1280 }}条评价)</span>
            <span class="sales">已售 {{ tour?.sales_count || 2580 }} 份</span>
          </div>
        </div>
        <div class="route-images">
          <div class="main-image">
            <img :src="tour?.image" :alt="tour?.name" />
          </div>
          <div class="gallery">
            <img v-for="(img, index) in tour?.gallery" :key="index" :src="img" :alt="`图片${index + 1}`" />
          </div>
        </div>
        <div class="route-actions">
          <button class="btn btn-primary book-now" @click="openBookingModal">立即预订</button>
        </div>
      </section>

      <!-- 每日行程 -->
      <section class="daily-itinerary">
        <h2>每日行程</h2>
        <div v-for="(day, dayIndex) in tour?.days" :key="day.id" class="day-itinerary">
          <div class="day-header">
            <span class="day-number">DAY {{ dayIndex + 1 }}</span>
            <h3>{{ day.title }}</h3>
          </div>
          <div class="day-content">
            <div v-for="(slot, slotIndex) in day.time_slots" :key="slot.id" class="time-slot">
              <div class="time">{{ slot.time_range }}</div>
              <div class="activity">
                <h4>{{ slot.activity }}</h4>
                <p>{{ slot.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 非遗亮点 -->
      <section class="heritage-highlights">
        <h2>非遗亮点</h2>
        <div class="highlights-grid">
          <div v-for="(highlight, index) in tour?.highlights" :key="index" class="highlight-item">
            <div class="highlight-icon">
              <span>{{ highlight.icon }}</span>
            </div>
            <h3>{{ highlight.name }}</h3>
            <p>{{ highlight.description }}</p>
          </div>
        </div>
      </section>

      <!-- 费用说明 -->
      <section class="cost-explanation">
        <h2>费用说明</h2>
        <div class="cost-content">
          <div class="cost-includes">
            <h3>费用包含</h3>
            <ul>
              <li v-for="(item, index) in tour?.cost_includes" :key="index">{{ item }}</li>
            </ul>
          </div>
          <div class="cost-excludes">
            <h3>费用不含</h3>
            <ul>
              <li v-for="(item, index) in tour?.cost_excludes" :key="index">{{ item }}</li>
            </ul>
          </div>
          <div class="booking-notes">
            <h3>预订须知</h3>
            <ul>
              <li v-for="(note, index) in tour?.booking_notes" :key="index">{{ note }}</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- 用户评价 -->
      <section class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-header">
          <div class="rating-overall">
            <span class="rating-score">{{ tour?.rating || 4.9 }}</span>
            <span class="rating-stars">{{ '⭐'.repeat(Math.floor(tour?.rating || 4.9)) }}</span>
            <span class="rating-count">{{ tour?.review_count || 1280 }}条评价</span>
          </div>
          <div class="review-filter">
            <button class="filter-btn" :class="{ active: reviewFilter === 'all' }" @click="changeReviewFilter('all')">全部评价</button>
            <button class="filter-btn" :class="{ active: reviewFilter === 'good' }" @click="changeReviewFilter('good')">好评</button>
            <button class="filter-btn" :class="{ active: reviewFilter === 'middle' }" @click="changeReviewFilter('middle')">中评</button>
            <button class="filter-btn" :class="{ active: reviewFilter === 'bad' }" @click="changeReviewFilter('bad')">差评</button>
            <button class="filter-btn" :class="{ active: reviewFilter === 'has_image' }" @click="changeReviewFilter('has_image')">有图</button>
          </div>
        </div>
        <div class="reviews-list">
          <div v-for="review in reviews" :key="review.id" class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img :src="review.avatar || '/image/TourRouteDetail/user_avatar_1.jpeg'" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">{{ review.username }}</span>
                  <span class="review-date">{{ review.date }}</span>
                </div>
              </div>
              <div class="review-rating">
                <span>{{ '⭐'.repeat(review.rating) }}</span>
              </div>
            </div>
            <div class="review-content">
              <p v-if="review.content.length <= 100">{{ review.content }}</p>
              <p v-else>
                {{ review.content.slice(0, 100) }}...
                <span class="expand-btn" @click="toggleReviewExpand(review.id)">展开</span>
              </p>
              <p v-if="expandedReviews.includes(review.id)" class="expanded-content">
                {{ review.content }}
                <span class="expand-btn" @click="toggleReviewExpand(review.id)">收起</span>
              </p>
              <div v-if="review.images && review.images.length > 0" class="review-images">
                <img v-for="(img, index) in review.images" :key="index" :src="img" :alt="`评价图片${index + 1}`" />
              </div>
            </div>
          </div>
        </div>

      </section>

      <!-- 附加功能 -->
      <section class="additional-features">
        <h2>附加功能</h2>
        
        <!-- AI 路线定制 -->
        <div class="ai-customization">
          <h3>AI 路线定制</h3>
          <div class="ai-form">
            <p>根据您的兴趣和需求，AI 为您定制专属旅游路线</p>
            <div class="form-group">
              <label>旅行天数</label>
              <select v-model="aiForm.days">
                <option value="1">1天</option>
                <option value="2">2天</option>
                <option value="3">3天</option>
                <option value="4">4天</option>
                <option value="5+">5天以上</option>
              </select>
            </div>
            <div class="form-group">
              <label>兴趣偏好</label>
              <div class="checkbox-group">
                <label><input type="checkbox" v-model="aiForm.interests.culture" /> 文化体验</label>
                <label><input type="checkbox" v-model="aiForm.interests.nature" /> 自然风光</label>
                <label><input type="checkbox" v-model="aiForm.interests.food" /> 美食探索</label>
                <label><input type="checkbox" v-model="aiForm.interests.leisure" /> 休闲度假</label>
              </div>
            </div>
            <button class="btn btn-primary generate-route" @click="generateRoute">生成路线</button>
          </div>
          
          <!-- 生成结果 -->
          <div v-if="aiResult" class="ai-result">
            <h4>AI 定制路线</h4>
            <div class="result-content">
              <h5>{{ aiResult.title }}</h5>
              <p>{{ aiResult.description }}</p>
              <div class="route-itinerary">
                <h6>每日行程</h6>
                <div v-for="(day, index) in aiResult.itinerary" :key="index" class="day-plan">
                  <h6>Day {{ index + 1 }}</h6>
                  <ul>
                    <li v-for="(activity, actIndex) in day.activities" :key="actIndex">{{ activity }}</li>
                  </ul>
                </div>
              </div>
              <div class="route-highlights">
                <h6>路线亮点</h6>
                <ul>
                  <li v-for="(highlight, index) in aiResult.highlights" :key="index">{{ highlight }}</li>
                </ul>
              </div>
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
          <h3>预订 {{ tour?.name || '加载中...' }}</h3>
          <button class="close-btn" @click="closeBookingModal">&times;</button>
        </div>
        <div class="modal-body">
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
            <label for="booking-date">出发日期</label>
            <input type="date" id="booking-date" v-model="bookingForm.date" />
          </div>
          <div class="form-group">
            <label for="booking-guests">参与人数</label>
            <input type="number" id="booking-guests" v-model="bookingForm.guests" min="1" value="1" />
          </div>
          <div class="form-group">
            <label for="booking-notes">备注信息</label>
            <textarea id="booking-notes" v-model="bookingForm.notes" placeholder="请输入备注信息（可选）"></textarea>
          </div>
          <div class="form-group checkbox-group">
            <input type="checkbox" id="booking-agree" v-model="bookingForm.agree" />
            <label for="booking-agree">我已阅读并同意活动的须知和隐私政策</label>
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
import { useRouter, useRoute } from 'vue-router'
import { tourAPI } from '@/api/tours'
import api from '@/api/axios'

const router = useRouter()
const route = useRoute()
const showBackToTop = ref(false)

// 路线数据
const tour = ref(null)
const loading = ref(true)
const error = ref('')

// 评价数据
const reviews = ref([])
const reviewFilter = ref('all')
const currentPage = ref(1)
const totalPages = ref(1)
const expandedReviews = ref([])

// 切换评价展开/收起
const toggleReviewExpand = (reviewId) => {
  const index = expandedReviews.value.indexOf(reviewId)
  if (index > -1) {
    expandedReviews.value.splice(index, 1)
  } else {
    expandedReviews.value.push(reviewId)
  }
}

// 预订模态框
const showBookingModal = ref(false)

// 预订表单
const bookingForm = ref({
  name: '',
  phone: '',
  email: '',
  date: '',
  guests: 1,
  notes: '',
  agree: false
})

// AI路线定制表单
const aiForm = ref({
  days: '1',
  interests: {
    culture: false,
    nature: false,
    food: false,
    leisure: false
  }
})

// AI路线定制结果
const aiResult = ref(null)

// 打开预订模态框
const openBookingModal = () => {
  const user = localStorage.getItem('user')
  if (!user) {
    alert('请先登录')
    router.push('/login')
    return
  }
  showBookingModal.value = true
}

// 关闭预订模态框
const closeBookingModal = () => {
  showBookingModal.value = false
}

// 提交预订到后端
const submitBooking = async () => {
  if (!bookingForm.value.agree) {
    alert('请先同意须知和隐私政策')
    return
  }

  if (!bookingForm.value.name || !bookingForm.value.phone) {
    alert('请填写姓名和手机号码')
    return
  }

  let user = null
  try {
    user = JSON.parse(localStorage.getItem('user'))
  } catch (e) {
    console.error('解析用户数据失败:', e)
  }
  if (!user || !user.id) {
    alert('请先登录')
    router.push('/login')
    return
  }

  try {
    const tourId = parseInt(route.params.id)
    
    console.log('=== 预订信息 ===')
    console.log('tourId:', tourId)
    console.log('bookingForm:', bookingForm.value)
    console.log('localStorage中的token:', localStorage.getItem('token'))
    
    if (isNaN(tourId)) {
      alert('无法获取路线ID')
      return
    }
    
    const orderData = {
      tour_id: tourId,
      user_id: user.id,
      travel_date: bookingForm.value.date,
      guests: bookingForm.value.guests,
      contact_name: bookingForm.value.name,
      contact_phone: bookingForm.value.phone,
      notes: bookingForm.value.notes
    }
    
    console.log('发送的订单数据:', orderData)
    
    // 使用 api 发送请求，会自动携带 token
    const response = await api.post('/orders/create_tour_order/', orderData)
    
    console.log('订单创建成功，响应:', response)
    alert('预订成功！')
    closeBookingModal()
    // 跳转到我的页面
    router.push('/profile')
    
  } catch (error) {
    console.error('=== 提交预订异常 ===')
    console.error('错误对象:', error)
    console.error('响应数据:', JSON.stringify(error.response?.data, null, 2))
    console.error('响应状态:', error.response?.status)
    console.error('响应头:', error.response?.headers)
    console.error('错误消息:', error.message)

    const errorData = error.response?.data
    let errorMessage = ''
    if (errorData) {
      if (errorData.message) {
        errorMessage = errorData.message
      } else if (errorData.items && errorData.items.length > 0) {
        const itemErrors = errorData.items[0]
        errorMessage = Object.entries(itemErrors).map(([k, v]) => `${k}: ${v}`).join('; ')
      } else {
        errorMessage = JSON.stringify(errorData)
      }
    }
    alert('预订失败: ' + (errorMessage || error.message || '服务器错误'))
  }
}

// 根据路由名称获取对应的路线ID（数据库删除后新的ID）
const getTourIdFromRoute = () => {
  const routeName = route.name
  console.log('Current route name:', routeName)
  console.log('Current route params:', route.params)
  
  const tourIdMap = {
    'TourRouteDetail': '20',  // 长白山满族寻根2日游
    'TourDetailWithId': route.params.id || '20',
    'KoreanVillageTourDetail': '18',  // 朝鲜族民俗村1日游
    'ChaganLakeTourDetail': '19',     // 查干湖冬捕3日游
    'SonghuaLakeTourDetail': '17'     // 松花湖生态文化2日游
  }
  
  const tourId = tourIdMap[routeName] || '20'
  console.log('Mapped tour ID:', tourId)
  return tourId
}

// 获取路线详情
const fetchTourDetail = async () => {
  loading.value = true
  error.value = ''
  try {
    const tourId = getTourIdFromRoute()
    console.log('Fetching tour detail for ID:', tourId)
    
    const response = await tourAPI.getTourDetail(tourId)
    console.log('API Response:', response)
    console.log('API Response name:', response.name)
    console.log('API Response highlights:', response.highlights)
    
    // 处理API返回的数据结构
    tour.value = {
      ...response,
      // 处理每日行程
      days: response.days?.map(day => ({
        ...day,
        time_slots: day.time_slots?.map(slot => ({
          ...slot,
          time_range: slot.time  // 统一字段名
        })) || []
      })) || [],
      // 处理非遗亮点
      highlights: response.highlights?.map(h => ({
        ...h,
        name: h.title  // 统一字段名
      })) || [],
      // 处理费用说明
      cost_includes: response.cost_info?.includes || [],
      cost_excludes: response.cost_info?.excludes || [],
      booking_notes: response.cost_info?.booking_notes || [],
      // 处理图片
      image: getImageUrl(response.image),
      gallery: (response.gallery_base64 || []).map(img => getImageUrl(img))
    }
    
    console.log('Processed tour data:', tour.value)
    console.log('Tour name after processing:', tour.value.name)
    console.log('Tour highlights after processing:', tour.value.highlights)
  } catch (err) {
    error.value = '获取路线详情失败'
    console.error('Error fetching tour detail:', err)
  } finally {
    loading.value = false
  }
}

// 获取图片URL（处理相对路径）
const getImageUrl = (imagePath) => {
  if (!imagePath) return '/image/default-tour.jpeg'
  if (imagePath.startsWith('http')) return imagePath
  const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
  return apiBaseUrl + imagePath
}

// 获取评价列表
const fetchReviews = async () => {
  try {
    const tourId = getTourIdFromRoute()
    const response = await tourAPI.getTourReviews(tourId, {
      page: currentPage.value,
      limit: 10,
      filter: reviewFilter.value
    })
    
    // 处理评价数据
    reviews.value = (response.results || []).map(review => ({
      ...review,
      avatar: getImageUrl(review.avatar),
      images: (review.images || []).map(img => getImageUrl(img)),
      username: review.user_name  // 统一字段名
    }))
    totalPages.value = response.total_pages || 1
  } catch (err) {
    console.error('Error fetching reviews:', err)
  }
}

// 切换评价筛选
const changeReviewFilter = (filter) => {
  reviewFilter.value = filter
  currentPage.value = 1
  fetchReviews()
}

// 生成AI路线
const generateRoute = async () => {
  // 清除之前的结果，显示加载状态
  aiResult.value = {
    title: 'AI正在生成路线...',
    description: '请稍候，AI正在根据您的偏好分析最佳旅行方案...',
    itinerary: [],
    highlights: []
  }
  
  try {
    const response = await tourAPI.customizeRoute(aiForm.value)
    aiResult.value = response
  } catch (err) {
    aiResult.value = {
      title: '生成失败',
      description: 'AI路线生成失败，请重试',
      itinerary: [],
      highlights: []
    }
  }
}

const getTagClass = (tag) => {
  if (tag.includes('非遗')) return 'tag-orange'
  if (tag.includes('文化')) return 'tag-blue'
  if (tag.includes('小明')) return 'tag-green'
  return 'tag-default'
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
  // 获取路线详情
  fetchTourDetail()
  // 获取评价列表
  fetchReviews()
})</script>

<style scoped>
.tour-route-detail {
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
  padding-bottom: 12px;
  border-bottom: 2px solid var(--primary-color);
}

section h3 {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
  margin: 24px 0 16px;
}

/* 路线主信息 */
.route-header {
  margin-bottom: 24px;
}

.route-header h1 {
  font-size: 28px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 16px;
}

.route-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
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

.tag-green {
  background-color: var(--accent-green-light);
  color: var(--accent-green);
}

.route-price {
  display: flex;
  align-items: baseline;
  gap: 24px;
  margin-bottom: 12px;
}

.route-price .price {
  font-size: 24px;
  font-weight: 600;
  color: var(--accent-orange);
}

.route-price .duration {
  font-size: 16px;
  color: var(--text-medium);
}

.route-stats {
  display: flex;
  gap: 24px;
  font-size: 14px;
  color: var(--text-medium);
}

.route-images {
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

.route-actions {
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

/* 每日行程 */
.day-itinerary {
  margin-bottom: 32px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.day-header {
  background-color: var(--primary-light);
  padding: 16px 24px;
  display: flex;
  align-items: center;
  gap: 16px;
}

.day-number {
  font-size: 18px;
  font-weight: 600;
  color: var(--primary-color);
  background-color: var(--white);
  padding: 8px 16px;
  border-radius: var(--radius-md);
}

.day-header h3 {
  margin: 0;
  font-size: 18px;
}

.day-content {
  padding: 24px;
}

.time-slot {
  display: flex;
  gap: 24px;
  margin-bottom: 24px;
  position: relative;
}

.time-slot:not(:last-child)::before {
  content: '';
  position: absolute;
  left: 60px;
  top: 40px;
  bottom: -24px;
  width: 2px;
  background-color: var(--border-color);
}

.time {
  width: 120px;
  font-weight: 500;
  color: var(--text-dark);
  flex-shrink: 0;
  position: relative;
}

.time::before {
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

.activity h4 {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-dark);
}

.activity p {
  line-height: 1.5;
  color: var(--text-medium);
  margin: 0;
}

/* 非遗亮点 */
.highlights-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.highlight-item {
  background-color: var(--bg-light);
  padding: 24px;
  border-radius: var(--radius-md);
  text-align: center;
  transition: var(--transition);
}

.highlight-item:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.highlight-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.highlight-item h3 {
  margin: 0 0 12px;
  font-size: 18px;
}

.highlight-item p {
  line-height: 1.5;
  color: var(--text-medium);
  margin: 0;
}

/* 费用说明 */
.cost-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.cost-includes, .cost-excludes, .booking-notes {
  background-color: var(--bg-light);
  padding: 24px;
  border-radius: var(--radius-md);
}

.cost-includes h3, .cost-excludes h3, .booking-notes h3 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 16px;
  color: var(--text-dark);
}

.cost-includes ul, .cost-excludes ul, .booking-notes ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.cost-includes li, .cost-excludes li, .booking-notes li {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 8px;
  position: relative;
  padding-left: 20px;
}

.cost-includes li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: var(--accent-green);
  font-weight: 600;
}

.cost-excludes li::before {
  content: '✗';
  position: absolute;
  left: 0;
  color: var(--accent-red);
  font-weight: 600;
}

.booking-notes li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary-color);
  font-weight: 600;
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

.expand-btn {
  color: var(--primary-color);
  cursor: pointer;
  font-size: 14px;
  margin-left: 4px;
}

.expand-btn:hover {
  text-decoration: underline;
}

.expanded-content {
  margin-top: 8px;
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

/* 附加功能 */
.ai-customization {
  margin-bottom: 32px;
}

.ai-form {
  background-color: var(--bg-light);
  padding: 24px;
  border-radius: var(--radius-md);
}

.ai-form p {
  margin-bottom: 24px;
  color: var(--text-medium);
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--text-dark);
}

.form-group select {
  width: 100%;
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  font-size: 16px;
}

.checkbox-group {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: normal;
  cursor: pointer;
}

.generate-route {
  margin-top: 16px;
  width: 100%;
}

/* AI路线定制结果 */
.ai-result {
  margin-top: 32px;
  padding: 24px;
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
}

.ai-result h4 {
  margin-bottom: 16px;
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
}

.result-content h5 {
  font-size: 16px;
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 8px;
}

.result-content p {
  margin-bottom: 16px;
  color: var(--text-medium);
}

.route-itinerary,
.route-highlights {
  margin-bottom: 16px;
}

.route-itinerary h6,
.route-highlights h6 {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 8px;
}

.day-plan {
  margin-bottom: 12px;
}

.day-plan h7 {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-dark);
  margin-bottom: 4px;
}

.day-plan ul,
.route-highlights ul {
  list-style-type: disc;
  padding-left: 20px;
  margin: 0;
}

.day-plan li,
.route-highlights li {
  margin-bottom: 4px;
  color: var(--text-medium);
  font-size: 14px;
}

.day-plan li:last-child,
.route-highlights li:last-child {
  margin-bottom: 0;
}

.routes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 32px;
}

.route-card {
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: var(--transition);
}

.route-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.route-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.route-card h4 {
  padding: 16px;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
}

.route-card p {
  padding: 0 16px 16px;
  font-weight: 600;
  color: var(--accent-orange);
  margin-bottom: 12px;
}

.route-card .btn {
  margin: 0 16px 16px;
  width: calc(100% - 32px);
}

.recommend-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
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
  
  .route-header h1 {
    font-size: 24px;
  }
  
  .main-image {
    height: 250px;
  }
  
  .gallery {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .route-actions {
    flex-direction: column;
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
  .modal-content {
    width: 95%;
    margin: 20px;
  }
  
  .modal-header,
  .modal-body,
  .modal-footer {
    padding: 16px;
  }
  
  .route-actions {
    flex-direction: column;
  }
  
  .btn-secondary {
    flex: none;
  }
  
  .time-slot {
    flex-direction: column;
    gap: 12px;
  }
  
  .time {
    width: 100%;
  }
  
  .time::before {
    left: 0;
  }
  
  .time-slot:not(:last-child)::before {
    left: 0;
  }
  
  .highlights-grid,
  .routes-grid,
  .recommend-grid {
    grid-template-columns: 1fr;
  }
  
  .back-to-top {
    bottom: 20px;
    right: 20px;
  }
}
</style>