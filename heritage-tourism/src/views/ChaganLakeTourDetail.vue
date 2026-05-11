<template>
  <div class="tour-route-detail">

    <div class="container">
      <!-- 路线主信息 -->
      <section class="route-main">
        <div class="route-header">
          <h1>查干湖冬捕 3 日游</h1>
          <div class="route-tags">
            <span class="tag tag-orange">非遗主题</span>
            <span class="tag tag-blue">文化体验</span>
            <span class="tag tag-green">三日游</span>
          </div>
          <div class="route-price">
            <span class="price">¥988 / 人起</span>
            <span class="duration">3 天</span>
          </div>
          <div class="route-stats">
            <span class="rating">⭐⭐⭐⭐⭐ 4.9 (1280条评价)</span>
            <span class="sales">已售 2560 份</span>
          </div>
        </div>
        <div class="route-images">
          <div class="main-image">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20Jilin%20traditional%20custom&image_size=landscape_16_9" alt="查干湖冬捕 3 日游" />
          </div>
          <div class="gallery">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20net%20pulling&image_size=portrait_4_3" alt="查干湖冬捕拉网" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20ceremony&image_size=portrait_4_3" alt="查干湖冬捕仪式" />
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20fish%20from%20Chagan%20Lake&image_size=portrait_4_3" alt="查干湖鲜鱼" />
            <img :src="chaganhu1" alt="查干湖冬景" />
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
            <h3>查干湖冬捕开网仪式</h3>
          </div>
          <div class="day-content">
            <div class="time-slot">
              <div class="time">08:00 - 10:00</div>
              <div class="activity">
                <h4>集合出发</h4>
                <p>指定地点集合，乘坐舒适旅游大巴前往查干湖</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">10:00 - 12:30</div>
              <div class="activity">
                <h4>抵达查干湖，入住酒店</h4>
                <p>办理入住手续，稍作休息</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">12:30 - 14:00</div>
              <div class="activity">
                <h4>查干湖特色午餐</h4>
                <p>品尝查干湖特色美食，如全鱼宴、东北农家菜等（推荐：查干湖胖头鱼、铁锅炖鱼）</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">14:00 - 16:00</div>
              <div class="activity">
                <h4>查干湖冬捕文化体验</h4>
                <p>参观查干湖冬捕博物馆，了解冬捕历史文化，学习冬捕知识</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">16:00 - 18:00</div>
              <div class="activity">
                <h4>查干湖冬景游览</h4>
                <p>欣赏查干湖冬季风光，拍照留念</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">18:00 - 20:00</div>
              <div class="activity">
                <h4>查干湖特色晚餐</h4>
                <p>品尝查干湖特色晚餐，如鱼宴、东北菜等</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 第二天 -->
        <div class="day-itinerary">
          <div class="day-header">
            <span class="day-number">DAY 2</span>
            <h3>查干湖冬捕体验日</h3>
          </div>
          <div class="day-content">
            <div class="time-slot">
              <div class="time">06:00 - 08:00</div>
              <div class="activity">
                <h4>早起观看冬捕</h4>
                <p>前往冬捕现场，观看渔民凿冰、下网、拉网的全过程</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">08:00 - 09:30</div>
              <div class="activity">
                <h4>冬捕开网仪式</h4>
                <p>观看传统的冬捕开网仪式，感受渔猎文化的魅力</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">09:30 - 11:30</div>
              <div class="activity">
                <h4>体验冬捕</h4>
                <p>在渔民的指导下，体验冬捕的乐趣，感受传统渔猎文化</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">11:30 - 13:00</div>
              <div class="activity">
                <h4>查干湖特色午餐</h4>
                <p>品尝刚捕捞的新鲜鱼，享受查干湖特色美食</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">13:00 - 15:00</div>
              <div class="activity">
                <h4>冬捕文化体验</h4>
                <p>参与冬捕相关的传统活动，如冰上垂钓、冰雕制作等</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">15:00 - 17:00</div>
              <div class="activity">
                <h4>查干湖周边游览</h4>
                <p>游览查干湖周边景点，如妙因寺、郭尔罗斯王府等</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">17:00 - 19:00</div>
              <div class="activity">
                <h4>查干湖特色晚餐</h4>
                <p>品尝查干湖特色晚餐，如鱼宴、东北菜等</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 第三天 -->
        <div class="day-itinerary">
          <div class="day-header">
            <span class="day-number">DAY 3</span>
            <h3>返程</h3>
          </div>
          <div class="day-content">
            <div class="time-slot">
              <div class="time">08:00 - 09:30</div>
              <div class="activity">
                <h4>早餐</h4>
                <p>享用酒店早餐</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">09:30 - 11:30</div>
              <div class="activity">
                <h4>自由活动</h4>
                <p>自由活动，购买查干湖特色纪念品，如鱼干、冬捕相关文创产品等</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">11:30 - 13:00</div>
              <div class="activity">
                <h4>查干湖特色午餐</h4>
                <p>最后一次品尝查干湖特色美食</p>
              </div>
            </div>
            <div class="time-slot">
              <div class="time">13:00 - 15:00</div>
              <div class="activity">
                <h4>返程</h4>
                <p>乘坐大巴返回市区，结束愉快的查干湖冬捕之旅</p>
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
              <span>🎣</span>
            </div>
            <h3>查干湖冬捕</h3>
            <p>国家级非物质文化遗产，历史悠久，是中国北方渔猎文化的重要组成部分</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>🏺</span>
            </div>
            <h3>冬捕开网仪式</h3>
            <p>传统的祭湖醒网仪式，具有浓厚的萨满文化色彩，是冬捕文化的重要环节</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>🐟</span>
            </div>
            <h3>查干湖鱼文化</h3>
            <p>查干湖鱼类资源丰富，鱼文化历史悠久，是吉林特色文化的重要组成部分</p>
          </div>
          <div class="highlight-item">
            <div class="highlight-icon">
              <span>❄️</span>
            </div>
            <h3>东北冬季民俗</h3>
            <p>体验东北冬季特色民俗，如冰上活动、雪地游戏等</p>
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
              <li>查干湖景区门票</li>
              <li>2晚住宿（查干湖特色酒店）</li>
              <li>5餐（3早餐2午餐2晚餐）</li>
              <li>冬捕体验活动费用</li>
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
              <li>退改政策：出发前3天可全额退款，出发前2天退款50%，出发当天不退款</li>
              <li>建议穿着保暖衣物，如羽绒服、保暖裤、防滑鞋等</li>
              <li>请携带身份证等有效证件</li>
              <li>冬季查干湖气温较低，请做好防寒保暖措施</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- 用户评价 -->
      <section class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-header">
          <div class="rating-overall">
            <span class="rating-score">4.9</span>
            <span class="rating-stars">⭐⭐⭐⭐⭐</span>
            <span class="rating-count">1280条评价</span>
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
                  <span class="user-name">@旅行爱好者</span>
                  <span class="review-date">2026-04-10</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>查干湖冬捕太震撼了！第一次看到那么大规模的冬捕，渔民们凿冰、下网、拉网的过程非常壮观。开网仪式也很有特色，充满了神秘的萨满文化色彩。住的酒店很舒适，吃的鱼也非常新鲜，特别是刚捕捞上来的胖头鱼，味道鲜美。导游讲解很专业，全程服务周到。非常推荐！</p>
              <div class="review-images">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20ceremony&image_size=portrait_4_3" alt="冬捕仪式" />
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20fish%20from%20Chagan%20Lake&image_size=portrait_4_3" alt="鲜鱼" />
              </div>
            </div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@摄影爱好者</span>
                  <span class="review-date">2026-04-08</span>
                </div>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <div class="review-content">
              <p>查干湖的冬季风光太美了！湖面结冰后一片雪白，非常适合拍照。冬捕的过程非常壮观，特别是拉网的时候，很多鱼被拉上来，场面很震撼。住的酒店暖气很足，吃的鱼也非常新鲜。导游很热情，讲解详细，推荐大家来体验一下查干湖冬捕的魅力！</p>
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
              <p>带孩子一起参加的，孩子非常喜欢冬捕体验。看到那么多鱼被拉上来，孩子很兴奋。导游对孩子也很有耐心，讲解生动有趣。行程安排合理，不会太赶，适合家庭出游。住的酒店很舒适，吃的鱼也非常新鲜，特别是铁锅炖鱼，非常好吃。</p>
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
          <h3>预订查干湖冬捕 3 日游</h3>
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
  date: '',
  guests: 1,
  notes: '',
  agree: false
})

// AI路线定制表单
const aiForm = ref({
  days: '3',
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
    item: '查干湖冬捕 3 日游',
    price: 988,
    totalPrice: 988 * bookingForm.value.guests,
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
      title = '查干湖冬捕一日游'
      description = '体验查干湖冬捕文化，感受渔猎传统'
      itinerary = [
        {
          activities: [
            '08:00 - 出发前往查干湖',
            '10:00 - 抵达查干湖，参观冬捕博物馆',
            '12:00 - 品尝查干湖特色午餐（推荐：全鱼宴、铁锅炖鱼）',
            '13:30 - 观看冬捕过程',
            '15:30 - 体验冰上活动',
            '17:00 - 返程'
          ]
        }
      ]
      highlights = ['冬捕文化体验', '冰上活动', '特色美食']
    } else if (days === '2') {
      title = '查干湖冬捕二日游'
      description = '深入体验查干湖冬捕文化和东北冬季民俗'
      itinerary = [
        {
          activities: [
            '08:00 - 出发前往查干湖',
            '10:00 - 抵达查干湖，入住酒店',
            '12:00 - 品尝查干湖特色午餐（推荐：全鱼宴）',
            '13:30 - 参观冬捕博物馆',
            '15:00 - 观看冬捕过程',
            '17:00 - 品尝查干湖特色晚餐',
            '18:30 - 参加篝火晚会'
          ]
        },
        {
          activities: [
            '07:00 - 观看冬捕开网仪式',
            '09:00 - 体验冬捕',
            '11:00 - 品尝查干湖特色早餐',
            '12:00 - 游览查干湖周边景点',
            '14:00 - 购买特色纪念品',
            '15:00 - 返程'
          ]
        }
      ]
      highlights = ['冬捕开网仪式', '冬捕体验', '篝火晚会', '特色美食']
    } else {
      title = '查干湖冬捕深度之旅'
      description = '全方位体验查干湖冬捕文化和东北冬季民俗'
      itinerary = [
        {
          activities: [
            '08:00 - 出发前往查干湖',
            '10:00 - 抵达查干湖，入住酒店',
            '12:00 - 品尝查干湖特色午餐（推荐：全鱼宴）',
            '13:30 - 参观冬捕博物馆',
            '15:00 - 观看冬捕过程',
            '17:00 - 品尝查干湖特色晚餐',
            '18:30 - 参加篝火晚会'
          ]
        },
        {
          activities: [
            '06:00 - 观看冬捕开网仪式',
            '08:00 - 体验冬捕',
            '10:00 - 品尝查干湖特色早餐',
            '11:00 - 体验冰上活动',
            '12:30 - 品尝查干湖特色午餐',
            '14:00 - 游览查干湖周边景点',
            '17:00 - 品尝查干湖特色晚餐'
          ]
        },
        {
          activities: [
            '08:00 - 早餐后自由活动',
            '10:00 - 购买特色纪念品',
            '12:00 - 最后一次品尝查干湖特色午餐',
            '13:30 - 返程'
          ]
        }
      ]
      highlights = ['冬捕开网仪式', '冬捕体验', '冰上活动', '篝火晚会', '特色美食']
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
            day.activities.push(`${14 + index}:00 - 参观查干湖冬捕博物馆，了解冬捕历史文化`)
          } else if (index === 1) {
            day.activities.push(`${14 + index}:00 - 体验东北传统民俗活动`)
          } else {
            day.activities.push(`${14 + index}:00 - 参观郭尔罗斯王府，了解蒙古族文化`)
          }
        })
      }
      
      if (interests.includes('自然风光')) {
        // 在每天的行程中添加自然景观
        itinerary.forEach((day, index) => {
          if (index === 0) {
            day.activities.push(`${15 + index}:00 - 欣赏查干湖冬季风光，拍照留念`)
          } else if (index === 1) {
            day.activities.push(`${15 + index}:00 - 游览查干湖周边自然景观`)
          } else {
            day.activities.push(`${15 + index}:00 - 欣赏东北平原冬季风光`)
          }
        })
      }
      
      if (interests.includes('美食探索')) {
        // 在每天的行程中添加美食体验
        itinerary.forEach((day, index) => {
          if (index === 0) {
            day.activities.push(`${16 + index}:00 - 品尝查干湖特色小吃，如鱼干、东北大煎饼`)
          } else if (index === 1) {
            day.activities.push(`${16 + index}:00 - 学习制作东北特色美食，如酸菜炖粉条`)
          } else {
            day.activities.push(`${16 + index}:00 - 品尝吉林特色美食，如锅包肉、煎粉`)
          }
        })
      }
      
      if (interests.includes('休闲度假')) {
        // 在每天的行程中添加休闲活动
        itinerary.forEach((day, index) => {
          if (index === 0) {
            day.activities.push(`${17 + index}:00 - 体验东北传统汗蒸，放松身心`)
          } else if (index === 1) {
            day.activities.push(`${17 + index}:00 - 参加东北传统娱乐活动，如二人转表演`)
          } else {
            day.activities.push(`${17 + index}:00 - 自由活动，享受休闲时光`)
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