<template>
  <div class="tour-route-detail">

    <div class="container">
      <!-- 路线主信息 -->
      <section class="route-main">
        <div class="route-header">
          <h1>朝鲜族民俗村 1 日游</h1>
          <div class="route-tags">
            <span class="tag tag-orange">非遗主题</span>
            <span class="tag tag-blue">文化体验</span>
            <span class="tag tag-green">一日游</span>
          </div>
          <div class="route-price">
            <span class="price">¥298 / 人起</span>
            <span class="duration">1 天</span>
          </div>
          <div class="route-stats">
            <span class="rating">⭐⭐⭐⭐⭐ 4.8 (980条评价)</span>
            <span class="sales">已售 1850 份</span>
          </div>
        </div>
        <div class="route-images">
          <div class="main-image">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20ethnic%20village%20Jilin%20traditional%20culture%20tour&image_size=landscape_16_9" alt="朝鲜族民俗村 1 日游" />
          </div>
          <div class="gallery">
            <img :src="minsucun1" alt="朝鲜族传统建筑" />
            <img :src="minsucun2" alt="朝鲜族传统舞蹈" />
            <img :src="minsucun3" alt="朝鲜族传统美食制作" />
            <img :src="minsucun4" alt="朝鲜族传统手工艺" />
          </div>
        </div>
        <div class="route-actions">
          <button class="btn btn-primary book-now" @click="openBookingModal">立即预订</button>
        </div>
      </section>

      <!-- 每日行程 -->
      <section class="daily-itinerary">
        <h2>每日行程</h2>
        
        <!-- 第一天 -->
        <div class="day-itinerary">
          <div class="day-header">
            <span class="day-number">DAY 1</span>
            <h3>朝鲜族民俗村体验日</h3>
          </div>
          <div class="day-content">
            <div class="time-slot">
              <div class="time">08:00 - 09:30</div>
              <div class="activity">
                <h4>集合出发</h4>
                <p>指定地点集合，乘坐舒适旅游大巴前往朝鲜族民俗村</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">09:30 - 11:00</div>
              <div class="activity">
                <h4>朝鲜族民俗村参观</h4>
                <p>游览朝鲜族传统建筑，了解朝鲜族历史文化，参观朝鲜族民俗博物馆</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">11:00 - 12:30</div>
              <div class="activity">
                <h4>非遗体验：朝鲜族农乐舞</h4>
                <p>由国家级非遗传承人指导，学习朝鲜族农乐舞基本动作，体验传统舞蹈文化</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">12:30 - 14:00</div>
              <div class="activity">
                <h4>朝鲜族特色午餐</h4>
                <p>品尝朝鲜族特色美食，如冷面、辣白菜、烤肉等传统菜肴（推荐：石锅拌饭、朝鲜烤肉）</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">14:00 - 15:30</div>
              <div class="activity">
                <h4>非遗体验：打糕制作</h4>
                <p>亲手制作传统打糕，感受朝鲜族饮食文化的魅力</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">15:30 - 16:30</div>
              <div class="activity">
                <h4>非遗体验：泡菜制作</h4>
                <p>学习制作朝鲜族传统泡菜，了解泡菜的腌制过程和文化意义</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">16:30 - 17:30</div>
              <div class="activity">
                <h4>自由活动</h4>
                <p>在民俗村内自由活动，购买特色纪念品，拍照留念</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">17:30 - 19:00</div>
              <div class="activity">
                <h4>返程</h4>
                <p>乘坐大巴返回市区，结束愉快的朝鲜族民俗文化之旅</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 非遗亮点 -->
      <section class="heritage-highlights">
        <h2>非遗亮点</h2>
        <div class="highlights-grid">
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>💃</span>
            </div>
            <h3>朝鲜族农乐舞</h3>
            <p>国家级非物质文化遗产，历史悠久，风格独特，是朝鲜族文化的重要组成部分</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>🍚</span>
            </div>
            <h3>朝鲜族打糕制作</h3>
            <p>传统手工制作技艺，口感软糯，是朝鲜族重要的传统食品</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>🥬</span>
            </div>
            <h3>朝鲜族泡菜制作</h3>
            <p>传统发酵食品制作技艺，具有独特的风味和保健功效</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>🏠</span>
            </div>
            <h3>朝鲜族传统建筑</h3>
            <p>独特的建筑风格，体现了朝鲜族的生活方式和审美观念</p>
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
              <li>全程旅游大巴交通</li>
              <li>朝鲜族民俗村门票</li>
              <li>午餐（朝鲜族特色餐）</li>
              <li>所有非遗体验活动费用</li>
              <li>专业导游服务</li>
              <li>旅游保险</li>
            </ul>
          </div>
          <div class="cost-excludes">
            <h3>费用不含</h3>
            <ul>
              <li>个人消费</li>
              <li>往返集合地点的交通费用</li>
              <li>因天气等不可抗力因素产生的额外费用</li>
              <li>其他未提及的费用</li>
            </ul>
          </div>
          <div class="booking-notes">
            <h3>预订须知</h3>
            <ul>
              <li>至少提前1天预订</li>
              <li>人数限制：每团最多30人</li>
              <li>儿童政策：1.2米以下儿童半价，1.2米以上全价</li>
              <li>退改政策：出发前1天可全额退款，出发当天不退款</li>
              <li>建议穿着舒适的运动鞋和休闲衣物</li>
              <li>请携带身份证等有效证件</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- 用户评价 -->
      <section class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-header">
          <div class="rating-overall">
            <span class="rating-score">4.8</span>
            <span class="rating-stars">⭐⭐⭐⭐⭐</span>
            <span class="rating-count">980条评价</span>
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
              <p>这次朝鲜族民俗村之旅非常棒！农乐舞体验很有意思，老师教得很耐心。打糕和泡菜制作也很有趣，自己做的食物特别好吃。导游讲解很专业，全程服务周到。非常推荐！</p>
              <div class="review-images">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20traditional%20dance%20class&image_size=portrait_4_3" alt="农乐舞体验" />
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20rice%20cake%20making&image_size=portrait_4_3" alt="打糕制作" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@美食探索者</span>
                  <span class="review-date">2026-04-08</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>朝鲜族的美食太好吃了！冷面、辣白菜、烤肉都非常地道。打糕制作体验很有趣，自己做的打糕特别软糯。民俗村的建筑也很有特色，拍照很出片。导游很热情，讲解详细，推荐大家来体验！</p>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@家庭出游</span>
                  <span class="review-date">2026-04-05</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>带孩子一起参加的，孩子非常喜欢农乐舞和打糕制作。导游对孩子也很有耐心，讲解生动有趣。行程安排合理，不会太赶，适合家庭出游。朝鲜族的美食也很合我们的口味，特别是石锅拌饭，非常好吃。</p>
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
                  <h7>Day {{ index + 1 }}</h7>
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
          <h3>预订朝鲜族民俗村 1 日游</h3>
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
import { useRouter } from 'vue-router'
import minsucun1 from '@/assets/minsucun/1.png'
import minsucun2 from '@/assets/minsucun/2.png'
import minsucun3 from '@/assets/minsucun/3.png'
import minsucun4 from '@/assets/minsucun/4.png'

const router = useRouter()
const showBackToTop = ref(false)

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
    type: 'tour',
    item: '朝鲜族民俗村 1 日游',
    price: 298,
    totalPrice: 298 * bookingForm.value.guests,
    guests: bookingForm.value.guests,
    date: bookingForm.value.date,
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

// 生成AI路线
const generateRoute = () => {
  // 清除之前的结果，显示加载状态
  aiResult.value = {
    title: 'AI正在生成路线...',
    description: '请稍候，AI正在根据您的偏好定制专属路线',
    itinerary: [],
    highlights: []
  }
  
  // 模拟AI生成路线
  setTimeout(() => {
    const days = aiForm.value.days
    const interests = []
    
    if (aiForm.value.interests.culture) interests.push('文化体验')
    if (aiForm.value.interests.nature) interests.push('自然风光')
    if (aiForm.value.interests.food) interests.push('美食探索')
    if (aiForm.value.interests.leisure) interests.push('休闲度假')
    
    let title = ''
    let description = ''
    let itinerary = []
    let highlights = []
    
    // 根据天数和兴趣生成路线
    if (days === '1') {
      title = '朝鲜族文化一日游'
      description = '体验朝鲜族丰富多彩的文化遗产，感受传统与现代的交融'
      itinerary = [
        {
          activities: [
            '09:00 - 参观延边朝鲜族自治州博物馆，了解朝鲜族历史文化',
            '11:30 - 品尝朝鲜族特色午餐（推荐：石锅拌饭、朝鲜烤肉）',
            '13:30 - 体验朝鲜族农乐舞',
            '15:30 - 游览朝鲜族民俗村',
            '17:30 - 结束行程'
          ]
        }
      ]
      highlights = ['文化体验丰富', '历史感强烈', '适合一日游']
    } else if (days === '2') {
      title = '朝鲜族文化二日游'
      description = '深入体验朝鲜族文化和自然风光'
      itinerary = [
        {
          activities: [
            '08:00 - 出发前往延边朝鲜族自治州',
            '11:30 - 抵达延边，品尝朝鲜族特色午餐（推荐：冷面、辣白菜）',
            '13:00 - 游览朝鲜族民俗村',
            '15:30 - 体验朝鲜族打糕制作',
            '18:00 - 入住朝鲜族特色民宿'
          ]
        },
        {
          activities: [
            '08:00 - 早餐后前往长白山',
            '09:30 - 游览长白山天池',
            '11:30 - 品尝长白山山珍午餐（推荐：人参鸡汤）',
            '13:00 - 体验朝鲜族泡菜制作',
            '15:30 - 返程'
          ]
        }
      ]
      highlights = ['文化体验丰富', '自然风光壮丽', '适合周末游']
    } else {
      title = '吉林朝鲜族文化深度之旅'
      description = '全方位体验吉林的朝鲜族文化和自然景观'
      itinerary = [
        {
          activities: [
            '09:00 - 参观延边朝鲜族自治州博物馆',
            '11:30 - 品尝朝鲜族特色午餐（推荐：石锅拌饭、朝鲜烤肉）',
            '13:30 - 体验朝鲜族农乐舞',
            '15:30 - 游览朝鲜族民俗村',
            '17:30 - 入住朝鲜族特色民宿'
          ]
        },
        {
          activities: [
            '08:00 - 出发前往长白山',
            '11:30 - 抵达长白山，品尝山珍午餐（推荐：人参鸡汤）',
            '13:00 - 游览长白山天池',
            '15:30 - 体验朝鲜族打糕制作',
            '18:00 - 入住长白山脚下民宿'
          ]
        },
        {
          activities: [
            '08:00 - 早餐后前往查干湖',
            '09:30 - 游览查干湖',
            '11:30 - 品尝查干湖特色午餐（推荐：全鱼宴）',
            '13:00 - 体验朝鲜族泡菜制作',
            '15:30 - 返程'
          ]
        }
      ]
      highlights = ['行程丰富', '文化深度体验', '自然景观壮丽']
    }
    
    // 根据兴趣偏好调整行程
    if (interests.length > 0) {
      // 添加兴趣相关的亮点
      highlights = [...highlights, `包含${interests.join('、')}等您感兴趣的内容`]
      
      // 根据兴趣偏好调整行程内容
      if (interests.includes('文化体验')) {
        // 在每天的行程中添加文化体验
        itinerary.forEach((day, index) => {
          if (index === 0) {
            day.activities.push(`${14 + index}:00 - 参观延边朝鲜族民俗博物馆，体验朝鲜族文化`)
          } else if (index === 1) {
            day.activities.push(`${14 + index}:00 - 参观长白山满族文化博物馆，了解满族历史`)
          } else {
            day.activities.push(`${14 + index}:00 - 参观吉林省博物馆，了解吉林历史文化`)
          }
        })
      }
      
      if (interests.includes('自然风光')) {
        // 在每天的行程中添加自然景观
        itinerary.forEach((day, index) => {
          if (index === 0) {
            day.activities.push(`${15 + index}:00 - 游览延吉市布尔哈通河，欣赏城市风光`)
          } else if (index === 1) {
            day.activities.push(`${15 + index}:00 - 游览长白山地下森林，感受原始森林的魅力`)
          } else {
            day.activities.push(`${15 + index}:00 - 游览查干湖，欣赏湖泊风光`)
          }
        })
      }
      
      if (interests.includes('美食探索')) {
        // 在每天的行程中添加美食体验
        itinerary.forEach((day, index) => {
          if (index === 0) {
            day.activities.push(`${16 + index}:00 - 品尝朝鲜族特色小吃，如米肠、打糕`)
          } else if (index === 1) {
            day.activities.push(`${16 + index}:00 - 品尝长白山山珍，如松茸、林蛙`)
          } else {
            day.activities.push(`${16 + index}:00 - 品尝吉林特色美食，如锅包肉、煎粉`)
          }
        })
      }
      
      if (interests.includes('休闲度假')) {
        // 在每天的行程中添加休闲活动
        itinerary.forEach((day, index) => {
          if (index === 0) {
            day.activities.push(`${17 + index}:00 - 体验朝鲜族传统汗蒸，放松身心`)
          } else if (index === 1) {
            day.activities.push(`${17 + index}:00 - 体验长白山温泉，缓解疲劳`)
          } else {
            day.activities.push(`${17 + index}:00 - 体验吉林特色休闲活动，如滑雪`)
          }
        })
      }
    }
    
    aiResult.value = {
      title,
      description,
      itinerary,
      highlights
    }
  }, 1000)
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
  padding-bottom: 16px;
  border-bottom: 2px solid var(--primary-color);
}

/* 路线主信息 */
.route-header h1 {
  font-size: 32px;
  font-weight: 700;
  color: var(--text-dark);
  margin-bottom: 16px;
}

.route-tags {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
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

.route-price {
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

.duration {
  font-size: 16px;
  color: var(--text-medium);
}

.route-stats {
  display: flex;
  align-items: center;
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

/* 每日行程 */
.day-itinerary {
  margin-bottom: 32px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.day-header {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 24px;
  background-color: var(--bg-light);
  border-bottom: 1px solid var(--border-color);
}

.day-number {
  font-size: 18px;
  font-weight: 700;
  color: var(--primary-color);
  background-color: var(--primary-light);
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

.cost-includes,
.cost-excludes,
.booking-notes {
  background-color: var(--bg-light);
  padding: 24px;
  border-radius: var(--radius-md);
}

.cost-includes h3,
.cost-excludes h3,
.booking-notes h3 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 16px;
  font-weight: 600;
  color: var(--text-dark);
}

.cost-includes ul,
.cost-excludes ul,
.booking-notes ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.cost-includes li,
.cost-excludes li,
.booking-notes li {
  margin-bottom: 8px;
  position: relative;
  padding-left: 20px;
  line-height: 1.4;
  color: var(--text-medium);
}

.cost-includes li::before,
.cost-excludes li::before,
.booking-notes li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--primary-color);
  font-weight: bold;
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
  .cost-content {
    grid-template-columns: 1fr;
  }
  
  .reviews-header {
    flex-direction: column;
    align-items: flex-start;
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
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
}
</style>