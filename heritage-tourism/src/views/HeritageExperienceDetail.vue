<template>
  <div class="heritage-experience-detail">
    <!-- 顶部图片轮播 -->
    <div class="top-banner">
      <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20Korean%20rice%20cake%20making%20experience%20traditional%20craft&image_size=landscape_16_9" alt="朝鲜族打糕制作体验" />
      <div class="banner-content">
        <h1>朝鲜族打糕制作体验</h1>
        <div class="experience-tags">
          <span class="tag tag-red">非遗体验</span>
          <span class="tag tag-green">推荐</span>
          <span class="tag tag-blue">手作体验</span>
        </div>
        <div class="experience-info">
          <span class="price">¥88/人</span>
          <span class="duration">时长：2小时</span>
          <span class="location">地点：朝鲜族民俗村</span>
        </div>
      </div>
    </div>

    <div class="container">
      <!-- 体验介绍 -->
      <section class="experience-intro">
        <h2>体验介绍</h2>
        <div class="intro-content">
          <h3>体验流程</h3>
          <ol>
            <li>传承人讲解朝鲜族打糕的历史和文化背景</li>
            <li>学习打糕制作的基本技巧和注意事项</li>
            <li>亲手体验打糕的制作过程</li>
            <li>品尝自己制作的打糕</li>
            <li>了解打糕的保存方法和食用禁忌</li>
          </ol>
          
          <h3>适合人群</h3>
          <p>适合所有年龄段的游客，尤其适合家庭亲子活动、文化爱好者和美食爱好者。</p>
          
          <h3>体验收获</h3>
          <p>通过亲手制作打糕，了解朝鲜族的饮食文化和传统手工艺，体验劳动的乐趣，收获成就感和美味的打糕。</p>
        </div>
      </section>

      <!-- 传承人信息 -->
      <section class="inheritor-info">
        <h2>传承人信息</h2>
        <div class="inheritor-card">
          <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Elderly%20Korean%20woman%20rice%20cake%20maker%20traditional%20craftsman&image_size=portrait_4_3" alt="金师傅" />
          <div class="inheritor-content">
            <h3>金顺玉 师傅</h3>
            <p class="title">朝鲜族打糕制作技艺传承人</p>
            <p class="bio">金师傅从事打糕制作已有30余年，是朝鲜族打糕制作技艺的代表性传承人。她制作的打糕口感软糯，甜而不腻，深受当地人和游客的喜爱。</p>
            <p class="achievements">曾获得吉林省非物质文化遗产传承人称号，多次在全国非遗展示活动中获奖。</p>
          </div>
        </div>
      </section>

      <!-- 体验地点 -->
      <section class="experience-location">
        <h2>体验地点</h2>
        <div class="location-info">
          <h3>延边朝鲜族自治州朝鲜族民俗村</h3>
          <p>地址：吉林省延边朝鲜族自治州延吉市小营镇光东村朝鲜族民俗村</p>
          <p>交通：从延吉市区乘坐37路公交车到光东村站下车，或自驾导航至"光东村朝鲜族民俗村"</p>

        </div>
      </section>

      <!-- 用户评价 -->
      <section class="user-reviews">
        <h2>用户评价</h2>
        <div class="reviews-list">
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture&image_size=portrait_4_3" alt="用户头像" />
                <span class="user-name">@美食爱好者</span>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <p class="review-content">第一次体验打糕制作，很有趣，味道也很棒！金师傅非常耐心地教我们，学到了很多关于朝鲜族文化的知识。</p>
            <div class="review-date">2026-04-10</div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <span class="user-name">@文化探索者</span>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <p class="review-content">非常棒的体验！不仅学会了制作打糕，还了解了朝鲜族的传统文化。打糕的味道很好，推荐大家来体验。</p>
            <div class="review-date">2026-04-08</div>
          </div>
          <div class="review-item">
            <div class="review-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3" alt="用户头像" />
                <span class="user-name">@亲子游家庭</span>
              </div>
              <div class="review-rating">
                <span>⭐⭐⭐⭐⭐</span>
              </div>
            </div>
            <p class="review-content">带孩子来体验，孩子非常喜欢！金师傅对孩子很有耐心，整个过程充满乐趣，是一次难忘的文化体验。</p>
            <div class="review-date">2026-04-05</div>
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

const showBackToTop = ref(false)

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
.heritage-experience-detail {
  background-color: var(--bg-light);
}

.top-banner {
  position: relative;
  height: 500px;
  overflow: hidden;
}

.top-banner img {
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

.experience-tags {
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

.experience-info {
  display: flex;
  gap: 24px;
  font-size: 16px;
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

/* 体验介绍 */
.intro-content ol {
  list-style: decimal;
  padding-left: 24px;
  margin-bottom: 16px;
}

.intro-content li {
  margin-bottom: 8px;
  line-height: 1.5;
}

.intro-content p {
  line-height: 1.5;
  margin-bottom: 16px;
}

/* 传承人信息 */
.inheritor-card {
  display: flex;
  gap: 24px;
}

.inheritor-card img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: var(--radius-md);
}

.inheritor-content h3 {
  margin-top: 0;
}

.inheritor-content .title {
  font-size: 14px;
  color: var(--primary-color);
  margin-bottom: 12px;
}

.inheritor-content .bio,
.inheritor-content .achievements {
  line-height: 1.5;
  margin-bottom: 12px;
}

/* 体验地点 */
.location-info p {
  margin-bottom: 12px;
}

.location-map img {
  width: 100%;
  border-radius: var(--radius-md);
  margin-top: 16px;
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
  
  .experience-info {
    flex-direction: column;
    gap: 8px;
  }
  
  .inheritor-card {
    flex-direction: column;
  }
  
  .inheritor-card img {
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
}
</style>