<template>
  <div class="travel-note-detail">
    <!-- 顶部导航 -->
    <div class="top-nav">
      <div class="container">
        <div class="breadcrumb">
          <router-link to="/">首页</router-link>
          <span>/</span>
          <router-link to="/community">社区</router-link>
          <span>/</span>
          <span class="current">长白山之旅</span>
        </div>
      </div>
    </div>

    <div class="container">
      <!-- 游记主信息 -->
      <section class="note-main">
        <div class="note-header">
          <h1>长白山之旅</h1>
          <div class="note-meta">
            <router-link to="/user/小明" class="author">
              <img src="/image/TravelNoteDetail/author_avatar.jpeg" alt="旅行含小明" />
              <span>@旅行含小明</span>
            </router-link>
            <span class="publish-date">2026-04-10</span>
            <span class="views">阅读 12,800</span>
          </div>
          <div class="note-tags">
            <span class="tag tag-blue">长白山</span>
            <span class="tag tag-green">非遗体验</span>
            <span class="tag tag-orange">旅行日记</span>
          </div>
        </div>
        <div class="note-content">
          <div class="note-cover">
            <img :src="changbaishan" alt="长白山风景" />
          </div>
          <div class="note-text">
            <p>终于来到了心心念念的长白山！这次旅行真的是一场视觉盛宴，从山脚到山顶，每一处风景都让人流连忘返。</p>
            
            <h3>Day 1: 长白山北坡</h3>
            <p>早上从延吉出发，大约3小时车程到达长白山北坡景区。一下车就被眼前的美景震撼了，远处的长白山主峰在云雾中若隐若现，仿佛仙境一般。</p>
            <div class="note-images">
              <img src="/image/TravelNoteDetail/day1_entrance.jpeg" alt="长白山北坡入口" />
              <img src="/image/TravelNoteDetail/day1_waterfall.jpeg" alt="长白山瀑布" />
              <img src="/image/TravelNoteDetail/day1_hotsprings.jpeg" alt="长白山温泉" />
            </div>
            <p>我们先乘坐景区大巴到天池换乘中心，然后再坐越野车上山。虽然山路崎岖，但沿途的风景非常壮观。到达天池后，我们被眼前的景象惊呆了 - 湛蓝的湖水像一块宝石镶嵌在群山之间，周围的雪山倒映在水中，美不胜收。</p>
            
            <h3>Day 2: 满族民俗村</h3>
            <p>第二天我们来到了附近的满族民俗村，体验了满族的传统文化。在这里，我们学习了满族剪纸技艺，穿上了传统的满族服饰，还品尝了正宗的满族美食。</p>
            <div class="note-images">
              <img src="/image/TravelNoteDetail/day2_village.jpeg" alt="满族民俗村" />
              <img src="/image/TravelNoteDetail/day2_papercutting.jpeg" alt="满族剪纸体验" />
              <img src="/image/TravelNoteDetail/day2_food.jpeg" alt="满族美食" />
            </div>
            <p>最让我印象深刻的是满族的篝火晚会，当地的村民们穿着传统服饰，载歌载舞，我们也加入其中，一起跳舞、唱歌，度过了一个难忘的夜晚。</p>
            
            <h3>Day 3: 长白山天池西坡</h3>
            <p>第三天我们来到了长白山西坡，这里的风景与北坡有所不同，更加原始和壮观。我们沿着1236级台阶登上山顶，虽然很累，但当看到天池的那一刻，所有的疲惫都值得了。</p>
            <div class="note-images">
              <img src="/image/TravelNoteDetail/day3_steps.jpeg" alt="西坡台阶" />
              <img src="/image/TravelNoteDetail/day3_tianchi.jpeg" alt="西坡天池" />
              <img src="/image/TravelNoteDetail/day3_meadow.jpeg" alt="高山草甸" />
            </div>
            <p>西坡的高山草甸非常漂亮，大片的野花盛开，仿佛置身于童话世界。我们在这里拍了很多照片，留下了美好的回忆。</p>
            
            <h3>总结</h3>
            <p>这次长白山之旅真的是一次难忘的经历，不仅欣赏了美丽的自然风光，还体验了丰富的满族文化。如果你也喜欢大自然和传统文化，一定要来长白山看看，相信你会和我一样爱上这个地方。</p>
            <p>最后，感谢所有帮助过我们的当地人，他们的热情好客让我们的旅程更加愉快。期待下次再来！</p>
          </div>
        </div>
        <div class="note-actions">
          <button class="action-btn like">
            <span class="action-icon">❤️</span>
            <span class="action-text">1,280</span>
          </button>
          <button class="action-btn comment">
            <span class="action-icon">💬</span>
            <span class="action-text">328</span>
          </button>
          <button class="action-btn favorite">
            <span class="action-icon">⭐</span>
            <span class="action-text">896</span>
          </button>
          <button class="action-btn share">
            <span class="action-icon">🔗</span>
            <span class="action-text">分享</span>
          </button>
        </div>
      </section>

      <!-- 评论区 -->
      <section class="comment-section">
        <h2>评论区</h2>
        <div class="comment-form">
          <textarea placeholder="写下你的评论..." rows="4"></textarea>
          <button class="btn btn-primary submit-comment">发表评论</button>
        </div>
        <div class="comments-list">
          <div class="comment-item">
            <div class="comment-header">
              <div class="user-info">
                <img src="/image/TravelNoteDetail/user_avatar_1.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@旅行爱好者</span>
                  <span class="comment-date">2026-04-11</span>
                </div>
              </div>
              <button class="comment-like">❤️ 28</button>
            </div>
            <div class="comment-content">
              <p>太精彩了！你的游记让我对长白山充满了向往，特别是满族民俗村的体验，看起来非常有趣。请问你住的是哪家民宿？环境怎么样？</p>
            </div>
            <div class="comment-reply">
              <button class="reply-btn">回复</button>
            </div>
          </div>
          <div class="comment-item">
            <div class="comment-header">
              <div class="user-info">
                <img src="/image/TravelNoteDetail/user_avatar_2.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@文化探索者</span>
                  <span class="comment-date">2026-04-12</span>
                </div>
              </div>
              <button class="comment-like">❤️ 15</button>
            </div>
            <div class="comment-content">
              <p>天池的照片太震撼了！我去年也去过长白山，但是因为天气原因没有看到天池，一直很遗憾。看到你的照片，我决定今年再去一次，希望能幸运地看到天池。</p>
            </div>
            <div class="comment-reply">
              <button class="reply-btn">回复</button>
            </div>
          </div>
          <div class="comment-item">
            <div class="comment-header">
              <div class="user-info">
                <img src="/image/TravelNoteDetail/user_avatar_3.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@美食达人</span>
                  <span class="comment-date">2026-04-13</span>
                </div>
              </div>
              <button class="comment-like">❤️ 12</button>
            </div>
            <div class="comment-content">
              <p>满族美食看起来好诱人！请问具体是哪些菜品？有没有推荐的餐厅？我计划下个月去长白山，希望能尝尝当地的特色美食。</p>
            </div>
            <div class="comment-reply">
              <button class="reply-btn">回复</button>
            </div>
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
import changbaishan from '@/assets/changbaishan.png'

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
.travel-note-detail {
  background-color: var(--bg-light);
  min-height: 100vh;
}

.top-nav {
  background-color: var(--white);
  border-bottom: 1px solid var(--border-color);
  padding: 16px 0;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
}

.breadcrumb a {
  color: var(--text-medium);
  text-decoration: none;
  transition: var(--transition);
}

.breadcrumb a:hover {
  color: var(--primary-color);
}

.breadcrumb .current {
  color: var(--text-dark);
  font-weight: 500;
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

/* 游记主信息 */
.note-header {
  margin-bottom: 24px;
}

.note-header h1 {
  font-size: 28px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 16px;
}

.note-meta {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 16px;
}

.author {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  transition: var(--transition);
}

.author:hover {
  color: var(--primary-color);
}

.author img {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.author span {
  font-weight: 500;
  color: var(--text-dark);
}

.publish-date, .views {
  font-size: 14px;
  color: var(--text-medium);
}

.note-tags {
  display: flex;
  gap: 8px;
}

.tag {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.tag-blue {
  background-color: var(--accent-blue-light);
  color: var(--accent-blue);
}

.tag-green {
  background-color: var(--accent-green-light);
  color: var(--accent-green);
}

.tag-orange {
  background-color: var(--accent-orange-light);
  color: var(--accent-orange);
}

.note-cover {
  width: 100%;
  height: 400px;
  border-radius: var(--radius-md);
  overflow: hidden;
  margin-bottom: 24px;
}

.note-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.note-text p {
  line-height: 1.6;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.note-images {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin: 24px 0;
}

.note-images img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: var(--radius-md);
  transition: var(--transition);
  cursor: pointer;
}

.note-images img:hover {
  transform: scale(1.05);
  box-shadow: var(--shadow-hover);
}

.note-actions {
  display: flex;
  gap: 24px;
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid var(--border-color);
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  font-size: 16px;
  color: var(--text-medium);
  cursor: pointer;
  transition: var(--transition);
  padding: 8px 16px;
  border-radius: var(--radius-md);
}

.action-btn:hover {
  background-color: var(--primary-light);
  color: var(--primary-color);
}

.action-icon {
  font-size: 20px;
}

/* 评论区 */
.comment-form {
  margin-bottom: 32px;
}

.comment-form textarea {
  width: 100%;
  padding: 16px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  font-size: 16px;
  resize: vertical;
  margin-bottom: 16px;
  outline: none;
  transition: var(--transition);
}

.comment-form textarea:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px var(--primary-light);
}

.submit-comment {
  align-self: flex-end;
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-bottom: 32px;
}

.comment-item {
  padding: 24px;
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
}

.comment-header {
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

.comment-date {
  font-size: 12px;
  color: var(--text-light);
}

.comment-like {
  background: none;
  border: none;
  font-size: 14px;
  color: var(--text-medium);
  cursor: pointer;
  transition: var(--transition);
  padding: 4px 8px;
  border-radius: var(--radius-sm);
}

.comment-like:hover {
  background-color: var(--accent-red-light);
  color: var(--accent-red);
}

.comment-content p {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 12px;
}

.comment-reply {
  display: flex;
  justify-content: flex-end;
}

.reply-btn {
  background: none;
  border: none;
  font-size: 14px;
  color: var(--primary-color);
  cursor: pointer;
  transition: var(--transition);
  padding: 4px 8px;
  border-radius: var(--radius-sm);
}

.reply-btn:hover {
  background-color: var(--primary-light);
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
  
  .note-header h1 {
    font-size: 24px;
  }
  
  .note-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  
  .note-cover {
    height: 250px;
  }
  
  .note-images {
    grid-template-columns: 1fr;
  }
  
  .note-actions {
    flex-wrap: wrap;
    gap: 12px;
  }
  
  .action-btn {
    flex: 1;
    justify-content: center;
  }
  
  section {
    padding: 20px;
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