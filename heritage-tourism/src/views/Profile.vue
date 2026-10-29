<template>
  <div class="profile">
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1>个人中心</h1>
        <p>我的吉韵遗风之旅</p>
      </div>
    </section>

    <!-- 用户信息 -->
    <section class="user-info">
      <div class="container">
        <div class="user-card">
          <div class="user-avatar">
            <img :src="getAvatarUrl(user.avatar)" alt="用户头像" />
          </div>
          <div class="user-details">
            <div class="user-header">
              <h3>{{ user.nickname || user.username || '未知旅行者' }}</h3>
              <button class="btn btn-secondary edit-profile-btn" @click="showEditProfileModal = true">编辑资料</button>
            </div>
            <p class="user-level">会员等级：非遗行者</p>
            <div class="user-stats">
              <div class="stat-item">
                <span class="stat-number">12</span>
                <span class="stat-label">已体验</span>
              </div>
              <div class="stat-item">
                <span class="stat-number">8</span>
                <span class="stat-label">收藏</span>
              </div>
              <div class="stat-item">
                <span class="stat-number">5</span>
                <span class="stat-label">发布</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 我的订单 -->
    <section class="orders-section">
      <div class="container">
        <h2>我的订单</h2>
        <div class="order-tabs">
          <button 
            class="order-tab" 
            :class="{ active: activeOrderTab === 'all' }"
            @click="switchOrderTab('all')"
          >全部</button>
          <button 
            class="order-tab" 
            :class="{ active: activeOrderTab === 'pending' }"
            @click="switchOrderTab('pending')"
          >待付款</button>
          <button 
            class="order-tab" 
            :class="{ active: activeOrderTab === 'pending_experience' }"
            @click="switchOrderTab('pending_experience')"
          >待体验</button>
          <button 
            class="order-tab" 
            :class="{ active: activeOrderTab === 'pending_review' }"
            @click="switchOrderTab('pending_review')"
          >待评价</button>
          <button 
            class="order-tab" 
            :class="{ active: activeOrderTab === 'after_sale' }"
            @click="switchOrderTab('after_sale')"
          >售后</button>
        </div>
        <div class="order-list">
          <div v-if="filteredOrders.length === 0" class="empty-orders">
            <p>暂无订单</p>
            <router-link to="/" class="btn btn-primary">去浏览</router-link>
          </div>
          <div v-else v-for="order in filteredOrders" :key="order.id" class="order-card">
            <div class="order-header">
              <span class="order-id">订单号：{{ order.id }}</span>
              <span class="order-status" :class="order.status">{{ order.statusText }}</span>
            </div>
            <div class="order-content">
              <img :src="getOrderImage(order.item, order.image)" :alt="order.item" />
              <div class="order-info">
                <div class="order-type">{{ order.typeText }}</div>
                <h4>{{ order.item }}</h4>
                <p class="order-date">
                  {{ order.checkIn ? `入住：${order.checkIn} 退房：${order.checkOut}` : 
                     order.date ? `预约：${order.date} ${order.time}` : 
                     order.spec ? `规格：${order.spec.type} - ${order.spec.theme}` : '' }}
                </p>
                <p v-if="order.createdAt" class="order-create-time">下单时间：{{ order.createdAt }}</p>
                <div class="order-price">
                  <span>¥{{ order.price }} × {{ order.quantity || order.guests || order.participants || 1 }}</span>
                  <span class="total-price">¥{{ order.totalPrice }}</span>
                </div>
              </div>
            </div>
            <div class="order-footer">
              <button class="btn btn-secondary">再次预订</button>
              <button class="btn btn-primary" :disabled="order.status === 'completed'">评价</button>
              <button class="btn btn-danger" @click="confirmDeleteOrder(order.dbId || order.id)">删除</button>
            </div>
          </div>
        </div>
      </div>
    </section>



    <!-- 发布内容 -->
    <section class="posts-section">
      <div class="container">
        <h2>我的发布</h2>
        <div class="posts-list">
          <div v-if="posts.length === 0" class="empty-posts">
            <p>暂无发布内容</p>
            <button class="btn btn-primary" @click="showAddPostModal = true">发布新内容</button>
          </div>
          <div v-else v-for="post in posts" :key="post.id" class="post-card">
            <img :src="post.image" :alt="post.title" />
            <div class="post-info">
              <h4>{{ post.title }}</h4>
              <p>{{ post.content }}</p>
              <div class="post-stats">
                <span>❤️ {{ post.likes }}</span>
                <span>💬 {{ post.comments }}</span>
              </div>
              <div class="post-actions">
                <button class="action-btn" @click="editPost(post)">编辑</button>
                <button class="action-btn delete-btn" @click="confirmDelete(post.id)">删除</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 编辑/添加发布模态框 -->
    <div v-if="showPostModal" class="modal-overlay" @click="closePostModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>{{ editingPost ? '编辑发布' : '发布新内容' }}</h3>
          <button class="close-btn" @click="closePostModal">&times;</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="savePost">
            <div class="form-group">
              <label for="post-title">标题</label>
              <input type="text" id="post-title" v-model="postForm.title" placeholder="请输入标题" required />
            </div>
            <div class="form-group">
              <label for="post-content">内容</label>
              <textarea id="post-content" v-model="postForm.content" placeholder="请输入内容" rows="4" required></textarea>
            </div>
            <div class="form-group">
              <label for="post-image">图片</label>
              <input type="file" id="post-image" accept="image/*" @change="handleImageUpload" />
              <div v-if="postForm.image" class="image-preview">
                <img :src="postForm.image" alt="预览" />
                <button type="button" class="remove-image" @click="removeImage">移除</button>
              </div>
            </div>
            <div class="form-actions">
              <button type="button" class="btn btn-secondary" @click="closePostModal">取消</button>
              <button type="submit" class="btn btn-primary">保存</button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- 删除确认模态框 -->
    <div v-if="showDeleteModal" class="modal-overlay" @click="closeDeleteModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>确认删除</h3>
          <button class="close-btn" @click="closeDeleteModal">&times;</button>
        </div>
        <div class="modal-body">
          <p>确定要删除这篇发布吗？此操作不可撤销。</p>
          <div class="form-actions">
            <button class="btn btn-secondary" @click="closeDeleteModal">取消</button>
            <button class="btn btn-danger" @click="deletePost">删除</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 订单删除确认模态框 -->
    <div v-if="showOrderDeleteModal" class="modal-overlay" @click="closeOrderDeleteModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>确认删除订单</h3>
          <button class="close-btn" @click="closeOrderDeleteModal">&times;</button>
        </div>
        <div class="modal-body">
          <p>确定要删除这个订单吗？此操作不可撤销。</p>
          <div class="form-actions">
            <button class="btn btn-secondary" @click="closeOrderDeleteModal">取消</button>
            <button class="btn btn-danger" @click="deleteOrder">删除</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 编辑个人资料模态框 -->
    <div v-if="showEditProfileModal" class="modal-overlay" @click="closeEditProfileModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>编辑个人资料</h3>
          <button class="close-btn" @click="closeEditProfileModal">&times;</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="saveProfile">
            <div class="form-group">
              <label for="edit-nickname">昵称</label>
              <input type="text" id="edit-nickname" v-model="profileForm.nickname" placeholder="请输入昵称" />
            </div>
            <div class="form-group">
              <label for="edit-email">邮箱</label>
              <input type="email" id="edit-email" v-model="profileForm.email" placeholder="请输入邮箱" />
            </div>
            <div class="form-group">
              <label for="edit-phone">电话</label>
              <input type="tel" id="edit-phone" v-model="profileForm.phone" placeholder="请输入电话" />
            </div>
            <div class="form-group">
              <label for="edit-bio">个人简介</label>
              <textarea id="edit-bio" v-model="profileForm.bio" placeholder="请输入个人简介" rows="4"></textarea>
            </div>
            <div class="form-group">
              <label for="edit-avatar">头像</label>
              <input type="file" id="edit-avatar" accept="image/*" @change="handleAvatarUpload" />
              <div v-if="profileForm.avatar" class="image-preview">
                <img :src="profileForm.avatar" alt="预览" />
                <button type="button" class="remove-image" @click="removeAvatar">移除</button>
              </div>
            </div>
            <div class="form-actions">
              <button type="button" class="btn btn-secondary" @click="closeEditProfileModal">取消</button>
              <button type="submit" class="btn btn-primary" :disabled="loading">
                {{ loading ? '保存中...' : '保存' }}
              </button>
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
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { userAPI } from '../api/users'
import orderAPI from '../api/orders'
import api from '../api/axios'

const route = useRoute()

const showBackToTop = ref(false)
const orders = ref([])
const posts = ref([])
const showPostModal = ref(false)
const showAddPostModal = ref(false)
const showDeleteModal = ref(false)
const showEditProfileModal = ref(false)
const showOrderDeleteModal = ref(false)
const editingPost = ref(null)
const postForm = ref({
  title: '',
  content: '',
  image: ''
})
const postToDelete = ref(null)
const orderToDelete = ref(null)
const activeOrderTab = ref('all')
const user = ref({
  username: '',
  avatar: '',
  email: '',
  phone: '',
  bio: ''
})
const profileForm = ref({
  nickname: '',
  email: '',
  phone: '',
  bio: '',
  avatar: ''
})
const loading = ref(false)
const originalUser = ref({}) // 保存打开模态框时的原始用户数据，用于比较变更

// 切换订单标签
const switchOrderTab = (tab) => {
  activeOrderTab.value = tab
}

// 根据标签筛选订单
const filteredOrders = computed(() => {
  if (activeOrderTab.value === 'all') {
    return orders.value
  }
  
  const statusMap = {
    'pending': ['pending'],           // 待付款
    'pending_experience': ['confirmed'], // 待体验（已确认但未完成）
    'pending_review': ['completed'],     // 待评价（已完成）
    'after_sale': ['cancelled', 'refunded'] // 售后（已取消、已退款）
  }
  
  const statuses = statusMap[activeOrderTab.value] || []
  return orders.value.filter(order => statuses.includes(order.status))
})

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

// 获取头像URL
const getAvatarUrl = (avatar) => {
  if (!avatar) {
    return '/image/Profile/user_avatar_default.jpeg'
  }
  // 如果已经是完整URL，直接返回
  if (avatar.startsWith('http://') || avatar.startsWith('https://')) {
    return avatar
  }
  // 后端返回的头像路径可能是：
  // - /media/avatars/xxx.jpg（完整相对路径）
  // - media/avatars/xxx.jpg（没有开头斜杠）
  // - avatars/xxx.jpg（只有文件名）
  // 统一处理：移除可能的 /media/ 或 media/ 前缀，然后拼接完整URL
  const cleanPath = avatar.replace(/^\/?media\//i, '')
  return `${apiBaseUrl}/media/${cleanPath}`
}

// 根据订单item名称获取对应的图片URL
const getOrderImage = (item, imagePath) => {
  console.log('获取订单图片:', item, imagePath)
  // 优先使用后端返回的图片路径
  if (imagePath && imagePath !== '') {
    const fullPath = imagePath.startsWith('http') ? imagePath : apiBaseUrl + imagePath
    return fullPath
  }
  
  // 本地映射表作为 fallback
  const imageMap = {
    '满族剪纸艺术套装': '/image/Profile/order_papercutting.jpeg',
    '长白山天然蜂蜜': '/image/Profile/order_honey.jpeg',
    '长白山蜂蜜': '/image/Profile/order_honey.jpeg',
    '长白山野生人参': '/image/Profile/order_ginseng.jpeg',
    '朝鲜族传统打糕': '/image/Profile/order_ricecake.jpeg',
    '查干湖有机鱼': '/image/Profile/order_fish.jpeg',
    '松花湖咸鸭蛋': '/image/Profile/order_eggs.jpeg',
    '吉林玉米糁': '/image/Profile/order_corn.jpeg',
    '朝鲜族泡菜': '/image/Profile/order_kimchi.jpeg',
    '吉林长白山旅游文创礼盒': '/image/Profile/order_giftbox.jpeg',
    '查干湖冬捕纪念套装': '/image/Profile/order_winterfishing.jpeg',
    '松花湖风光摄影集': '/image/Profile/order_album.jpeg',
    '火炕房': '/image/Profile/order_kang.jpeg',
    '松花湖生态2日游': '/image/Profile/order_tour1.jpeg',
    '长白山深度3日游': '/image/Profile/order_tour2.jpeg',
    '高句丽古迹探秘': '/image/Profile/order_tour3.jpeg',
    '查干湖冬捕之旅': '/image/Profile/order_tour4.jpeg'
  }
  const imageUrl = imageMap[item] || '/image/Profile/order_default.jpeg'
  console.log('图片URL:', imageUrl)
  return imageUrl
}

// 从后端获取订单数据
const loadOrders = async () => {
  try {
    // 检查用户是否登录
    let user = null
    try { user = JSON.parse(localStorage.getItem('user')) } catch (e) {}
    if (!user || !user.id) {
      orders.value = []
      return
    }

    const response = await orderAPI.getMyOrders({ user_id: user.id })
    console.log('获取订单成功:', response)
    
    // 处理后端返回的订单数据
    let orderList = []
    
    const statusMap = {
      'pending': '待付款',
      'paid': '已付款',
      'confirmed': '已确认',
      'completed': '已完成',
      'cancelled': '已取消',
      'refunded': '已退款'
    }
    const typeMap = {
      'tour': '旅游路线',
      'homestay': '民宿预订',
      'experience': '体验项目',
      'product': '商品订单'
    }
    
    let rawOrders = []
    if (response.results && Array.isArray(response.results)) {
      rawOrders = response.results
    } else if (response.value && Array.isArray(response.value)) {
      rawOrders = response.value
    } else if (response.orders && Array.isArray(response.orders)) {
      rawOrders = response.orders
    } else if (Array.isArray(response)) {
      rawOrders = response
    }
    
    orderList = rawOrders.map(order => {
      return {
        id: order.order_id || order.id,
        dbId: order.id,
        item: order.first_item_name || order.item || '未知商品',
        image: order.first_item_image || '',
        price: parseFloat(order.total_price) || parseFloat(order.amount) || 0,
        totalPrice: parseFloat(order.total_price) || parseFloat(order.amount) || 0,
        quantity: order.guests || order.items_count || order.quantity || 1,
        status: order.status,
        statusText: statusMap[order.status] || order.status_display || order.status,
        type: order.type,
        typeText: typeMap[order.type] || order.type,
        checkIn: order.check_in,
        checkOut: order.check_out,
        date: order.travel_date || order.date,
        time: order.time || '',
        spec: order.spec || null,
        createdAt: order.created_at || order.createdAt
      }
    })
    
    orders.value = orderList
    console.log('订单数据:', orders.value)
    
    // 将订单数据保存到localStorage作为备份
    try {
      localStorage.setItem('orders', JSON.stringify(orderList))
    } catch (localStorageError) {
      console.error('保存订单到localStorage失败:', localStorageError)
    }
    
  } catch (error) {
    console.error('Error loading orders:', error)
    // 出错时尝试从localStorage读取备份数据
    try {
      const storedOrders = localStorage.getItem('orders')
      if (storedOrders) {
        orders.value = JSON.parse(storedOrders)
      } else {
        orders.value = []
      }
    } catch (localStorageError) {
      orders.value = []
    }
  }
}

// 从localStorage读取发布数据
const loadPosts = () => {
  try {
    const storedPosts = localStorage.getItem('posts')
    if (storedPosts) {
      posts.value = JSON.parse(storedPosts)
    } else {
      // 默认数据
      posts.value = [
        {
          id: 1,
          title: '长白山之旅',
          content: '太美了！长白山的雪景令人震撼，非遗体验也很有趣。',
          image: '/image/Profile/post_default.jpeg',
          likes: 128,
          comments: 32
        }
      ]
      savePosts()
    }
  } catch (error) {
    console.error('Error loading posts:', error)
    posts.value = []
  }
}

// 保存发布数据到localStorage
const savePosts = () => {
  try {
    localStorage.setItem('posts', JSON.stringify(posts.value))
  } catch (error) {
    console.error('Error saving posts:', error)
  }
}

// 打开添加发布模态框
const openAddPostModal = () => {
  editingPost.value = null
  postForm.value = {
    title: '',
    content: '',
    image: ''
  }
  showPostModal.value = true
}

// 编辑发布
const editPost = (post) => {
  editingPost.value = post
  postForm.value = {
    title: post.title,
    content: post.content,
    image: post.image
  }
  showPostModal.value = true
}

// 保存发布
const savePost = () => {
  if (editingPost.value) {
    // 更新现有发布
    const index = posts.value.findIndex(p => p.id === editingPost.value.id)
    if (index !== -1) {
      posts.value[index] = {
        ...posts.value[index],
        title: postForm.value.title,
        content: postForm.value.content,
        image: postForm.value.image
      }
    }
  } else {
    // 添加新发布
    const newPost = {
      id: Date.now(),
      title: postForm.value.title,
      content: postForm.value.content,
      image: postForm.value.image,
      likes: 0,
      comments: 0
    }
    posts.value.unshift(newPost)
  }
  savePosts()
  closePostModal()
}

// 确认删除
const confirmDelete = (postId) => {
  postToDelete.value = postId
  showDeleteModal.value = true
}

// 删除发布
const deletePost = () => {
  if (postToDelete.value) {
    posts.value = posts.value.filter(p => p.id !== postToDelete.value)
    savePosts()
    closeDeleteModal()
  }
}

// 处理图片上传
const handleImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      postForm.value.image = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

// 移除图片
const removeImage = () => {
  postForm.value.image = ''
  document.getElementById('post-image').value = ''
}

// 关闭发布模态框
const closePostModal = () => {
  showPostModal.value = false
  showAddPostModal.value = false
  editingPost.value = null
  postForm.value = {
    title: '',
    content: '',
    image: ''
  }
  // 清空文件输入
  const fileInput = document.getElementById('post-image')
  if (fileInput) {
    fileInput.value = ''
  }
}

// 关闭删除模态框
const closeDeleteModal = () => {
  showDeleteModal.value = false
  postToDelete.value = null
}

// 确认删除订单
const confirmDeleteOrder = (orderId) => {
  orderToDelete.value = orderId
  showOrderDeleteModal.value = true
}

// 关闭订单删除模态框
const closeOrderDeleteModal = () => {
  showOrderDeleteModal.value = false
  orderToDelete.value = null
}

// 删除订单
const deleteOrder = async () => {
  if (orderToDelete.value) {
    try {
      const response = await orderAPI.deleteOrder(orderToDelete.value)
      console.log('删除订单成功:', response)
      // 重新加载订单列表
      await loadOrders()
      closeOrderDeleteModal()
    } catch (error) {
      console.error('删除订单失败:', error)
      // 即使出错也重新加载订单列表，因为订单可能已经删除了
      await loadOrders()
      closeOrderDeleteModal()
    }
  }
}

// 加载用户信息
const loadUserInfo = async () => {
  try {
    // 从localStorage获取用户信息
    const storedUser = localStorage.getItem('user')
    console.log('localStorage中的用户数据:', storedUser)
    if (storedUser) {
      const userData = JSON.parse(storedUser)
      console.log('解析后的用户数据:', userData)
      console.log('用户数据类型:', typeof userData)
      console.log('用户数据结构:', Object.keys(userData))
      console.log('username字段值:', userData.username)
      console.log('username字段类型:', typeof userData.username)
      
      // 检查用户数据结构，尝试从不同字段获取用户名
      let username = '未知旅行者'
      if (userData.username && userData.username !== '用户' && userData.username !== 'user') {
        username = userData.username
        console.log('使用username字段作为用户名:', username)
      } else if (userData.user && userData.user.username) {
        username = userData.user.username
        console.log('使用user.username字段作为用户名:', username)
      } else if (userData.name) {
        username = userData.name
        console.log('使用name字段作为用户名:', username)
      } else if (userData.userName) {
        username = userData.userName
        console.log('使用userName字段作为用户名:', username)
      } else {
        console.log('未找到有效的用户名字段，使用默认值')
      }
      
      // 更新用户数据
      user.value = {
        ...userData,
        username: username
      }
      console.log('最终用户数据:', user.value)
    } else {
      // 没有用户信息，设置默认值
      user.value = {
        username: '未知旅行者',
        avatar: '',
        email: '',
        phone: '',
        bio: ''
      }
      console.log('localStorage中没有用户数据，使用默认值')
    }
  } catch (error) {
    console.error('加载用户信息失败:', error)
    // 出错时设置默认值
    user.value = {
      username: '未知旅行者',
      avatar: '',
      email: '',
      phone: '',
      bio: ''
    }
  }
}

// 打开编辑个人资料模态框
const openEditProfileModal = () => {
  // 头像用完整URL预览，但为空时不留占位（避免默认头像被误认为已有头像）
  const avatarPreview = getAvatarUrl(user.value.avatar)
  const isDefault = avatarPreview === '/image/Profile/user_avatar_default.jpeg'
  profileForm.value = {
    nickname: user.value.nickname || '',
    email: user.value.email || '',
    phone: user.value.phone || '',
    bio: user.value.bio || '',
    avatar: isDefault ? '' : avatarPreview
  }
  // 保存原始值，用于比较哪些字段发生了变化
  originalUser.value = { ...profileForm.value }
  showEditProfileModal.value = true
}

// 处理头像上传
const handleAvatarUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      profileForm.value.avatar = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

// 移除头像
const removeAvatar = () => {
  profileForm.value.avatar = ''
  document.getElementById('edit-avatar').value = ''
}

// 保存个人资料
const saveProfile = async () => {
  try {
    loading.value = true

    const formData = new FormData()

    // 从localStorage获取当前用户信息，用于传递user_id
    let storedUser = null
    try { storedUser = JSON.parse(localStorage.getItem('user')) } catch (e) {}
    if (storedUser && storedUser.id) {
      formData.append('user_id', storedUser.id)
    }

    // 只发送与原始值不同的字段（局部更新）
    const textFields = ['nickname', 'email', 'phone', 'bio']
    const original = originalUser.value || {}
    textFields.forEach(field => {
      const newVal = (profileForm.value[field] || '').trim()
      const oldVal = (original[field] || '').trim()
      if (newVal !== oldVal) {
        formData.append(field, newVal)
      }
    })

    // 处理头像上传：只有用户选择了新文件时才上传
    const avatarInput = document.getElementById('edit-avatar')
    if (avatarInput && avatarInput.files && avatarInput.files[0]) {
      formData.append('avatar', avatarInput.files[0])
    }

    console.log('发送的更新数据:', [...formData.entries()])

    // 调用API更新个人资料
    const userData = await api.put('/users/profile/', formData)
    console.log('更新个人资料成功:', userData)

    // 更新本地用户信息
    user.value = {
      ...user.value,
      ...userData
    }
    // 同步到localStorage
    let currentStoredUser = null
    try { currentStoredUser = JSON.parse(localStorage.getItem('user')) } catch (e) {}
    localStorage.setItem('user', JSON.stringify({
      ...currentStoredUser,
      ...userData
    }))
    closeEditProfileModal()
    alert('资料更新成功！')
  } catch (error) {
    console.error('更新个人资料失败:', error)
    if (error.response) {
      const errorMsg = error.response.data.error || error.response.data.detail || JSON.stringify(error.response.data) || error.response.statusText
      alert(`更新失败: ${errorMsg}`)
    } else if (error.request) {
      alert('更新失败: 服务器无响应，请检查网络连接')
    } else {
      alert(`更新失败: ${error.message}`)
    }
  } finally {
    loading.value = false
  }
}

// 关闭编辑个人资料模态框
const closeEditProfileModal = () => {
  showEditProfileModal.value = false
  profileForm.value = {
    nickname: '',
    email: '',
    phone: '',
    bio: '',
    avatar: ''
  }
  originalUser.value = {}
  // 清空文件输入
  const fileInput = document.getElementById('edit-avatar')
  if (fileInput) {
    fileInput.value = ''
  }
}

// 监听showAddPostModal的变化
watch(showAddPostModal, (newValue) => {
  if (newValue) {
    openAddPostModal()
  }
})

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

onMounted(async () => {
  // 加载用户信息
  await loadUserInfo()
  // 加载订单数据
  await loadOrders()
  // 加载发布数据
  loadPosts()
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
})

// 监听路由变化，每次路由变化时重新加载用户信息和订单数据
watch(() => route.path, async () => {
  await loadUserInfo()
  await loadOrders()
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Page Header */
.page-header {
  background-color: var(--primary-color);
  color: var(--white);
  padding: 64px 0;
  text-align: center;
}

.page-header h1 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--white);
}

.page-header p {
  font-size: 18px;
  margin-bottom: 0;
}

/* User Info */
.user-info {
  padding: 48px 0;
  background-color: var(--white);
}

.user-card {
  display: flex;
  align-items: center;
  gap: 24px;
  background-color: var(--bg-color);
  padding: 24px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
}

.user-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: var(--shadow);
}

.user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.user-header h3 {
  font-size: 24px;
  font-weight: 600;
  color: var(--text-dark);
  margin: 0;
}

.edit-profile-btn {
  padding: 6px 12px;
  font-size: 14px;
}

.user-level {
  font-size: 14px;
  color: var(--primary-color);
  margin-bottom: 16px;
  font-weight: 500;
}

.user-stats {
  display: flex;
  gap: 32px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.stat-number {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
}

.stat-label {
  font-size: 14px;
  color: var(--text-medium);
}

/* Orders Section */
.orders-section {
  padding: 64px 0;
  background-color: var(--bg-color);
}

.orders-section h2 {
  margin-bottom: 24px;
  color: var(--text-dark);
}

.order-tabs {
  display: flex;
  gap: 16px;
  margin-bottom: 32px;
  overflow-x: auto;
}

.empty-orders {
  text-align: center;
  padding: 64px 24px;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
}

.empty-orders p {
  font-size: 18px;
  color: var(--text-medium);
  margin-bottom: 24px;
}

.empty-orders .btn {
  margin: 0 auto;
}

.order-tab {
  padding: 8px 16px;
  border: none;
  background: none;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-medium);
  cursor: pointer;
  transition: var(--transition);
  white-space: nowrap;
  border-bottom: 2px solid transparent;
}

.order-tab:hover {
  color: var(--primary-color);
}

.order-tab.active {
  color: var(--primary-color);
  border-bottom-color: var(--primary-color);
}

.order-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.order-card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.order-card:hover {
  box-shadow: var(--shadow-hover);
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border-color);
}

.order-id {
  font-size: 14px;
  color: var(--text-medium);
}

.order-status {
  font-size: 14px;
  font-weight: 500;
  padding: 4px 12px;
  border-radius: 20px;
}

.order-status.pending {
  background-color: #fff3cd;
  color: #856404;
}

.order-status.paid {
  background-color: #cce5ff;
  color: #004085;
}

.order-status.confirmed {
  background-color: #d4edda;
  color: #155724;
}

.order-status.completed {
  background-color: #f8f9fa;
  color: #6c757d;
}

.order-status.cancelled {
  background-color: #f8d7da;
  color: #721c24;
}

.order-status.refunded {
  background-color: #e2e3e5;
  color: #383d41;
}

.order-type {
  display: inline-block;
  font-size: 12px;
  color: var(--primary-color);
  background-color: rgba(var(--primary-color-rgb), 0.1);
  padding: 2px 8px;
  border-radius: 4px;
  margin-bottom: 8px;
}

.order-create-time {
  font-size: 13px;
  color: var(--text-light);
  margin-bottom: 8px;
}

.order-content {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}

.order-content img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: var(--radius-md);
}

.order-info {
  flex: 1;
}

.order-info h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.order-date {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 8px;
}

.order-price {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.order-price span {
  font-size: 14px;
  color: var(--text-medium);
}

.total-price {
  font-size: 16px;
  font-weight: 600;
  color: var(--orange);
}

.order-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}



/* Posts Section */
.posts-section {
  padding: 64px 0;
  background-color: var(--bg-color);
}

.posts-section h2 {
  margin-bottom: 24px;
  color: var(--text-dark);
}

.posts-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.post-card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.post-card:hover {
  box-shadow: var(--shadow-hover);
}

.post-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.post-info {
  padding: 20px;
}

.post-info h4 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.post-info p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 16px;
  line-height: 1.5;
}

.post-stats {
  display: flex;
  gap: 24px;
  margin-bottom: 16px;
  font-size: 14px;
  color: var(--text-medium);
}

.post-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

.action-btn {
  padding: 6px 12px;
  border: 1px solid var(--border-color);
  background-color: var(--white);
  border-radius: 20px;
  font-size: 14px;
  cursor: pointer;
  transition: var(--transition);
}

.action-btn:hover {
  background-color: var(--primary-color);
  color: var(--white);
  border-color: var(--primary-color);
}

.action-btn.delete-btn:hover {
  background-color: var(--red);
  border-color: var(--red);
}

/* Empty Posts */
.empty-posts {
  text-align: center;
  padding: 64px 24px;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
}

.empty-posts p {
  font-size: 18px;
  color: var(--text-medium);
  margin-bottom: 24px;
}

.empty-posts .btn {
  margin: 0 auto;
}

/* Modal Styles */
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
  box-shadow: var(--shadow-hover);
  width: 90%;
  max-width: 500px;
  max-height: 80vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid var(--border-color);
}

.modal-header h3 {
  margin: 0;
  color: var(--text-dark);
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: var(--text-medium);
  transition: color 0.3s;
}

.close-btn:hover {
  color: var(--text-dark);
}

.modal-body {
  padding: 24px;
}

/* Form Styles */
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
  border-radius: var(--radius-md);
  font-size: 14px;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
}

/* Image Preview */
.image-preview {
  margin-top: 12px;
  position: relative;
  display: inline-block;
}

.image-preview img {
  max-width: 200px;
  max-height: 150px;
  object-fit: cover;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-color);
}

.remove-image {
  position: absolute;
  top: -10px;
  right: -10px;
  background-color: var(--red);
  color: var(--white);
  border: none;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  font-size: 16px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: var(--shadow);
  transition: background-color 0.3s;
}

.remove-image:hover {
  background-color: #c82333;
}

.form-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 32px;
}

.btn-danger {
  background-color: var(--red);
  color: var(--white);
  border: none;
  padding: 10px 20px;
  border-radius: var(--radius-md);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-danger:hover {
  background-color: #c82333;
}



/* Responsive */
@media (max-width: 768px) {
  .page-header {
    padding: 48px 0;
  }
  
  .page-header h1 {
    font-size: 28px;
  }
  
  .user-card {
    flex-direction: column;
    text-align: center;
  }
  
  .user-stats {
    justify-content: center;
  }
  
  .order-content {
    flex-direction: column;
  }
  
  .order-content img {
    width: 100%;
    height: 150px;
  }
  
  .favorite-card {
    flex-direction: column;
  }
  
  .favorite-card img {
    width: 100%;
    height: 150px;
  }
  
  .user-info,
  .orders-section,
  .posts-section {
    padding: 48px 0;
  }
  
  .back-to-top {
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
}

/* Back to Top Button */
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
</style>