<template>
  <div class="tour-route-detail">


    <div class="container">
      <!-- 路线主信息 -->
      <section class="route-main">
        <div class="route-header">
          <h1>松花湖生态文化2日游</h1>
          <div class="route-tags">
            <span class="tag tag-orange">城市逃离者</span>
            <span class="tag tag-blue">生态主题</span>
            <span class="tag tag-green">文化体验</span>
          </div>
          <div class="route-price">
            <span class="price">¥588 / 人起</span>
            <span class="duration">2 天 1 晚</span>
          </div>
          <div class="route-stats">
            <span class="rating">⭐⭐⭐⭐⭐ 4.8 (980条评价)</span>
            <span class="sales">已售 1860 份</span>
          </div>
        </div>
        <div class="route-images">
          <div class="main-image">
            <img :src="songhuahu1" alt="松花湖生态文化2日游" />
          </div>
          <div class="gallery">
            <img :src="songhuahu2" alt="松花湖风景" />
            <img :src="songhuahu3" alt="传统渔业文化" />
            <img :src="songhuahu4" alt="生态旅游活动" />
            <img :src="songhuahu5" alt="当地文化表演" />
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
            <h3>松花湖生态体验日</h3>
          </div>
          <div class="day-content">
            <div class="time-slot">
              <div class="time">08:00 - 09:30</div>
              <div class="activity">
                <h4>集合出发</h4>
                <p>指定地点集合，乘坐舒适旅游大巴前往松花湖景区</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">09:30 - 11:30</div>
              <div class="activity">
                <h4>松花湖游船</h4>
                <p>乘坐游船游览松花湖，欣赏湖光山色，了解松花湖的生态环境</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">11:30 - 13:00</div>
              <div class="activity">
                <h4>湖鲜午餐</h4>
                <p>品尝松花湖特色湖鲜，如松花湖鱼、湖虾等新鲜美食</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">13:00 - 15:30</div>
              <div class="activity">
                <h4>生态保护活动</h4>
                <p>参与湖面垃圾清理、生态监测等环保活动，了解生态保护的重要性</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">15:30 - 17:00</div>
              <div class="activity">
                <h4>传统渔业体验</h4>
                <p>跟随当地渔民学习传统捕鱼技艺，体验撒网捕鱼的乐趣</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">17:00 - 18:30</div>
              <div class="activity">
                <h4>入住湖畔民宿</h4>
                <p>入住松花湖畔的生态民宿，欣赏湖景，休息调整</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">18:30 - 20:00</div>
              <div class="activity">
                <h4>篝火晚会</h4>
                <p>参加湖边篝火晚会，欣赏当地传统歌舞表演，品尝烤湖鱼</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 第二天 -->
        <div class="day-itinerary">
          <div class="day-header">
            <span class="day-number">DAY 2</span>
            <h3>文化探索日</h3>
          </div>
          <div class="day-content">
            <div class="time-slot">
              <div class="time">07:00 - 08:00</div>
              <div class="activity">
                <h4>早餐</h4>
                <p>享用营养早餐，准备开始一天的行程</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">08:00 - 10:00</div>
              <div class="activity">
                <h4>参观渔猎文化博物馆</h4>
                <p>了解松花湖地区的渔猎文化历史，观看传统渔业工具展示</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">10:00 - 12:30</div>
              <div class="activity">
                <h4>非遗体验：传统鱼皮画</h4>
                <p>由当地非遗传承人指导，学习制作传统鱼皮画，了解鱼皮文化</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">12:30 - 13:30</div>
              <div class="activity">
                <h4>农家特色午餐</h4>
                <p>品尝当地农家菜，如贴饼子、炖柴鸡等传统美食</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">13:30 - 15:30</div>
              <div class="activity">
                <h4>乡村文化体验</h4>
                <p>参观当地村庄，了解乡村文化，体验传统农耕活动</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">15:30 - 17:30</div>
              <div class="activity">
                <h4>返回市区</h4>
                <p>乘坐大巴返回市区，结束愉快的生态文化之旅</p>
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
              <span>🎨</span>
            </div>
            <h3>传统鱼皮画</h3>
            <p>国家级非物质文化遗产，用鱼皮制作的传统艺术品，历史悠久，工艺精湛</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>🎣</span>
            </div>
            <h3>传统渔业技艺</h3>
            <p>传承千年的捕鱼技艺，体现了当地渔民的智慧和与自然和谐相处的理念</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>🔥</span>
            </div>
            <h3>湖畔篝火晚会</h3>
            <p>传统的庆祝活动，包含歌舞表演、烤湖鱼等环节，展现当地文化特色</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>🌿</span>
            </div>
            <h3>生态保护实践</h3>
            <p>参与湖面垃圾清理、生态监测等活动，了解生态保护的重要性</p>
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
              <li>1晚湖畔生态民宿住宿</li>
              <li>3餐特色餐食（1早餐、2午餐）</li>
              <li>松花湖景区门票</li>
              <li>游船费用</li>
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
              <li>至少提前3天预订</li>
              <li>人数限制：每团最多30人</li>
              <li>儿童政策：1.2米以下儿童半价，1.2米以上全价</li>
              <li>退改政策：出发前3天可全额退款，出发前1-2天退款50%，出发当天不退款</li>
              <li>建议穿着舒适的运动鞋和防蚊虫衣物</li>
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
                  <span class="user-name">@自然爱好者</span>
                  <span class="review-date">2026-04-08</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>这次生态之旅非常棒！松花湖的景色很美，湖水清澈，空气清新。生态保护活动很有意义，让我们了解了保护湖泊生态的重要性。传统渔业体验也很有趣，学到了很多知识。住宿条件也很好，湖景房视野开阔。非常推荐！</p>
              <div class="review-images">
                <img :src="songhuahu2" alt="松花湖风景" />
                <img :src="songhuahu3" alt="传统捕鱼体验" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@文化探索者</span>
                  <span class="review-date">2026-04-05</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>鱼皮画体验很有意思，老师教得很耐心，我们都做出了漂亮的作品。篝火晚会也很热闹，当地的歌舞表演很有特色。湖鲜午餐很新鲜，味道很棒。行程安排合理，不会太赶，适合放松心情。</p>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@家庭出游</span>
                  <span class="review-date">2026-04-01</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>带孩子一起参加的，孩子非常喜欢游船和捕鱼体验。生态保护活动也让孩子学到了很多环保知识。民宿环境很好，干净舒适，早餐也很丰盛。导游对孩子很有耐心，讲解生动有趣。是一次非常有意义的家庭旅行。</p>
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
          <h3>预订松花湖生态文化2日游</h3>
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
import songhuahu1 from '@/assets/songhuahu/1.png'
import songhuahu2 from '@/assets/songhuahu/2.png'
import songhuahu3 from '@/assets/songhuahu/3.png'
import songhuahu4 from '@/assets/songhuahu/4.png'
import songhuahu5 from '@/assets/songhuahu/5.png'

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
    item: '松花湖生态文化2日游',
    price: 588,
    totalPrice: 588 * bookingForm.value.guests,
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
    description: '请稍候，AI正在根据您的偏好分析最佳旅行方案...',
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
    
    // 生成AI风格的标题和描述
    const generateAITitle = (days, interests) => {
      const prefixes = ['智能定制', 'AI推荐', '个性化', '专属', '定制化']
      const themes = interests.length > 0 ? interests.join('+') : '综合体验'
      const suffixes = {
        '1': '一日游',
        '2': '二日游',
        '3': '三日游',
        '4': '四日游',
        '5+': '多日深度游'
      }
      const randomPrefix = prefixes[Math.floor(Math.random() * prefixes.length)]
      return `${randomPrefix}·${themes}${suffixes[days] || '深度游'}`
    }
    
    const generateAIDescription = (days, interests) => {
      const intro = ['基于您的兴趣偏好，AI为您精心定制了', '根据您的个性化需求，智能推荐', '结合您的旅行偏好，为您打造']
      const middle = interests.length > 0 
        ? `以${interests.join('、')}为核心的` 
        : '全方位的'
      const activities = ['沉浸式体验', '深度探索', '文化之旅', '自然探索', '美食之旅', '休闲度假']
      const randomIntro = intro[Math.floor(Math.random() * intro.length)]
      const randomActivity = activities[Math.floor(Math.random() * activities.length)]
      return `${randomIntro}${middle}${randomActivity}，让您在${days === '1' ? '一天' : days === '2' ? '两天' : '多天'}的行程中充分感受吉林的独特魅力。`
    }
    
    let title = generateAITitle(days, interests)
    let description = generateAIDescription(days, interests)
    let itinerary = []
    let highlights = []
    
    // 根据兴趣偏好生成完全不同的路线
    if (interests.length === 0) {
      // 默认综合路线
      if (days === '1') {
        itinerary = [
          {
            activities: [
              '09:00 - 参观吉林省博物馆，了解吉林历史文化',
              '11:30 - 品尝吉林特色午餐（推荐：李连贵熏肉大饼、吉林煎粉）',
              '13:30 - 体验满族剪纸艺术',
              '15:30 - 游览伪满皇宫博物院',
              '17:30 - 结束行程'
            ]
          }
        ]
        highlights = ['文化体验丰富', '历史感强烈', '适合一日游', '行程紧凑合理']
      } else if (days === '2') {
        itinerary = [
          {
            activities: [
              '08:00 - 出发前往松花湖',
              '11:30 - 抵达松花湖，品尝湖鲜午餐（推荐：松花湖鱼、湖虾）',
              '13:00 - 乘坐游船游览松花湖',
              '15:30 - 参与生态保护活动',
              '18:00 - 入住湖畔民宿'
            ]
          },
          {
            activities: [
              '08:00 - 早餐后参观渔猎文化博物馆',
              '09:30 - 体验传统鱼皮画制作',
              '11:30 - 品尝农家特色午餐（推荐：贴饼子、炖柴鸡）',
              '13:00 - 参观当地村庄，体验传统农耕活动',
              '15:30 - 返程'
            ]
          }
        ]
        highlights = ['自然风光优美', '生态体验丰富', '适合周末游', '住宿环境舒适']
      } else {
        itinerary = [
          {
            activities: [
              '09:00 - 参观吉林省博物馆',
              '11:30 - 品尝吉林特色午餐（推荐：李连贵熏肉大饼、吉林煎粉）',
              '13:30 - 体验满族剪纸艺术',
              '15:30 - 游览伪满皇宫博物院',
              '17:30 - 入住酒店'
            ]
          },
          {
            activities: [
              '08:00 - 出发前往松花湖',
              '11:30 - 抵达松花湖，品尝湖鲜午餐（推荐：松花湖鱼、湖虾）',
              '13:00 - 乘坐游船游览松花湖',
              '15:30 - 参与生态保护活动',
              '18:00 - 入住湖畔民宿'
            ]
          },
          {
            activities: [
              '08:00 - 早餐后参观渔猎文化博物馆',
              '09:30 - 体验传统鱼皮画制作',
              '11:30 - 品尝农家特色午餐（推荐：贴饼子、炖柴鸡）',
              '13:00 - 参观当地村庄，体验传统农耕活动',
              '15:30 - 返程'
            ]
          }
        ]
        highlights = ['行程丰富', '文化深度体验', '自然景观优美', '美食种类多样']
      }
    } else if (interests.includes('文化体验') && !interests.includes('自然风光') && !interests.includes('美食探索') && !interests.includes('休闲度假')) {
      // 纯文化体验路线
      if (days === '1') {
        itinerary = [
          {
            activities: [
              '09:00 - 参观吉林省博物馆，深度了解吉林历史文化',
              '11:30 - 品尝传统吉林午餐，感受饮食文化',
              '13:30 - 体验国家级非遗：满族剪纸艺术',
              '15:30 - 游览伪满皇宫博物院，了解近代历史',
              '17:30 - 参观吉林文庙，体验儒家文化'
            ]
          }
        ]
        highlights = ['文化体验深度', '非遗项目丰富', '历史感强烈', '适合文化爱好者']
      } else if (days === '2') {
        itinerary = [
          {
            activities: [
              '08:00 - 出发前往满族民俗村',
              '10:00 - 参观满族民俗博物馆，了解满族历史',
              '11:30 - 品尝满族特色午餐（推荐：满族火锅、萨其马）',
              '13:00 - 体验满族传统服饰和礼仪',
              '15:30 - 参与满族传统手工艺制作',
              '18:00 - 入住满族风格民宿，感受传统居住文化'
            ]
          },
          {
            activities: [
              '08:00 - 早餐后前往朝鲜族民俗村',
              '09:30 - 参观朝鲜族文化博物馆',
              '11:30 - 品尝朝鲜族特色午餐（推荐：冷面、辣白菜）',
              '13:00 - 体验朝鲜族传统舞蹈和音乐',
              '15:30 - 参与朝鲜族传统手工艺制作',
              '17:30 - 返程'
            ]
          }
        ]
        highlights = ['多民族文化体验', '非遗项目丰富', '传统工艺学习', '文化深度探索']
      } else {
        itinerary = [
          {
            activities: [
              '09:00 - 参观吉林省博物馆，了解吉林历史文化',
              '11:30 - 品尝传统吉林午餐',
              '13:30 - 体验满族剪纸艺术',
              '15:30 - 游览伪满皇宫博物院',
              '17:30 - 入住酒店'
            ]
          },
          {
            activities: [
              '08:00 - 出发前往满族民俗村',
              '10:00 - 参观满族民俗博物馆',
              '11:30 - 品尝满族特色午餐',
              '13:00 - 体验满族传统服饰和礼仪',
              '15:30 - 参与满族传统手工艺制作',
              '18:00 - 入住满族风格民宿'
            ]
          },
          {
            activities: [
              '08:00 - 早餐后前往朝鲜族民俗村',
              '09:30 - 参观朝鲜族文化博物馆',
              '11:30 - 品尝朝鲜族特色午餐',
              '13:00 - 体验朝鲜族传统舞蹈和音乐',
              '15:30 - 参与朝鲜族传统手工艺制作',
              '17:30 - 返程'
            ]
          }
        ]
        highlights = ['多民族文化体验', '非遗项目丰富', '传统工艺学习', '文化深度探索', '历史感强烈']
      }
    } else if (interests.includes('自然风光') && !interests.includes('文化体验') && !interests.includes('美食探索') && !interests.includes('休闲度假')) {
      // 纯自然风光路线
      if (days === '1') {
        itinerary = [
          {
            activities: [
              '08:00 - 出发前往松花湖',
              '09:30 - 乘坐游船游览松花湖，欣赏湖光山色',
              '11:30 - 品尝景区特色午餐',
              '13:00 - 徒步松花湖周边森林步道，感受自然氧吧',
              '15:30 - 参观松花湖生态博物馆，了解生态知识',
              '17:30 - 返程'
            ]
          }
        ]
        highlights = ['自然风光优美', '生态环境良好', '适合户外活动', '空气清新']
      } else if (days === '2') {
        itinerary = [
          {
            activities: [
              '07:00 - 出发前往松花湖',
              '09:30 - 抵达松花湖，品尝湖鲜早餐',
              '10:30 - 乘坐游船游览松花湖全景',
              '12:30 - 品尝湖鲜特色午餐',
              '14:00 - 徒步松花湖森林步道',
              '16:30 - 参观松花湖生态保护区',
              '18:30 - 入住湖畔民宿'
            ]
          },
          {
            activities: [
              '07:00 - 早餐后前往净月潭国家森林公园',
              '09:00 - 游览净月潭，欣赏湖光山色',
              '11:30 - 品尝景区特色午餐',
              '13:00 - 徒步净月潭森林步道',
              '15:30 - 返程'
            ]
          }
        ]
        highlights = ['自然风光壮丽', '生态环境原始', '徒步体验丰富', '空气清新', '适合自然爱好者']
      } else {
        itinerary = [
          {
            activities: [
              '08:00 - 出发前往松花湖',
              '09:30 - 乘坐游船游览松花湖',
              '11:30 - 品尝湖鲜特色午餐',
              '13:00 - 徒步松花湖森林步道',
              '15:30 - 参观松花湖生态博物馆',
              '17:30 - 入住湖畔民宿'
            ]
          },
          {
            activities: [
              '07:00 - 早餐后前往净月潭国家森林公园',
              '09:00 - 游览净月潭',
              '11:30 - 品尝景区特色午餐',
              '13:00 - 徒步净月潭森林步道',
              '15:30 - 参观净月潭博物馆',
              '17:30 - 入住酒店'
            ]
          },
          {
            activities: [
              '07:00 - 早餐后前往查干湖',
              '09:30 - 游览查干湖',
              '11:30 - 品尝查干湖特色午餐',
              '13:00 - 参观查干湖生态保护区',
              '15:30 - 返程'
            ]
          }
        ]
        highlights = ['自然风光壮丽', '生态环境原始', '徒步体验丰富', '空气清新', '适合自然爱好者', '行程安排合理']
      }
    } else if (interests.includes('美食探索') && !interests.includes('文化体验') && !interests.includes('自然风光') && !interests.includes('休闲度假')) {
      // 纯美食探索路线
      if (days === '1') {
        itinerary = [
          {
            activities: [
              '09:00 - 早餐品尝吉林特色早点（推荐：煎粉、豆腐脑）',
              '11:30 - 午餐品尝吉林传统美食（推荐：李连贵熏肉大饼、锅包肉）',
              '13:30 - 下午茶品尝吉林特色甜点（推荐：萨其马、打糕）',
              '15:30 - 参观吉林美食文化博物馆，了解吉林饮食文化',
              '17:30 - 晚餐品尝吉林特色火锅'
            ]
          }
        ]
        highlights = ['美食种类丰富', '特色小吃众多', '饮食文化体验', '适合美食爱好者']
      } else if (days === '2') {
        itinerary = [
          {
            activities: [
              '09:00 - 早餐品尝吉林特色早点',
              '11:30 - 午餐品尝松花湖特色湖鲜（推荐：全鱼宴、湖虾）',
              '13:30 - 参观松花湖渔业文化博物馆',
              '15:30 - 体验传统鱼食制作',
              '18:30 - 晚餐品尝满族特色美食（推荐：满族火锅、萨其马）'
            ]
          },
          {
            activities: [
              '09:00 - 早餐品尝朝鲜族特色早点',
              '11:30 - 午餐品尝朝鲜族特色美食（推荐：冷面、辣白菜、烤肉）',
              '13:30 - 参观朝鲜族饮食文化博物馆',
              '15:30 - 体验朝鲜族传统美食制作',
              '17:30 - 返程'
            ]
          }
        ]
        highlights = ['多民族美食体验', '特色小吃众多', '美食制作体验', '饮食文化学习', '适合美食爱好者']
      } else {
        itinerary = [
          {
            activities: [
              '09:00 - 早餐品尝吉林特色早点',
              '11:30 - 午餐品尝吉林传统美食',
              '13:30 - 下午茶品尝吉林特色甜点',
              '15:30 - 参观吉林美食文化博物馆',
              '17:30 - 晚餐品尝吉林特色火锅',
              '入住酒店'
            ]
          },
          {
            activities: [
              '09:00 - 早餐品尝松花湖特色早点',
              '11:30 - 午餐品尝松花湖特色湖鲜',
              '13:30 - 参观松花湖渔业文化博物馆',
              '15:30 - 体验传统鱼食制作',
              '18:30 - 晚餐品尝满族特色美食',
              '入住湖畔民宿'
            ]
          },
          {
            activities: [
              '09:00 - 早餐品尝朝鲜族特色早点',
              '11:30 - 午餐品尝朝鲜族特色美食',
              '13:30 - 参观朝鲜族饮食文化博物馆',
              '15:30 - 体验朝鲜族传统美食制作',
              '17:30 - 返程'
            ]
          }
        ]
        highlights = ['多民族美食体验', '特色小吃众多', '美食制作体验', '饮食文化学习', '适合美食爱好者', '行程安排合理']
      }
    } else if (interests.includes('休闲度假') && !interests.includes('文化体验') && !interests.includes('自然风光') && !interests.includes('美食探索')) {
      // 纯休闲度假路线
      if (days === '1') {
        itinerary = [
          {
            activities: [
              '10:00 - 抵达松花湖度假村',
              '11:30 - 品尝度假村特色午餐',
              '13:00 - 体验水上休闲活动（推荐：划船、钓鱼）',
              '15:30 - 享受度假村SPA服务',
              '17:30 - 晚餐后返程'
            ]
          }
        ]
        highlights = ['休闲放松', '水上活动', 'SPA服务', '适合减压放松']
      } else if (days === '2') {
        itinerary = [
          {
            activities: [
              '10:00 - 抵达松花湖度假村',
              '11:30 - 品尝湖鲜特色午餐',
              '13:00 - 体验水上休闲活动（推荐：划船、钓鱼、水上摩托）',
              '15:30 - 享受度假村SPA服务',
              '18:30 - 晚餐品尝湖鲜盛宴',
              '20:00 - 参加度假村夜间娱乐活动'
            ]
          },
          {
            activities: [
              '09:00 - 早餐后自由活动',
              '11:30 - 品尝度假村特色午餐',
              '13:00 - 体验温泉浸泡',
              '15:30 - 返程'
            ]
          }
        ]
        highlights = ['休闲放松', '水上活动', '温泉体验', 'SPA服务', '适合减压放松']
      } else {
        itinerary = [
          {
            activities: [
              '10:00 - 抵达松花湖度假村',
              '11:30 - 品尝度假村特色午餐',
              '13:00 - 体验水上休闲活动',
              '15:30 - 享受度假村SPA服务',
              '18:30 - 晚餐品尝度假村特色美食',
              '入住度假村'
            ]
          },
          {
            activities: [
              '10:00 - 继续在松花湖度假村活动',
              '11:30 - 品尝湖鲜特色午餐',
              '13:00 - 体验更多水上活动',
              '15:30 - 享受温泉浸泡',
              '18:30 - 晚餐品尝湖鲜盛宴',
              '20:00 - 参加度假村夜间娱乐活动',
              '入住度假村'
            ]
          },
          {
            activities: [
              '09:00 - 早餐后自由活动',
              '11:30 - 品尝度假村特色午餐',
              '13:00 - 体验最后一次温泉浸泡',
              '15:30 - 返程'
            ]
          }
        ]
        highlights = ['休闲放松', '水上活动', '温泉体验', 'SPA服务', '适合减压放松', '行程安排合理']
      }
    } else {
      // 混合兴趣路线
      if (days === '1') {
        itinerary = [
          {
            activities: [
              '09:00 - 参观吉林省博物馆',
              '11:30 - 品尝吉林特色午餐',
              '13:30 - 体验满族剪纸艺术',
              '15:30 - 游览松花湖',
              '17:30 - 晚餐品尝吉林特色火锅'
            ]
          }
        ]
        highlights = ['文化体验', '自然风光', '美食探索', '行程紧凑合理']
      } else if (days === '2') {
        itinerary = [
          {
            activities: [
              '08:00 - 出发前往松花湖',
              '11:30 - 抵达松花湖，品尝湖鲜午餐',
              '13:00 - 乘坐游船游览松花湖',
              '15:30 - 参与生态保护活动',
              '18:00 - 入住湖畔民宿',
              '19:00 - 晚餐品尝湖鲜盛宴'
            ]
          },
          {
            activities: [
              '08:00 - 早餐后参观渔猎文化博物馆',
              '09:30 - 体验传统鱼皮画制作',
              '11:30 - 品尝农家特色午餐',
              '13:00 - 参观当地村庄，体验传统农耕活动',
              '15:30 - 返程'
            ]
          }
        ]
        highlights = ['自然风光', '文化体验', '美食探索', '适合周末游']
      } else {
        itinerary = [
          {
            activities: [
              '09:00 - 参观吉林省博物馆',
              '11:30 - 品尝吉林特色午餐',
              '13:30 - 体验满族剪纸艺术',
              '15:30 - 游览伪满皇宫博物院',
              '17:30 - 入住酒店'
            ]
          },
          {
            activities: [
              '08:00 - 出发前往松花湖',
              '11:30 - 抵达松花湖，品尝湖鲜午餐',
              '13:00 - 乘坐游船游览松花湖',
              '15:30 - 参与生态保护活动',
              '18:00 - 入住湖畔民宿'
            ]
          },
          {
            activities: [
              '08:00 - 早餐后参观渔猎文化博物馆',
              '09:30 - 体验传统鱼皮画制作',
              '11:30 - 品尝农家特色午餐',
              '13:00 - 参观当地村庄，体验传统农耕活动',
              '15:30 - 返程'
            ]
          }
        ]
        highlights = ['文化体验', '自然风光', '美食探索', '行程丰富', '适合深度游']
      }
    }
    
    // 添加AI生成的特色标识
    highlights.push('AI智能定制', '个性化推荐', '行程优化')
    
    aiResult.value = {
      title,
      description,
      itinerary,
      highlights
    }
  }, 1500)
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