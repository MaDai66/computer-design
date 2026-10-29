<template>
  <div class="homestay-detail">
    <!-- 顶部图片 -->
    <div class="top-banner">
      <div class="banner-slider">
        <img :src="currentHomestay.images[0]" :alt="currentHomestay.name" />
      </div>
      <div class="banner-content">
        <h1>{{ currentHomestay.name }}</h1>
        <div class="homestay-tags">
          <span class="tag tag-green" v-if="currentHomestay.selfOperated">农家自营</span>
          <span class="tag tag-blue" v-if="currentHomestay.hot">热销</span>
          <span class="tag tag-orange">农家台屋</span>
          <span class="tag tag-red">热宿</span>
        </div>
        <div class="homestay-info">
          <span class="price">¥{{ currentHomestay.price }}/晚</span>
          <span class="location">地点：{{ currentHomestay.location }}</span>
          <span class="distance">距离景区：{{ currentHomestay.distance }}公里</span>
        </div>
      </div>
    </div>

    <div class="container">
      <!-- 房型 & 价格 -->
      <section class="room-types">
        <h2>房型 & 价格</h2>
        <div class="rooms-grid">
          <div class="room-card" v-for="room in currentHomestay.rooms" :key="room.name">
            <img :src="room.image" :alt="room.name" />
            <div class="room-content">
              <h3>{{ room.name }}</h3>
              <p class="room-desc">{{ room.description }}</p>
              <div class="room-price">
                <span class="price">¥{{ room.price }}/晚</span>
                <span class="capacity">{{ room.capacity }}</span>
              </div>
              <button class="btn btn-secondary" @click="openRoomBookingModal(room.name, room.price, room.id)">预订</button>
            </div>
          </div>
        </div>
      </section>

      <!-- 非遗体验项目 -->
      <section class="heritage-experiences">
        <h2>非遗体验项目</h2>
        <div class="experiences-list">
          <div class="experience-item" v-for="experience in currentHomestay.experiences" :key="experience.name">
            <img :src="experience.image" :alt="experience.name" />
            <div class="experience-content">
              <h3>{{ experience.name }}</h3>
              <p class="experience-desc">{{ experience.description }}</p>
              <div class="experience-info">
                <span class="duration">时长：{{ experience.duration }}</span>
                <span class="price">¥{{ experience.price }}/人</span>
              </div>
              <button class="btn btn-secondary" @click="openExperienceBookingModal(experience.name, experience.price, experience.id)">预约</button>
            </div>
          </div>
        </div>
      </section>

      <!-- 用户评价 -->
      <section class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-list">
          <div class="review-item" v-for="(review, index) in currentHomestay.reviews" :key="index">
            <div class="review-header">
              <div class="user-info">
                <img :src="review.avatar" :alt="review.user" />
                <span class="user-name">{{ review.user }}</span>
              </div>
              <div class="review-rating">
                <span v-for="i in 5" :key="i" :class="i <= review.rating ? 'star-filled' : 'star-empty'">⭐</span>
              </div>
            </div>
            <p class="review-content">{{ review.content }}</p>
            <div class="review-date">{{ review.date }}</div>
          </div>
        </div>
      </section>

      <!-- 房间预订模态框 -->
      <div v-if="showRoomBookingModal" class="modal">
        <div class="modal-content">
          <h3>预订{{ selectedRoom }} - ¥{{ selectedRoomPrice }}/晚</h3>
          <form @submit.prevent="submitRoomBooking">
            <div class="form-group">
              <label for="check-in">入住日期</label>
              <input type="date" id="check-in" v-model="roomBooking.checkIn" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="check-out">退房日期</label>
              <input type="date" id="check-out" v-model="roomBooking.checkOut" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="guests">入住人数</label>
              <input type="number" id="guests" v-model.number="roomBooking.guests" class="form-control" min="1" value="2" required />
            </div>
            <div class="form-group">
              <label for="name">联系人姓名</label>
              <input type="text" id="name" v-model="roomBooking.name" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="phone">联系电话</label>
              <input type="tel" id="phone" v-model="roomBooking.phone" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="notes">备注</label>
              <textarea id="notes" v-model="roomBooking.notes" class="form-control" rows="3"></textarea>
            </div>
            <div class="modal-actions">
              <button type="button" class="btn btn-secondary" @click="showRoomBookingModal = false">取消</button>
              <button type="submit" class="btn btn-primary">提交预订</button>
            </div>
          </form>
        </div>
      </div>

      <!-- 体验预约模态框 -->
      <div v-if="showExperienceBookingModal" class="modal">
        <div class="modal-content">
          <h3>预约{{ selectedExperience }} - ¥{{ selectedExperiencePrice }}/人</h3>
          <form @submit.prevent="submitExperienceBooking">
            <div class="form-group">
              <label for="experience-date">预约日期</label>
              <input type="date" id="experience-date" v-model="experienceBooking.date" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="experience-time">预约时间</label>
              <select id="experience-time" v-model="experienceBooking.time" class="form-control" required>
                <option value="09:00-10:30">09:00-10:30</option>
                <option value="14:00-15:30">14:00-15:30</option>
                <option value="16:00-17:30">16:00-17:30</option>
              </select>
            </div>
            <div class="form-group">
              <label for="participants">参与人数</label>
              <input type="number" id="participants" v-model.number="experienceBooking.participants" class="form-control" min="1" value="1" required />
            </div>
            <div class="form-group">
              <label for="contact-name">联系人姓名</label>
              <input type="text" id="contact-name" v-model="experienceBooking.name" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="contact-phone">联系电话</label>
              <input type="tel" id="contact-phone" v-model="experienceBooking.phone" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="experience-notes">备注</label>
              <textarea id="experience-notes" v-model="experienceBooking.notes" class="form-control" rows="3"></textarea>
            </div>
            <div class="modal-actions">
              <button type="button" class="btn btn-secondary" @click="showExperienceBookingModal = false">取消</button>
              <button type="submit" class="btn btn-primary">提交预约</button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import api from '@/api/axios'

const router = useRouter()
const route = useRoute()
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

// 加载状态
const loading = ref(true)
const error = ref('')

// 当前农家院数据
const currentHomestayData = ref({
  id: 1,
  name: '长白山脚下农家院',
  image: '/image/HomestayDetail/changbaishan_farmhouse_1.jpeg',
  images: [
    '/image/HomestayDetail/changbaishan_farmhouse_1.jpeg',
    '/image/HomestayDetail/changbaishan_farmhouse_2.jpeg',
    '/image/HomestayDetail/changbaishan_farmhouse_3.jpeg',
    '/image/HomestayDetail/changbaishan_farmhouse_4.jpeg'
  ],
  rating: 4.8,
  location: '长白山景区附近',
  distance: 5,
  hasHeritage: true,
  selfOperated: true,
  hot: true,
  description: '位于长白山脚下，环境优美，提供满族剪纸体验，正宗农家菜。',
  price: 280,
  rooms: [
    {
      name: '火炕房',
      image: '/image/HomestayDetail/room_kang.jpeg',
      description: '传统火炕，可住2-4人，独立卫浴，空调，WiFi',
      price: 280,
      capacity: '2-4人'
    },
    {
      name: '山景房',
      image: '/image/HomestayDetail/room_mountain.jpeg',
      description: '落地窗山景，可住2人，独立卫浴，空调，WiFi',
      price: 320,
      capacity: '2人'
    },
    {
      name: '家庭房',
      image: '/image/HomestayDetail/room_family.jpeg',
      description: '宽敞空间，可住4-6人，独立卫浴，空调，WiFi',
      price: 480,
      capacity: '4-6人'
    }
  ],
  experiences: [
    {
      name: '满族剪纸教学',
      image: '/image/HomestayDetail/exp_papercutting.jpeg',
      description: '由当地非遗传承人教授满族传统剪纸技艺，可带走自己的作品。',
      duration: '1.5小时',
      price: 68
    },
    {
      name: '满族火锅体验',
      image: '/image/HomestayDetail/exp_hotpot.jpeg',
      description: '品尝正宗满族火锅，了解满族饮食文化和传统烹饪方法。',
      duration: '2小时',
      price: 128
    }
  ],
  reviews: [
    {
      user: '@旅行爱好者',
      avatar: '/image/HomestayDetail/avatar_1.jpeg',
      rating: 5,
      content: '农家院环境非常好，干净整洁，老板热情好客。火炕很舒服，晚上睡得很香。早餐是正宗的农家菜，味道很棒。离长白山景区很近，交通方便。强烈推荐！',
      date: '2026-04-10'
    },
    {
      user: '@家庭出游',
      avatar: '/image/HomestayDetail/avatar_2.jpeg',
      rating: 5,
      content: '带家人来长白山旅游，选择了这家农家院。房间宽敞，设施齐全，孩子们很喜欢火炕。老板还安排了满族剪纸体验，非常有特色。下次来还会住这里。',
      date: '2026-04-08'
    },
    {
      user: '@摄影爱好者',
      avatar: '/image/HomestayDetail/avatar_3.jpeg',
      rating: 5,
      content: '农家院的位置绝佳，是拍摄长白山的好地方。房间干净舒适，老板很热情，给我们推荐了很多拍摄点。晚上在院子里还能看到星空，非常美丽。',
      date: '2026-04-05'
    }
  ]
})

// 获取图片URL
const getImageUrl = (imagePath) => {
  if (!imagePath) return '/image/HomestayDetail/default.jpg'
  if (imagePath.startsWith('http')) return imagePath
  if (imagePath.startsWith('/media')) return apiBaseUrl + imagePath
  if (imagePath.startsWith('/image')) return imagePath
  return apiBaseUrl + imagePath
}

// 获取当前农家院详情
const currentHomestay = computed(() => {
  const data = currentHomestayData.value
  const processedImages = data.images && data.images.length > 0 
    ? data.images.map(img => getImageUrl(img))
    : [getImageUrl(data.image)]
  return {
    ...data,
    image: getImageUrl(data.image),
    images: processedImages,
    rooms: data.rooms.map(room => ({
      ...room,
      image: getImageUrl(room.image)
    })),
    experiences: data.experiences.map(exp => ({
      ...exp,
      image: getImageUrl(exp.image)
    })),
    reviews: data.reviews.map(review => ({
      ...review,
      avatar: getImageUrl(review.avatar)
    }))
  }
})

// 获取农家院数据
const fetchHomestay = async () => {
  loading.value = true
  error.value = ''
  try {
    const id = parseInt(route.params.id) || 1
    const response = await axios.get(`${apiBaseUrl}/api/homestay/${id}/`)
    const data = response.data
    
    const roomsResponse = await axios.get(`${apiBaseUrl}/api/homestay/rooms/?homestay=${id}`)
    const rooms = roomsResponse.data.results || roomsResponse.data || []
    
    const experiencesResponse = await axios.get(`${apiBaseUrl}/api/homestay/experiences/?homestay=${id}`)
    const experiences = experiencesResponse.data.results || experiencesResponse.data || []
    
    const reviewsResponse = await axios.get(`${apiBaseUrl}/api/homestay/reviews/?homestay=${id}`)
    const reviews = reviewsResponse.data.results || reviewsResponse.data || []
    
    currentHomestayData.value = {
      id: data.id,
      name: data.name || '',
      image: data.image || '',
      images: data.images || [],
      rating: parseFloat(data.rating) || 0,
      location: data.location || '',
      distance: data.distance || 0,
      hasHeritage: data.has_heritage || false,
      selfOperated: data.self_operated || false,
      hot: data.hot || false,
      description: data.description || '',
      price: parseFloat(data.price) || 0,
      rooms: rooms.map(room => ({
        id: room.id || null,
        name: room.name || '',
        image: room.image || '',
        description: room.description || '',
        price: parseFloat(room.price) || 0,
        capacity: room.capacity || ''
      })),
      experiences: experiences.map(exp => ({
        id: exp.id || null,
        name: exp.name || '',
        image: exp.image || '',
        description: exp.description || '',
        duration: exp.duration || '',
        price: parseFloat(exp.price) || 0
      })),
      reviews: reviews.map(review => ({
        user: review.user_name || '',
        avatar: review.avatar || '',
        rating: review.rating || 5,
        content: review.content || '',
        date: review.date ? new Date(review.date).toISOString().split('T')[0] : new Date().toISOString().split('T')[0]
      }))
    }
  } catch (err) {
    console.error('获取农家院详情失败:', err)
    error.value = '获取农家院详情失败，使用本地数据'
  } finally {
    loading.value = false
  }
}

const showBackToTop = ref(false)

// 房间预订相关状态
const showRoomBookingModal = ref(false)
const selectedRoom = ref('')
const selectedRoomPrice = ref(0)
const selectedRoomId = ref(null)
const roomBooking = ref({
  checkIn: '',
  checkOut: '',
  guests: 2,
  name: '',
  phone: '',
  notes: ''
})

// 体验预约相关状态
const showExperienceBookingModal = ref(false)
const selectedExperience = ref('')
const selectedExperiencePrice = ref(0)
const selectedExperienceId = ref(null)
const experienceBooking = ref({
  date: '',
  time: '09:00-10:30',
  participants: 1,
  name: '',
  phone: '',
  notes: ''
})

// 打开房间预订模态框
const openRoomBookingModal = (room, price, roomId = null) => {
  selectedRoom.value = room
  selectedRoomPrice.value = price
  selectedRoomId.value = roomId
  showRoomBookingModal.value = true
}

// 打开体验预约模态框
const openExperienceBookingModal = (experience, price, experienceId = null) => {
  selectedExperience.value = experience
  selectedExperiencePrice.value = price
  selectedExperienceId.value = experienceId
  showExperienceBookingModal.value = true
}

// 提交房间预订到后端
const submitRoomBooking = async () => {
  // 检查登录状态
  let user = null
  try { user = JSON.parse(localStorage.getItem('user')) } catch (e) {}
  if (!user || !user.id) {
    alert('请先登录')
    router.push('/login')
    return
  }
  
  if (!roomBooking.value.name || !roomBooking.value.phone) {
    alert('请填写姓名和手机号码')
    return
  }
  
  if (!roomBooking.value.checkIn || !roomBooking.value.checkOut) {
    alert('请选择入住和退房日期')
    return
  }
  
  try {
    const homestayId = parseInt(route.params.id) || 1
    const checkInDate = new Date(roomBooking.value.checkIn)
    const checkOutDate = new Date(roomBooking.value.checkOut)
    const nights = Math.ceil((checkOutDate - checkInDate) / (1000 * 60 * 60 * 24))
    
    console.log('=== 房间预订信息 ===')
    console.log('homestayId:', homestayId)
    console.log('roomBooking:', roomBooking.value)
    console.log('selectedRoom:', selectedRoom.value)
    console.log('nights:', nights)
    
    const orderData = {
      homestay_id: homestayId,
      room_id: selectedRoomId.value,
      check_in: roomBooking.value.checkIn,
      check_out: roomBooking.value.checkOut,
      guests: roomBooking.value.guests || 1,
      contact_name: roomBooking.value.name,
      contact_phone: roomBooking.value.phone,
      notes: roomBooking.value.notes,
      user_id: user.id
    }

    console.log('发送的订单数据:', orderData)

    // 调用后端API创建民宿订单
    const response = await api.post('/orders/create_homestay_order/', orderData)
    
    console.log('订单创建成功，响应:', response)
    alert('预订成功！')
    
    // 关闭模态框
    showRoomBookingModal.value = false
    
    // 跳转到我的页面
    router.push('/profile')
    
  } catch (error) {
    console.error('=== 提交预订异常 ===')
    console.error('错误对象:', error)
    console.error('响应数据:', JSON.stringify(error.response?.data, null, 2))
    console.error('响应状态:', error.response?.status)

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

// 提交体验预约到后端
const submitExperienceBooking = async () => {
  // 检查登录状态
  let user = null
  try { user = JSON.parse(localStorage.getItem('user')) } catch (e) {}
  if (!user || !user.id) {
    alert('请先登录')
    router.push('/login')
    return
  }
  
  if (!experienceBooking.value.name || !experienceBooking.value.phone) {
    alert('请填写姓名和手机号码')
    return
  }
  
  if (!experienceBooking.value.date) {
    alert('请选择预约日期')
    return
  }
  
  try {
    const homestayId = parseInt(route.params.id) || 1
    
    console.log('=== 体验预约信息 ===')
    console.log('homestayId:', homestayId)
    console.log('experienceBooking:', experienceBooking.value)
    console.log('selectedExperience:', selectedExperience.value)
    console.log('selectedExperienceId:', selectedExperienceId.value)
    
    const orderData = {
      homestay_id: homestayId,
      experience_id: selectedExperienceId.value,
      date: experienceBooking.value.date,
      time: experienceBooking.value.time,
      participants: experienceBooking.value.participants || 1,
      contact_name: experienceBooking.value.name,
      contact_phone: experienceBooking.value.phone,
      notes: experienceBooking.value.notes,
      user_id: user.id
    }

    console.log('发送的订单数据:', orderData)

    // 调用后端API创建体验订单
    const response = await api.post('/orders/create_experience_order/', orderData)
    
    console.log('订单创建成功，响应:', response)
    alert('预约成功！')
    
    // 关闭模态框
    showExperienceBookingModal.value = false
    
    // 跳转到我的页面
    router.push('/profile')
    
  } catch (error) {
    console.error('=== 提交预约异常 ===')
    console.error('错误对象:', error)
    console.error('响应数据:', JSON.stringify(error.response?.data, null, 2))
    console.error('响应状态:', error.response?.status)

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
    alert('预约失败: ' + (errorMessage || error.message || '服务器错误'))
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
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
  // 获取农家院数据
  fetchHomestay()
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.homestay-detail {
  background-color: var(--bg-light);
}

.top-banner {
  position: relative;
  height: 500px;
  overflow: hidden;
}

.banner-slider {
  width: 100%;
  height: 100%;
}

.banner-slider img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.banner-content {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 40px;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  color: var(--white);
}

.banner-content h1 {
  font-size: 36px;
  font-weight: 600;
  margin-bottom: 16px;
}

.homestay-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.tag {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.tag-red {
  background-color: var(--accent-red);
  color: var(--white);
}

.tag-green {
  background-color: var(--accent-green);
  color: var(--white);
}

.tag-blue {
  background-color: var(--accent-blue);
  color: var(--white);
}

.tag-orange {
  background-color: var(--accent-orange);
  color: var(--white);
}

.homestay-info {
  display: flex;
  gap: 24px;
  font-size: 16px;
  flex-wrap: wrap;
}

.price {
  font-weight: 600;
  color: var(--accent-orange);
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

/* 房型 & 价格 */
.rooms-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.room-card {
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: var(--transition);
}

.room-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.room-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.room-content {
  padding: 20px;
}

.room-content h3 {
  margin-top: 0;
  margin-bottom: 8px;
}

.room-desc {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 16px;
  line-height: 1.5;
}

.room-price {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.capacity {
  font-size: 14px;
  color: var(--text-medium);
}

/* 非遗体验项目 */
.experiences-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.experience-item {
  display: flex;
  gap: 24px;
  padding: 20px;
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
  transition: var(--transition);
}

.experience-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}

.experience-item img {
  width: 200px;
  height: 150px;
  object-fit: cover;
  border-radius: var(--radius-md);
  flex-shrink: 0;
}

.experience-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.experience-content h3 {
  margin-top: 0;
  margin-bottom: 8px;
}

.experience-desc {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 12px;
  line-height: 1.5;
}

.experience-info {
  display: flex;
  gap: 24px;
  margin-bottom: 12px;
}

.duration {
  font-size: 14px;
  color: var(--text-medium);
}

/* 设施介绍 */
.facilities-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.facility-item {
  background-color: var(--bg-light);
  padding: 24px;
  border-radius: var(--radius-md);
  text-align: center;
  transition: var(--transition);
}

.facility-item:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.facility-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.facility-item h3 {
  margin-top: 0;
  margin-bottom: 16px;
}

.facility-item ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.facility-item li {
  margin-bottom: 8px;
  font-size: 14px;
  color: var(--text-medium);
}

/* 用户评价 */
.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.review-item {
  padding: 20px;
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-info img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.user-name {
  font-weight: 500;
}

.review-rating {
  font-size: 14px;
}

.review-content {
  line-height: 1.5;
  margin-bottom: 12px;
}

.review-date {
  font-size: 12px;
  color: var(--text-light);
}

/* 入住日历 */
.calendar-container {
  background-color: var(--bg-light);
  padding: 24px;
  border-radius: var(--radius-md);
}

.calendar-month h3 {
  margin-top: 0;
  margin-bottom: 16px;
  text-align: center;
}

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 8px;
}

.calendar-header {
  font-weight: 600;
  text-align: center;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border-color);
}

.calendar-days {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 8px;
}

.day {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  cursor: pointer;
  transition: var(--transition);
}

.day:hover:not(.disabled) {
  background-color: var(--primary-light);
}

.day.available {
  background-color: var(--accent-green-light);
  color: var(--accent-green);
  font-weight: 600;
}

.day.disabled {
  color: var(--text-light);
  cursor: not-allowed;
}

/* 预约表单 */
.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
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

.form-control {
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  font-size: 16px;
}

.form-control:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(42, 157, 143, 0.2);
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
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 32px;
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-hover);
}

.modal-content h3 {
  margin-top: 0;
  margin-bottom: 24px;
  color: var(--text-dark);
  font-size: 20px;
  font-weight: 600;
}

.modal-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 24px;
}

/* 响应式 */
@media (max-width: 768px) {
  .top-banner {
    height: 300px;
  }
  
  .banner-content {
    padding: 24px;
  }
  
  .banner-content h1 {
    font-size: 24px;
  }
  
  .homestay-info {
    flex-direction: column;
    gap: 8px;
  }
  
  .experience-item {
    flex-direction: column;
  }
  
  .experience-item img {
    width: 100%;
    height: 200px;
  }
  
  section {
    padding: 20px;
  }
  
  .container {
    padding: 24px 16px;
  }
  
  .back-to-top {
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
  
  .modal-content {
    width: 95%;
    padding: 24px;
  }
  
  .modal-actions {
    flex-direction: column;
  }
  
  .modal-actions .btn {
    width: 100%;
  }
}
</style>