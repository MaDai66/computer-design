<template>
  <div class="content-management">
    <div class="content-header">
      <h2>内容管理</h2>
      <div class="content-actions">
        <button class="btn btn-primary" @click="showAddModal = true">
          + 添加内容
        </button>
      </div>
    </div>

    <!-- 内容类型选择 -->
    <div class="content-tabs">
      <button 
        v-for="tab in contentTabs" 
        :key="tab.id"
        :class="['tab-btn', { active: activeTab === tab.id }]"
        @click="handleTabClick(tab.id)"
      >
        {{ tab.name }}
      </button>
    </div>

    <!-- 产品管理 -->
    <div v-if="activeTab === 'products'" class="content-section">
      <div class="section-header">
        <h3>产品管理</h3>
        <div class="search-box">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索产品..."
            @keyup.enter="handleSearch"
          />
          <button class="search-btn" @click="handleSearch">搜索</button>
        </div>
      </div>
      
      <div class="products-grid">
        <div v-for="product in products" :key="product.id" class="product-card">
          <div class="product-image">
            <img :src="getImageUrl(product.image)" :alt="product.name" />
          </div>
          <div class="product-info">
            <h4>{{ product.name }}</h4>
            <p class="product-price">¥{{ product.price }}</p>
            <p class="product-desc">{{ product.description }}</p>
            <div class="product-actions">
              <button class="action-btn edit">编辑</button>
              <button class="action-btn delete">删除</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 活动管理 -->
    <div v-if="activeTab === 'activities'" class="content-section">
      <div class="section-header">
        <h3>活动管理</h3>
        <div class="search-box">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索活动..."
            @keyup.enter="handleSearch"
          />
          <button class="search-btn" @click="handleSearch">搜索</button>
        </div>
      </div>
      
      <div class="activities-list">
        <div v-for="activity in activities" :key="activity.id" class="activity-item">
          <div class="activity-image">
            <img :src="getImageUrl(activity.image)" :alt="activity.title" />
          </div>
          <div class="activity-info">
            <h4>{{ activity.title }}</h4>
            <p class="activity-date">{{ activity.date }}</p>
            <p class="activity-desc">{{ activity.description }}</p>
            <div class="activity-actions">
              <button class="action-btn edit">编辑</button>
              <button class="action-btn delete">删除</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 非遗项目管理 -->
    <div v-if="activeTab === 'heritage'" class="content-section">
      <div class="section-header">
        <h3>非遗项目管理</h3>
        <div class="search-box">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索非遗项目..."
            @keyup.enter="handleSearch"
          />
          <button class="search-btn" @click="handleSearch">搜索</button>
        </div>
      </div>
      
      <div class="heritage-list">
        <div v-for="item in heritageItems" :key="item.id" class="heritage-item">
          <div class="heritage-image">
            <img :src="getImageUrl(item.image)" :alt="item.name" />
          </div>
          <div class="heritage-info">
            <h4>{{ item.name }}</h4>
            <p class="heritage-level">{{ item.level }}</p>
            <p class="heritage-desc">{{ item.description }}</p>
            <div class="heritage-actions">
              <button class="action-btn edit">编辑</button>
              <button class="action-btn delete">删除</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 旅游路线管理 -->
    <div v-if="activeTab === 'tours'" class="content-section">
      <div class="section-header">
        <h3>旅游路线管理</h3>
        <div class="search-box">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索旅游路线..."
            @keyup.enter="handleSearch"
          />
          <button class="search-btn" @click="handleSearch">搜索</button>
        </div>
      </div>
      
      <div class="tours-list">
        <div v-for="tour in tours" :key="tour.id" class="tour-card">
          <div class="tour-image">
            <img :src="tour.image" :alt="tour.name" />
          </div>
          <div class="tour-content">
            <div class="tour-header">
              <h4>{{ tour.name }}</h4>
              <span class="tour-rating">⭐ {{ tour.rating }}</span>
            </div>
            <div class="tour-info">
              <span class="info-tag">{{ tour.duration }}</span>
              <span class="info-tag">{{ tour.experience_points }}个非遗体验点</span>
              <span class="info-tag">{{ tour.sales_count }}人已购买</span>
            </div>
            <p class="tour-description">{{ tour.description }}</p>
            <div class="tour-tags">
              <span v-for="tag in tour.tags" :key="tag" class="tour-tag">{{ tag }}</span>
            </div>
            <div class="tour-footer">
              <span class="tour-price">¥{{ tour.price }}/人起</span>
              <div class="tour-actions">
                <button class="action-btn edit">编辑</button>
                <button class="action-btn delete">删除</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 乡宿管理 -->
    <div v-if="activeTab === 'homestays'" class="content-section">
      <div class="section-header">
        <h3>乡宿管理</h3>
        <div class="search-box">
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="搜索乡宿..."
            @keyup.enter="handleSearch"
          />
          <button class="search-btn" @click="handleSearch">搜索</button>
        </div>
      </div>
      
      <div class="homestays-list">
        <div v-for="homestay in homestays" :key="homestay.id" class="homestay-card">
          <div class="homestay-image">
            <img :src="homestay.image" :alt="homestay.name" />
            <div class="homestay-badges">
              <span v-if="homestay.hot" class="badge badge-hot">🔥 热门</span>
              <span v-if="homestay.has_heritage" class="badge badge-heritage">📜 非遗体验</span>
            </div>
          </div>
          <div class="homestay-content">
            <div class="homestay-header">
              <h4>{{ homestay.name }}</h4>
              <span class="homestay-rating">⭐ {{ homestay.rating }}</span>
            </div>
            <div class="homestay-location">📍 {{ homestay.location }}</div>
            <p class="homestay-description">{{ homestay.description }}</p>
            <div class="homestay-facilities">
              <span v-for="facility in homestay.facilities" :key="facility" class="facility-tag">{{ facility }}</span>
            </div>
            <div class="homestay-footer">
              <span class="homestay-price">¥{{ homestay.price }}/晚</span>
              <div class="homestay-actions">
                <button class="action-btn edit">编辑</button>
                <button class="action-btn delete">删除</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 添加内容模态框 -->
    <div v-if="showAddModal" class="modal-overlay" @click="showAddModal = false">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>添加内容</h3>
          <button class="close-btn" @click="showAddModal = false">&times;</button>
        </div>
        <div class="modal-body">
          <div class="form-group">
            <label>内容类型</label>
            <select v-model="newContent.type">
              <option value="product">产品</option>
              <option value="activity">活动</option>
              <option value="heritage">非遗项目</option>
            </select>
          </div>
          <div class="form-group">
            <label>名称/标题</label>
            <input type="text" v-model="newContent.name" placeholder="请输入名称" />
          </div>
          <div class="form-group">
            <label>描述</label>
            <textarea v-model="newContent.description" placeholder="请输入描述" rows="3"></textarea>
          </div>
          <div class="form-group" v-if="newContent.type === 'product'">
            <label>价格</label>
            <input type="number" v-model="newContent.price" placeholder="请输入价格" />
          </div>
          <div class="form-group">
            <label>图片</label>
            <input type="file" @change="handleImageUpload" />
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" @click="showAddModal = false">取消</button>
          <button class="btn btn-primary" @click="addContent">保存</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { adminAPI } from '../api/adminAPI'
import { tourAPI } from '../../api/tours'
import { homestayAPI } from '../../api/homestay'

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const activeTab = ref('products')
const searchQuery = ref('')
const showAddModal = ref(false)
const newContent = ref({
  type: 'product',
  name: '',
  description: '',
  price: '',
  image: ''
})
const isLoading = ref(false)

const getImageUrl = (imagePath) => {
  if (!imagePath) return ''
  if (imagePath.startsWith('http')) return imagePath
  if (imagePath.startsWith('/media')) return apiBaseUrl + imagePath
  if (imagePath.startsWith('/image')) return imagePath
  return apiBaseUrl + imagePath
}

const contentTabs = [
  { id: 'products', name: '产品' },
  { id: 'activities', name: '活动' },
  { id: 'heritage', name: '非遗项目' },
  { id: 'tours', name: '旅游路线' },
  { id: 'homestays', name: '乡宿' }
]

// 数据存储
const products = ref([])
const activities = ref([])
const heritageItems = ref([])
const tours = ref([])
const homestays = ref([])

// 加载产品数据
const loadProducts = async () => {
  isLoading.value = true
  try {
    const response = await adminAPI.products.getList({ search: searchQuery.value })
    products.value = response.results || []
  } catch (error) {
    console.error('加载产品失败:', error)
  } finally {
    isLoading.value = false
  }
}

// 加载活动数据
const loadActivities = async () => {
  isLoading.value = true
  try {
    const response = await adminAPI.activities.getList({ search: searchQuery.value })
    activities.value = response.results || []
  } catch (error) {
    console.error('加载活动失败:', error)
  } finally {
    isLoading.value = false
  }
}

// 加载非遗项目数据
const loadHeritage = async () => {
  isLoading.value = true
  try {
    const response = await adminAPI.heritage.getList({ search: searchQuery.value })
    heritageItems.value = response.results || []
  } catch (error) {
    console.error('加载非遗项目失败:', error)
  } finally {
    isLoading.value = false
  }
}

// 加载旅游路线数据
const loadTours = async () => {
  isLoading.value = true
  try {
    const response = await tourAPI.getTourList()
    tours.value = (response.results || response).map(tour => ({
      id: tour.id,
      name: tour.name,
      image: getImageUrl(tour.image),
      duration: tour.duration,
      price: parseFloat(tour.price) || 0,
      experience_points: tour.experience_points || 0,
      rating: tour.rating || 0,
      review_count: tour.review_count || 0,
      sales_count: tour.sales_count || 0,
      description: tour.description,
      tags: tour.tags || []
    }))
  } catch (error) {
    console.error('加载旅游路线失败:', error)
    // 模拟数据
    tours.value = [
      {
        id: 1,
        name: '长白山非遗探索之旅',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbaishan%20mountain%20tourism&image_size=portrait_4_3',
        duration: '3天2晚',
        price: 1288,
        experience_points: 15,
        rating: 4.8,
        review_count: 126,
        sales_count: 235,
        description: '深入长白山，探索满族、朝鲜族等非遗文化',
        tags: ['非遗体验', '自然风光']
      },
      {
        id: 2,
        name: '查干湖冬捕文化游',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20tour&image_size=portrait_4_3',
        duration: '2天1晚',
        price: 888,
        experience_points: 8,
        rating: 4.9,
        review_count: 203,
        sales_count: 412,
        description: '体验查干湖冬捕文化，感受渔猎风情',
        tags: ['冬捕', '民俗']
      },
      {
        id: 3,
        name: '朝鲜族民俗村体验',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20ethnic%20village%20tour&image_size=portrait_4_3',
        duration: '1天',
        price: 568,
        experience_points: 5,
        rating: 4.7,
        review_count: 189,
        sales_count: 189,
        description: '走进朝鲜族民俗村，体验传统歌舞和美食',
        tags: ['民俗', '文化体验']
      }
    ]
  } finally {
    isLoading.value = false
  }
}

// 标签点击处理
const handleTabClick = (tabId) => {
  activeTab.value = tabId
  handleTabChange()
}

// 加载乡宿数据
const loadHomestays = async () => {
  isLoading.value = true
  try {
    const response = await homestayAPI.getHomestayList()
    homestays.value = (response.results || response).map(homestay => ({
      id: homestay.id,
      name: homestay.name,
      image: getImageUrl(homestay.image),
      price: parseFloat(homestay.price) || 0,
      rating: homestay.rating || 0,
      review_count: homestay.review_count || 0,
      location: homestay.location,
      area: homestay.area,
      has_heritage: homestay.has_heritage || false,
      self_operated: homestay.self_operated || false,
      hot: homestay.hot || false,
      description: homestay.description,
      facilities: homestay.facilities || []
    }))
  } catch (error) {
    console.error('加载乡宿失败:', error)
    // 模拟数据
    homestays.value = [
      {
        id: 1,
        name: '长白山满族风情园',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20style%20homestay%20traditional%20house&image_size=portrait_4_3',
        price: 398,
        rating: 4.8,
        review_count: 156,
        location: '延边朝鲜族自治州',
        area: '长白山',
        has_heritage: true,
        self_operated: true,
        hot: true,
        description: '体验满族传统火炕，品尝地道农家菜',
        facilities: ['免费WiFi', '停车场', '早餐', '温泉']
      },
      {
        id: 2,
        name: '查干湖渔家乐',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=fishing%20village%20homestay%20lake%20view&image_size=portrait_4_3',
        price: 298,
        rating: 4.7,
        review_count: 203,
        location: '松原市查干湖',
        area: '查干湖',
        has_heritage: true,
        self_operated: false,
        hot: true,
        description: '住在湖边，体验渔猎生活，品尝新鲜湖鱼',
        facilities: ['免费WiFi', '停车场', '早餐', '钓鱼']
      },
      {
        id: 3,
        name: '朝鲜族民居客栈',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20traditional%20house%20homestay&image_size=portrait_4_3',
        price: 358,
        rating: 4.9,
        review_count: 128,
        location: '延边朝鲜族自治州',
        area: '朝鲜族民俗村',
        has_heritage: true,
        self_operated: false,
        hot: false,
        description: '朝鲜族传统民居，体验炕文化和民族美食',
        facilities: ['免费WiFi', '停车场', '早餐', '民俗体验']
      }
    ]
  } finally {
    isLoading.value = false
  }
}

// 切换标签时加载对应数据
const handleTabChange = () => {
  switch (activeTab.value) {
    case 'products':
      loadProducts()
      break
    case 'activities':
      loadActivities()
      break
    case 'heritage':
      loadHeritage()
      break
    case 'tours':
      loadTours()
      break
    case 'homestays':
      loadHomestays()
      break
  }
}

// 搜索
const handleSearch = () => {
  handleTabChange()
}

// 处理图片上传
const handleImageUpload = (event) => {
  // 这里可以添加图片上传逻辑
  console.log('Image uploaded:', event.target.files[0])
  // 模拟图片上传，使用默认图片
  newContent.value.image = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=product%20image&image_size=portrait_4_3'
}

// 添加内容
const addContent = async () => {
  isLoading.value = true
  try {
    let response
    switch (newContent.value.type) {
      case 'product':
        response = await adminAPI.products.create(newContent.value)
        break
      case 'activity':
        response = await adminAPI.activities.create(newContent.value)
        break
      case 'heritage':
        response = await adminAPI.heritage.create(newContent.value)
        break
    }
    showAddModal.value = false
    // 重新加载数据
    handleTabChange()
  } catch (error) {
    console.error('添加内容失败:', error)
  } finally {
    isLoading.value = false
  }
}

// 编辑内容
const editContent = async (item) => {
  // 这里可以添加编辑逻辑
  console.log('Edit content:', item)
}

// 删除内容
const deleteContent = async (id, type) => {
  if (!confirm('确定要删除吗？')) return
  
  isLoading.value = true
  try {
    switch (type) {
      case 'product':
        await adminAPI.products.delete(id)
        break
      case 'activity':
        await adminAPI.activities.delete(id)
        break
      case 'heritage':
        await adminAPI.heritage.delete(id)
        break
    }
    // 重新加载数据
    handleTabChange()
  } catch (error) {
    console.error('删除内容失败:', error)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  // 初始加载产品数据
  loadProducts()
})
</script>

<style scoped>
.content-management {
  width: 100%;
}

.content-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.content-header h2 {
  margin: 0;
  color: #333;
  font-size: 24px;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.btn-primary {
  background: #3498db;
  color: white;
}

.btn-primary:hover {
  background: #2980b9;
}

.btn-secondary {
  background: #95a5a6;
  color: white;
}

.btn-secondary:hover {
  background: #7f8c8d;
}

/* 内容类型选择 */
.content-tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  border-bottom: 1px solid #e0e6ed;
  padding-bottom: 10px;
}

.tab-btn {
  padding: 10px 20px;
  border: none;
  background: none;
  cursor: pointer;
  font-size: 14px;
  color: #666;
  border-bottom: 3px solid transparent;
  transition: all 0.3s;
}

.tab-btn:hover {
  color: #3498db;
}

.tab-btn.active {
  color: #3498db;
  border-bottom-color: #3498db;
  font-weight: 500;
}

/* 内容区域 */
.content-section {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.section-header h3 {
  margin: 0;
  color: #333;
  font-size: 18px;
}

.search-box {
  display: flex;
  gap: 10px;
}

.search-box input {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.search-btn {
  padding: 8px 16px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* 产品管理 */
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.product-card {
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
  transition: box-shadow 0.3s;
}

.product-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.product-image {
  height: 200px;
  overflow: hidden;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-info {
  padding: 15px;
}

.product-info h4 {
  margin: 0 0 10px 0;
  color: #333;
  font-size: 16px;
}

.product-price {
  margin: 0 0 10px 0;
  color: #e74c3c;
  font-weight: 600;
  font-size: 18px;
}

.product-desc {
  margin: 0 0 15px 0;
  color: #666;
  font-size: 14px;
  line-height: 1.4;
}

.product-actions {
  display: flex;
  gap: 10px;
}

/* 活动管理 */
.activities-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.activity-item {
  display: flex;
  gap: 20px;
  padding: 15px;
  border: 1px solid #eee;
  border-radius: 8px;
  transition: box-shadow 0.3s;
}

.activity-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.activity-image {
  width: 150px;
  height: 100px;
  overflow: hidden;
  border-radius: 4px;
}

.activity-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.activity-info {
  flex: 1;
}

.activity-info h4 {
  margin: 0 0 5px 0;
  color: #333;
  font-size: 16px;
}

.activity-date {
  margin: 0 0 10px 0;
  color: #666;
  font-size: 14px;
}

.activity-desc {
  margin: 0 0 15px 0;
  color: #666;
  font-size: 14px;
  line-height: 1.4;
}

.activity-actions {
  display: flex;
  gap: 10px;
}

/* 非遗项目管理 */
.heritage-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.heritage-item {
  display: flex;
  gap: 20px;
  padding: 15px;
  border: 1px solid #eee;
  border-radius: 8px;
  transition: box-shadow 0.3s;
}

.heritage-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.heritage-image {
  width: 150px;
  height: 100px;
  overflow: hidden;
  border-radius: 4px;
}

.heritage-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.heritage-info {
  flex: 1;
}

.heritage-info h4 {
  margin: 0 0 5px 0;
  color: #333;
  font-size: 16px;
}

.heritage-level {
  margin: 0 0 10px 0;
  color: #3498db;
  font-size: 14px;
  font-weight: 500;
}

.heritage-desc {
  margin: 0 0 15px 0;
  color: #666;
  font-size: 14px;
  line-height: 1.4;
}

.heritage-actions {
  display: flex;
  gap: 10px;
}

/* 旅游路线管理 */
.tours-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.tour-card {
  display: flex;
  gap: 20px;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 8px;
  transition: box-shadow 0.3s;
  background: #fff;
}

.tour-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.tour-image {
  width: 200px;
  height: 150px;
  overflow: hidden;
  border-radius: 8px;
  flex-shrink: 0;
}

.tour-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.tour-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.tour-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.tour-header h4 {
  margin: 0;
  color: #333;
  font-size: 18px;
  font-weight: 600;
}

.tour-rating {
  font-size: 14px;
  color: #f39c12;
  font-weight: 500;
}

.tour-info {
  display: flex;
  gap: 15px;
  margin-bottom: 10px;
}

.info-tag {
  padding: 4px 10px;
  background: #f5f7fa;
  border-radius: 4px;
  font-size: 12px;
  color: #666;
}

.tour-description {
  margin: 0 0 10px 0;
  color: #666;
  font-size: 14px;
  line-height: 1.5;
  flex: 1;
}

.tour-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 15px;
}

.tour-tag {
  padding: 3px 8px;
  background: #e8f4fd;
  color: #3498db;
  border-radius: 4px;
  font-size: 12px;
}

.tour-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tour-price {
  font-size: 20px;
  font-weight: 600;
  color: #e74c3c;
}

.tour-actions {
  display: flex;
  gap: 10px;
}

/* 乡宿管理 */
.homestays-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.homestay-card {
  display: flex;
  gap: 20px;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 8px;
  transition: box-shadow 0.3s;
  background: #fff;
}

.homestay-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.homestay-image {
  width: 200px;
  height: 150px;
  overflow: hidden;
  border-radius: 8px;
  flex-shrink: 0;
  position: relative;
}

.homestay-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.homestay-badges {
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.badge-hot {
  background: rgba(231, 76, 60, 0.9);
  color: white;
}

.badge-heritage {
  background: rgba(52, 152, 219, 0.9);
  color: white;
}

.homestay-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.homestay-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.homestay-header h4 {
  margin: 0;
  color: #333;
  font-size: 18px;
  font-weight: 600;
}

.homestay-rating {
  font-size: 14px;
  color: #f39c12;
  font-weight: 500;
}

.homestay-location {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.homestay-description {
  margin: 0 0 10px 0;
  color: #666;
  font-size: 14px;
  line-height: 1.5;
  flex: 1;
}

.homestay-facilities {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 15px;
}

.facility-tag {
  padding: 3px 8px;
  background: #e8f9e8;
  color: #27ae60;
  border-radius: 4px;
  font-size: 12px;
}

.homestay-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.homestay-price {
  font-size: 20px;
  font-weight: 600;
  color: #e74c3c;
}

.homestay-actions {
  display: flex;
  gap: 10px;
}

/* 操作按钮 */
.action-btn {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  transition: background-color 0.3s;
}

.action-btn.edit {
  background: #3498db;
  color: white;
}

.action-btn.edit:hover {
  background: #2980b9;
}

.action-btn.delete {
  background: #e74c3c;
  color: white;
}

.action-btn.delete:hover {
  background: #c0392b;
}

/* 模态框 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 8px;
  padding: 20px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.modal-header h3 {
  margin: 0;
  color: #333;
  font-size: 18px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #999;
}

.modal-body {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: #333;
  font-weight: 500;
  font-size: 14px;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  padding-top: 15px;
  border-top: 1px solid #eee;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .content-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  
  .content-tabs {
    flex-wrap: wrap;
  }
  
  .products-grid {
    grid-template-columns: 1fr;
  }
  
  .activity-item,
  .heritage-item {
    flex-direction: column;
  }
  
  .activity-image,
  .heritage-image {
    width: 100%;
    height: 150px;
  }
}
</style>