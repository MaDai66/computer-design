<template>
  <div class="home">
    <!-- 顶部轮播Banner -->
    <section class="banner">
      <div class="banner-slider">
        <router-link v-for="(slide, index) in slides" :key="slide.id" :to="slide.path" class="banner-slide" :class="{ active: index === 1 }">
          <img :src="slide.image" :alt="slide.title" />
          <div class="banner-content">
            <h1>{{ slide.title }}</h1>
            <p>{{ slide.description }}</p>
          </div>
        </router-link>
      </div>
      <div class="banner-dots">
        <span v-for="(slide, index) in originalSlides" :key="slide.id" class="dot" :class="{ active: currentIndex === index }" @click="showSlide(index)"></span>
      </div>
    </section>

    <!-- 智能推荐区 -->
    <section class="smart-recommend">
      <div class="container">
        <div class="section-header">
          <h2>为你精选</h2>
        </div>
        <div class="recommend-cards">
          <router-link to="/heritage-experience-detail" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20Korean%20rice%20cake%20making%20experience%20traditional%20craft&image_size=portrait_4_3" alt="朝鲜族打糕体验" />
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-red">手作体验</span>
                  <span class="tag tag-green">推荐</span>
                </div>
                <h3>朝鲜族打糕制作体验</h3>
                <p>亲手体验传统打糕制作，感受朝鲜族饮食文化</p>
                <div class="card-footer">
                  <span class="price">¥88/人</span>
                  <button class="btn btn-secondary">预订</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/homestay-detail/1" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20traditional%20farmhouse%20stay%20rural%20accommodation&image_size=portrait_4_3" alt="农家院住宿" />
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">农家台屋</span>
                  <span class="tag tag-blue">热宿</span>
                </div>
                <h3>长白山脚下农家院</h3>
                <p>体验乡村生活，感受自然之美</p>
                <div class="card-footer">
                  <span class="price">¥280/晚</span>
                  <button class="btn btn-secondary">预订</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/product-detail/1" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20art%20traditional%20craft%20Jilin&image_size=portrait_4_3" alt="剪纸文创" />
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-orange">文创产品</span>
                  <span class="tag tag-blue">满减</span>
                </div>
                <h3>满族剪纸艺术套装</h3>
                <p>传统剪纸工艺，精美文创礼品</p>
                <div class="card-footer">
                  <span class="price">¥128</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    <!-- 非遗主题游 -->
    <section class="heritage-tour">
      <div class="container">
        <div class="section-header">
          <h2>非遗主题游</h2>
        </div>
        <div class="tour-grid">
          <router-link to="/tour-route-detail" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbai%20Mountain%20Manchu%20cultural%20tour%20Jilin%20heritage&image_size=landscape_16_9" alt="长白山满族寻根游" />
              <div class="card-content">
                <h3>长白山满族寻根2日游</h3>
                <div class="tour-info">
                  <span class="tour-days">2天1晚</span>
                  <span class="tour-experience">3个非遗体验点</span>
                </div>
                <p>探访满族发源地，体验传统手工艺</p>
                <div class="card-footer">
                  <span class="price">¥688/人起</span>
                  <button class="btn btn-secondary">查看详情</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/korean-village-tour-detail" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20ethnic%20village%20Jilin%20traditional%20culture%20tour&image_size=landscape_16_9" alt="朝鲜族民俗村游" />
              <div class="card-content">
                <h3>朝鲜族民俗村1日游</h3>
                <div class="tour-info">
                  <span class="tour-days">1天</span>
                  <span class="tour-experience">4个非遗体验点</span>
                </div>
                <p>感受朝鲜族传统文化，品尝特色美食</p>
                <div class="card-footer">
                  <span class="price">¥298/人起</span>
                  <button class="btn btn-secondary">查看详情</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/chagan-lake-tour-detail" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20Jilin%20traditional%20custom&image_size=landscape_16_9" alt="查干湖冬捕游" />
              <div class="card-content">
                <h3>查干湖冬捕3日游</h3>
                <div class="tour-info">
                  <span class="tour-days">3天2晚</span>
                  <span class="tour-experience">2个非遗体验点</span>
                </div>
                <p>体验千年冬捕文化，感受北国风光</p>
                <div class="card-footer">
                  <span class="price">¥988/人起</span>
                  <button class="btn btn-secondary">查看详情</button>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    <!-- 即将开始的活动 -->
    <section class="upcoming-events">
      <div class="container">
        <div class="section-header">
          <h2>即将开始的活动</h2>
        </div>
        <div class="events-list">
          <router-link to="/chagan-lake-opening-ceremony" class="event-link">
            <div class="event-card">
              <div class="event-date">
                <span class="event-day">15</span>
                <span class="event-month">4月</span>
              </div>
              <div class="event-content">
                <h3>查干湖冬捕开网仪式</h3>
                <p>体验千年冬捕文化，见证丰收时刻</p>
                <div class="event-info">
                  <span class="event-time">08:00-12:00</span>
                  <span class="event-location">查干湖景区</span>
                </div>
                <button class="btn btn-primary">立即预订</button>
              </div>
            </div>
          </router-link>
          <router-link to="/heritage-experience-detail" class="event-link">
            <div class="event-card">
              <div class="event-date">
                <span class="event-day">20</span>
                <span class="event-month">4月</span>
              </div>
              <div class="event-content">
                <h3>朝鲜族打糕制作体验</h3>
                <p>亲手制作传统打糕，感受朝鲜族饮食文化</p>
                <div class="event-info">
                  <span class="event-time">14:00-16:00</span>
                  <span class="event-location">朝鲜族民俗村</span>
                </div>
                <button class="btn btn-primary">立即预订</button>
              </div>
            </div>
          </router-link>
          <router-link to="/paper-cutting-detail" class="event-link">
            <div class="event-card">
              <div class="event-date">
                <span class="event-day">25</span>
                <span class="event-month">4月</span>
              </div>
              <div class="event-content">
                <h3>满族剪纸艺术工作坊</h3>
                <p>学习传统剪纸技艺，创作个性化作品</p>
                <div class="event-info">
                  <span class="event-time">10:00-12:00</span>
                  <span class="event-location">长白山满族文化园</span>
                </div>
                <button class="btn btn-primary">立即预订</button>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    <!-- 助农好物推荐 -->
    <section class="agricultural-products">
      <div class="container">
        <div class="section-header">
          <h2>助农好物推荐</h2>
        </div>
        <div class="products-grid">
          <router-link to="/ginseng-product-detail" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbai%20Mountain%20wild%20ginseng%20Jilin%20natural%20herb%20traditional%20medicine&image_size=portrait_4_3" alt="长白山野生人参" />
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">原产地</span>
                  <span class="tag tag-orange">助农</span>
                </div>
                <h3>长白山野生人参</h3>
                <p>地道长白山特产，营养丰富</p>
                <div class="card-footer">
                  <span class="price">¥298/盒</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/corn-product-detail" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20organic%20corn%20agricultural%20products&image_size=portrait_4_3" alt="吉林玉米" />
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">原产地</span>
                  <span class="tag tag-orange">助农</span>
                </div>
                <h3>吉林有机玉米</h3>
                <p>无污染有机种植，口感香甜</p>
                <div class="card-footer">
                  <span class="price">¥39.9/5斤</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/honey-product-detail" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbai%20Mountain%20natural%20honey%20Jilin%20agricultural%20product&image_size=portrait_4_3" alt="吉林蜂蜜" />
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">原产地</span>
                  <span class="tag tag-orange">助农</span>
                </div>
                <h3>长白山天然蜂蜜</h3>
                <p>采自长白山原始森林，纯天然无添加</p>
                <div class="card-footer">
                  <span class="price">¥88/瓶</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/kimchi-product-detail" class="card-link">
            <div class="card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20traditional%20kimchi%20Jilin%20fermented%20food&image_size=portrait_4_3" alt="朝鲜族泡菜" />
              <div class="card-content">
                <div class="card-tags">
                  <span class="tag tag-green">原产地</span>
                  <span class="tag tag-orange">助农</span>
                </div>
                <h3>朝鲜族传统泡菜</h3>
                <p>传统工艺制作，酸辣可口</p>
                <div class="card-footer">
                  <span class="price">¥45/瓶</span>
                  <button class="btn btn-secondary">购买</button>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    <!-- 用户足迹/社区 -->
    <section class="user-community">
      <div class="container">
        <div class="section-header">
          <h2>用户足迹</h2>
        </div>
        <div class="community-grid">
          <router-link to="/travel-note-detail" class="community-link">
            <div class="community-card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Traveler%20taking%20photo%20of%20Changbai%20Mountain%20Jilin%20scenery&image_size=portrait_4_3" alt="用户游记" />
              <div class="community-content">
                <h3>长白山之旅</h3>
                <p class="user-name">@旅行含小明</p>
                <p>太美了！长白山的雪景令人震撼，非遗体验也很有趣。</p>
                <div class="community-actions">
                  <button class="action-btn">
                    <span>❤️</span>
                    <span>128</span>
                  </button>
                  <button class="action-btn">
                    <span>💬</span>
                    <span>32</span>
                  </button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/korean-rice-cake-note-detail" class="community-link">
            <div class="community-card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20experience%20Korean%20rice%20cake%20making%20Jilin%20traditional%20craft&image_size=portrait_4_3" alt="用户体验" />
              <div class="community-content">
                <h3>朝鲜族打糕体验</h3>
                <p class="user-name">@美食爱好者</p>
                <p>第一次体验打糕制作，很有趣，味道也很棒！</p>
                <div class="community-actions">
                  <button class="action-btn">
                    <span>❤️</span>
                    <span>89</span>
                  </button>
                  <button class="action-btn">
                    <span>💬</span>
                    <span>15</span>
                  </button>
                </div>
              </div>
            </div>
          </router-link>
          <router-link to="/homestay-experience-note-detail" class="community-link">
            <div class="community-card">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20staying%20in%20traditional%20farmhouse%20Jilin%20rural%20accommodation&image_size=portrait_4_3" alt="用户住宿" />
              <div class="community-content">
                <h3>农家院住宿体验</h3>
                <p class="user-name">@城市逃离者</p>
                <p>远离城市喧嚣，感受乡村宁静，太惬意了！</p>
                <div class="community-actions">
                  <button class="action-btn">
                    <span>❤️</span>
                    <span>156</span>
                  </button>
                  <button class="action-btn">
                    <span>💬</span>
                    <span>42</span>
                  </button>
                </div>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import dongbu from '@/assets/冬捕.jpg'
import jianzhi from '@/assets/剪纸.jpg'
import nonglew from '@/assets/农乐舞.jpg'

// 原始幻灯片数据
const originalSlides = ref([
  {
    id: 1,
    image: dongbu,
    title: '冬捕千年 · 吉地有礼',
    description: '探索吉林非遗文化与乡村旅游的独特魅力',
    path: '/activity-detail'
  },
  {
    id: 2,
    image: jianzhi,
    title: '剪纸艺术 · 传承千年',
    description: '体验满族传统剪纸技艺，感受民间艺术魅力',
    path: '/paper-cutting-detail'
  },
  {
    id: 3,
    image: nonglew,
    title: '农乐舞韵 · 民族风情',
    description: '感受朝鲜族传统农乐舞，体验民族文化魅力',
    path: '/nongak-dance-detail'
  }
])

const currentIndex = ref(0)
const showBackToTop = ref(false)

// 计算当前显示的幻灯片，确保当前幻灯片在中间
const slides = computed(() => {
  const result = []
  const total = originalSlides.value.length
  
  // 前一张
  const prevIndex = (currentIndex.value - 1 + total) % total
  result.push(originalSlides.value[prevIndex])
  
  // 当前张（中间）
  result.push(originalSlides.value[currentIndex.value])
  
  // 后一张
  const nextIndex = (currentIndex.value + 1) % total
  result.push(originalSlides.value[nextIndex])
  
  return result
})

const showSlide = (index) => {
  currentIndex.value = index
}

const nextSlide = () => {
  currentIndex.value = (currentIndex.value + 1) % originalSlides.value.length
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
  // 自动轮播
  setInterval(nextSlide, 5000)
  
  // 监听滚动事件
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  // 移除滚动事件监听
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Banner */
.banner {
  position: relative;
  height: 400px;
  overflow: hidden;
  margin: 20px 0;
}

.banner-slider {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  gap: 15px;
}

.banner-slide {
  flex: 0 0 25%;
  height: 70%;
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: var(--transition);
  cursor: pointer;
  position: relative;
  box-shadow: var(--shadow);
}

.banner-slide.active {
  flex: 0 0 45%;
  height: 100%;
  z-index: 10;
  box-shadow: var(--shadow-hover);
  order: 2;
}

.banner-slide:nth-child(1):not(.active) {
  order: 1;
}

.banner-slide:nth-child(3):not(.active) {
  order: 3;
}

.banner-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: var(--transition);
}

.banner-content {
  position: absolute;
  bottom: 20px;
  left: 20px;
  right: 20px;
  color: var(--white);
  z-index: 10;
  opacity: 0;
  transition: var(--transition);
}

.banner-slide.active .banner-content {
  opacity: 1;
}

.banner-content h1 {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--white);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.banner-content p {
  font-size: 14px;
  margin-bottom: 12px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.banner-content .btn {
  font-size: 14px;
  padding: 8px 16px;
}

.banner-dots {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 20;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: var(--transition);
}

.dot.active {
  background-color: var(--white);
  transform: scale(1.2);
}

/* Responsive */
@media (max-width: 768px) {
  .banner {
    height: 300px;
    margin: 10px 0;
  }
  
  .banner-slide {
    flex: 0 0 20%;
    height: 60%;
  }
  
  .banner-slide.active {
    flex: 0 0 60%;
    height: 100%;
  }
  
  .banner-content h1 {
    font-size: 16px;
  }
  
  .banner-content p {
    font-size: 10px;
  }
  
  .banner-content .btn {
    font-size: 10px;
    padding: 4px 8px;
  }
}

/* Section Header */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
}

.section-header h2 {
  font-size: 28px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 0;
}

.more-link {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 500;
  transition: var(--transition);
}

.more-link:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

/* Recommend Cards */
.recommend-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.card-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-content {
  padding: 20px;
}

.card-tags {
  margin-bottom: 12px;
}

.card h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.card p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 16px;
  line-height: 1.5;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price {
  font-size: 18px;
  font-weight: 600;
  color: var(--orange);
}

/* Tour Grid */
.tour-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 24px;
}

.tour-info {
  display: flex;
  gap: 16px;
  margin-bottom: 12px;
  font-size: 14px;
  color: var(--text-medium);
}

.tour-days,
.tour-experience {
  display: flex;
  align-items: center;
  gap: 4px;
}

/* Events List */
.events-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.event-card {
  display: flex;
  gap: 20px;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 20px;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.event-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.event-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}

.event-date {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  background-color: var(--primary-color);
  color: var(--white);
  border-radius: var(--radius-md);
  flex-shrink: 0;
}

.event-day {
  font-size: 24px;
  font-weight: 700;
}

.event-month {
  font-size: 14px;
}

.event-content {
  flex: 1;
}

.event-content h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.event-content p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 12px;
}

.event-info {
  display: flex;
  gap: 24px;
  font-size: 14px;
  color: var(--text-light);
  margin-bottom: 16px;
}

.event-time,
.event-location {
  display: flex;
  align-items: center;
  gap: 4px;
}

/* Products Grid */
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

/* Community Grid */
.community-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.community-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.community-card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.community-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.community-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.community-content {
  padding: 20px;
}

.community-content h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.user-name {
  font-size: 14px;
  color: var(--text-light);
  margin-bottom: 12px;
}

.community-actions {
  display: flex;
  gap: 24px;
  margin-top: 16px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 4px;
  background: none;
  border: none;
  color: var(--text-medium);
  cursor: pointer;
  transition: var(--transition);
  font-size: 14px;
}

.action-btn:hover {
  color: var(--primary-color);
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

/* Responsive */
@media (max-width: 768px) {
  .banner {
    height: 400px;
  }
  
  .banner-content {
    left: 20px;
    bottom: 20px;
  }
  
  .banner-content h1 {
    font-size: 32px;
  }
  
  .banner-content p {
    font-size: 16px;
  }
  
  .event-card {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .event-date {
    width: 60px;
    height: 60px;
  }
  
  .event-day {
    font-size: 20px;
  }
  
  .event-month {
    font-size: 12px;
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