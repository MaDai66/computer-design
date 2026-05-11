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
              <button class="btn btn-secondary" @click="openRoomBookingModal(room.name, room.price)">预订</button>
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
              <button class="btn btn-secondary" @click="openExperienceBookingModal(experience.name, experience.price)">预约</button>
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

const router = useRouter()
const route = useRoute()

// 农家院数据
const homestaysData = [
  {
    id: 1,
    name: '长白山脚下农家院',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Traditional%20Chinese%20farmhouse%20at%20the%20foot%20of%20Changbai%20Mountain&image_size=landscape_16_9',
    images: [
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Traditional%20Chinese%20farmhouse%20at%20the%20foot%20of%20Changbai%20Mountain&image_size=landscape_16_9',
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Farmhouse%20interior%20traditional%20Chinese%20style&image_size=landscape_16_9',
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Farmhouse%20garden%20with%20traditional%20Chinese%20elements&image_size=landscape_16_9',
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Farmhouse%20dining%20area%20traditional%20Chinese%20cuisine&image_size=landscape_16_9'
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
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Traditional%20Chinese%20room%20with%20kang%20bed&image_size=portrait_4_3',
        description: '传统火炕，可住2-4人，独立卫浴，空调，WiFi',
        price: 280,
        capacity: '2-4人'
      },
      {
        name: '山景房',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Deluxe%20traditional%20Chinese%20room%20mountain%20view&image_size=portrait_4_3',
        description: '落地窗山景，可住2人，独立卫浴，空调，WiFi',
        price: 320,
        capacity: '2人'
      },
      {
        name: '家庭房',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Family%20room%20traditional%20Chinese%20style&image_size=portrait_4_3',
        description: '宽敞空间，可住4-6人，独立卫浴，空调，WiFi',
        price: 480,
        capacity: '4-6人'
      }
    ],
    experiences: [
      {
        name: '满族剪纸教学',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20workshop%20traditional%20craft&image_size=portrait_4_3',
        description: '由当地非遗传承人教授满族传统剪纸技艺，可带走自己的作品。',
        duration: '1.5小时',
        price: 68
      },
      {
        name: '满族火锅体验',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20hot%20pot%20traditional%20cuisine&image_size=portrait_4_3',
        description: '品尝正宗满族火锅，了解满族饮食文化和传统烹饪方法。',
        duration: '2小时',
        price: 128
      }
    ],
    reviews: [
      {
        user: '@旅行爱好者',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture&image_size=portrait_4_3',
        rating: 5,
        content: '农家院环境非常好，干净整洁，老板热情好客。火炕很舒服，晚上睡得很香。早餐是正宗的农家菜，味道很棒。离长白山景区很近，交通方便。强烈推荐！',
        date: '2026-04-10'
      },
      {
        user: '@家庭出游',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3',
        rating: 5,
        content: '带家人来长白山旅游，选择了这家农家院。房间宽敞，设施齐全，孩子们很喜欢火炕。老板还安排了满族剪纸体验，非常有特色。下次来还会住这里。',
        date: '2026-04-08'
      },
      {
        user: '@摄影爱好者',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3',
        rating: 5,
        content: '农家院的位置绝佳，是拍摄长白山的好地方。房间干净舒适，老板很热情，给我们推荐了很多拍摄点。晚上在院子里还能看到星空，非常美丽。',
        date: '2026-04-05'
      }
    ]
  },
  {
    id: 2,
    name: '松花湖生态农家院',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Eco%20farmhouse%20by%20Songhua%20Lake&image_size=landscape_16_9',
    images: [
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Eco%20farmhouse%20by%20Songhua%20Lake&image_size=landscape_16_9',
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Lake%20view%20farmhouse%20interior&image_size=landscape_16_9',
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Eco%20garden%20at%20farmhouse&image_size=landscape_16_9',
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20seafood%20dining%20at%20farmhouse&image_size=landscape_16_9'
    ],
    rating: 4.6,
    location: '松花湖景区',
    distance: 10,
    hasHeritage: true,
    selfOperated: true,
    hot: false,
    description: '松花湖边的生态农家院，提供传统渔业体验，湖景房。',
    price: 320,
    rooms: [
      {
        name: '湖景房',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Lake%20view%20room%20traditional%20style&image_size=portrait_4_3',
        description: '落地窗湖景，可住2-3人，独立卫浴，空调，WiFi',
        price: 320,
        capacity: '2-3人'
      },
      {
        name: '家庭湖景房',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Family%20lake%20view%20room&image_size=portrait_4_3',
        description: '宽敞湖景，可住4-5人，独立卫浴，空调，WiFi',
        price: 450,
        capacity: '4-5人'
      }
    ],
    experiences: [
      {
        name: '传统渔业体验',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Traditional%20fishing%20experience%20on%20lake&image_size=portrait_4_3',
        description: '跟随当地渔民学习传统捕鱼技艺，体验撒网、收网的乐趣。',
        duration: '2小时',
        price: 88
      },
      {
        name: '湖鲜烹饪体验',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20fish%20cooking%20class&image_size=portrait_4_3',
        description: '使用刚捕获的湖鲜，学习制作正宗的松花湖鱼宴。',
        duration: '1.5小时',
        price: 108
      }
    ],
    reviews: [
      {
        user: '@自然爱好者',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%204&image_size=portrait_4_3',
        rating: 5,
        content: '农家院环境非常生态，周围都是绿色植物，空气清新。房间宽敞明亮，湖景房的视野非常好。老板很热情，给我们安排了捕鱼体验，非常有趣。',
        date: '2026-04-12'
      },
      {
        user: '@美食家',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%205&image_size=portrait_4_3',
        rating: 4,
        content: '湖鲜非常新鲜，味道很棒。房间干净整洁，设施齐全。唯一的不足是离市区有点远，但环境确实很好，适合度假。',
        date: '2026-04-09'
      }
    ]
  },
  {
    id: 3,
    name: '朝鲜族民俗村农家院',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20ethnic%20village%20traditional%20farmhouse%20with%20hanok%20style%20architecture&image_size=landscape_16_9',
    images: [
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20ethnic%20village%20traditional%20farmhouse%20with%20hanok%20style%20architecture&image_size=landscape_16_9'
    ],
    rating: 4.9,
    location: '朝鲜族民俗村',
    distance: 15,
    hasHeritage: true,
    selfOperated: true,
    hot: true,
    description: '朝鲜族特色农家院，提供打糕制作、朝鲜服装体验，正宗朝鲜美食。',
    price: 260,
    rooms: [
      {
        name: '韩式火炕房',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20style%20ondol%20room&image_size=portrait_4_3',
        description: '传统韩式火炕，可住2-4人，独立卫浴，空调，WiFi',
        price: 260,
        capacity: '2-4人'
      },
      {
        name: '韩式客房',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20style%20guest%20room&image_size=portrait_4_3',
        description: '韩式风格客房，可住2人，独立卫浴，空调，WiFi',
        price: 280,
        capacity: '2人'
      }
    ],
    experiences: [
      {
        name: '打糕制作体验',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20rice%20cake%20making%20workshop&image_size=portrait_4_3',
        description: '学习制作正宗朝鲜族打糕，体验传统捣糕工艺。',
        duration: '1小时',
        price: 58
      },
      {
        name: '朝鲜服装体验',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20traditional%20clothing%20experience&image_size=portrait_4_3',
        description: '穿上正宗朝鲜服装，在民俗村拍照留念。',
        duration: '1.5小时',
        price: 68
      },
      {
        name: '朝鲜美食制作',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20cuisine%20cooking%20class&image_size=portrait_4_3',
        description: '学习制作正宗朝鲜泡菜、烤肉等传统美食。',
        duration: '2小时',
        price: 98
      }
    ],
    reviews: [
      {
        user: '@文化爱好者',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%206&image_size=portrait_4_3',
        rating: 5,
        content: '非常有特色的朝鲜族农家院，老板是朝鲜族，非常热情。打糕制作体验很有趣，味道也很棒。房间干净整洁，朝鲜风格很地道。强烈推荐！',
        date: '2026-04-11'
      },
      {
        user: '@摄影爱好者',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%207&image_size=portrait_4_3',
        rating: 5,
        content: '民俗村的环境非常适合拍照，穿上朝鲜服装拍出来的照片非常漂亮。农家院的饭菜很正宗，尤其是泡菜和烤肉。房间舒适，服务周到。',
        date: '2026-04-07'
      },
      {
        user: '@家庭出游',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%208&image_size=portrait_4_3',
        rating: 5,
        content: '孩子们非常喜欢打糕制作和朝鲜服装体验，玩得很开心。农家院的环境干净整洁，饭菜味道好。老板很热情，还给我们讲了很多朝鲜族的文化和历史。',
        date: '2026-04-04'
      }
    ]
  },
  {
    id: 4,
    name: '查干湖冬捕农家院',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20traditional%20farmhouse%20with%20ice%20fishing%20scene&image_size=landscape_16_9',
    images: [
      'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20traditional%20farmhouse%20with%20ice%20fishing%20scene&image_size=landscape_16_9'
    ],
    rating: 4.7,
    location: '查干湖景区',
    distance: 20,
    hasHeritage: true,
    selfOperated: true,
    hot: true,
    description: '查干湖边的农家院，冬季提供冬捕体验，特色鱼宴。',
    price: 300,
    rooms: [
      {
        name: '暖炕房',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Warm%20kang%20room%20in%20winter&image_size=portrait_4_3',
        description: '传统暖炕，可住2-4人，独立卫浴，暖气，WiFi',
        price: 300,
        capacity: '2-4人'
      },
      {
        name: '豪华暖炕房',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Deluxe%20warm%20room%20winter&image_size=portrait_4_3',
        description: '宽敞暖炕，可住4-6人，独立卫浴，暖气，WiFi',
        price: 420,
        capacity: '4-6人'
      }
    ],
    experiences: [
      {
        name: '冬捕体验',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20traditional%20winter%20fishing%20on%20frozen%20lake%20with%20fishermen&image_size=portrait_4_3',
        description: '参与查干湖传统冬捕，体验冰上捕鱼的乐趣。',
        duration: '3小时',
        price: 168
      },
      {
        name: '鱼宴品尝',
        image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Fresh%20fish%20feast%20traditional%20style%20Chagan%20Lake&image_size=portrait_4_3',
        description: '品尝查干湖特色鱼宴，包括多种做法的鲜鱼。',
        duration: '2小时',
        price: 138
      }
    ],
    reviews: [
      {
        user: '@冬季旅游爱好者',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%209&image_size=portrait_4_3',
        rating: 5,
        content: '冬捕体验非常棒，第一次在冰面上捕鱼，非常新鲜刺激。农家院的暖炕很舒服，晚上睡在上面很暖和。鱼宴的味道非常鲜美，推荐大家来体验。',
        date: '2026-03-28'
      },
      {
        user: '@美食爱好者',
        avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%2010&image_size=portrait_4_3',
        rating: 4,
        content: '鱼宴非常美味，特别是查干湖的胖头鱼，肉质鲜嫩。冬捕体验很有趣，但需要注意保暖。农家院的环境干净整洁，服务周到。',
        date: '2026-03-25'
      }
    ]
  }
]

// 获取当前农家院详情
const currentHomestay = computed(() => {
  const id = parseInt(route.params.id) || 1
  return homestaysData.find(homestay => homestay.id === id) || homestaysData[0]
})

const showBackToTop = ref(false)

// 房间预订相关状态
const showRoomBookingModal = ref(false)
const selectedRoom = ref('')
const selectedRoomPrice = ref(0)
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
const experienceBooking = ref({
  date: '',
  time: '09:00-10:30',
  participants: 1,
  name: '',
  phone: '',
  notes: ''
})

// 打开房间预订模态框
const openRoomBookingModal = (room, price) => {
  selectedRoom.value = room
  selectedRoomPrice.value = price
  showRoomBookingModal.value = true
}

// 打开体验预约模态框
const openExperienceBookingModal = (experience, price) => {
  selectedExperience.value = experience
  selectedExperiencePrice.value = price
  showExperienceBookingModal.value = true
}

// 提交房间预订
const submitRoomBooking = () => {
  // 计算入住天数
  const checkInDate = new Date(roomBooking.value.checkIn)
  const checkOutDate = new Date(roomBooking.value.checkOut)
  const days = Math.ceil((checkOutDate - checkInDate) / (1000 * 60 * 60 * 24))
  
  // 计算总价
  const totalPrice = selectedRoomPrice.value * days
  
  // 生成订单ID
  const orderId = 'ORD' + Date.now()
  
  // 创建订单对象
  const order = {
    id: orderId,
    type: 'room',
    item: selectedRoom.value,
    price: selectedRoomPrice.value,
    totalPrice: totalPrice,
    checkIn: roomBooking.value.checkIn,
    checkOut: roomBooking.value.checkOut,
    guests: roomBooking.value.guests,
    name: roomBooking.value.name,
    phone: roomBooking.value.phone,
    notes: roomBooking.value.notes,
    status: 'pending',
    createdAt: new Date().toISOString()
  }
  
  // 保存订单到localStorage
  saveOrder(order)
  
  // 关闭模态框
  showRoomBookingModal.value = false
  
  // 跳转到我的页面
  router.push('/profile')
}

// 提交体验预约
const submitExperienceBooking = () => {
  // 计算总价
  const totalPrice = selectedExperiencePrice.value * experienceBooking.value.participants
  
  // 生成订单ID
  const orderId = 'ORD' + Date.now()
  
  // 创建订单对象
  const order = {
    id: orderId,
    type: 'experience',
    item: selectedExperience.value,
    price: selectedExperiencePrice.value,
    totalPrice: totalPrice,
    date: experienceBooking.value.date,
    time: experienceBooking.value.time,
    participants: experienceBooking.value.participants,
    name: experienceBooking.value.name,
    phone: experienceBooking.value.phone,
    notes: experienceBooking.value.notes,
    status: 'pending',
    createdAt: new Date().toISOString()
  }
  
  // 保存订单到localStorage
  saveOrder(order)
  
  // 关闭模态框
  showExperienceBookingModal.value = false
  
  // 跳转到我的页面
  router.push('/profile')
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