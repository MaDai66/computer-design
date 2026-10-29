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
          <span class="current">农家院住宿体验</span>
        </div>
      </div>
    </div>

    <div class="container">
      <!-- 游记主信息 -->
      <section class="note-main">
        <div class="note-header">
          <h1>农家院住宿体验</h1>
          <div class="note-meta">
            <router-link to="/user/城市逃离者" class="author">
              <img src="/image/HomestayExperienceNoteDetail/author_avatar.jpeg" alt="城市逃离者" />
              <span>@城市逃离者</span>
            </router-link>
            <span class="publish-date">2026-03-28</span>
            <span class="views">阅读 12,300</span>
          </div>
          <div class="note-tags">
            <span class="tag tag-blue">农家院</span>
            <span class="tag tag-green">乡村体验</span>
            <span class="tag tag-orange">住宿</span>
          </div>
        </div>
        <div class="note-content">
          <div class="note-cover">
            <img src="/image/HomestayExperienceNoteDetail/cover.jpeg" alt="农家院住宿" />
          </div>
          <div class="note-text">
            <p>远离城市的喧嚣，来到宁静的乡村，体验农家院的生活，真的是一种非常惬意的享受！</p>
            
            <h3>农家院环境</h3>
            <p>我们入住的农家院位于长白山脚下，周围是一片绿色的田野和森林，环境非常优美。农家院的建筑是传统的东北民居风格，红墙绿瓦，非常有特色。院子里种满了各种蔬菜和果树，空气中弥漫着清新的泥土气息。</p>
            <div class="note-images">
              <img src="/image/HomestayExperienceNoteDetail/exterior.jpeg" alt="农家院外观" />
              <img src="/image/HomestayExperienceNoteDetail/courtyard.jpeg" alt="农家院院子" />
              <img src="/image/HomestayExperienceNoteDetail/landscape.jpeg" alt="农家院周边环境" />
            </div>
            
            <h3>房间设施</h3>
            <p>农家院的房间干净整洁，虽然没有城市酒店的豪华，但却充满了家的温馨。房间里有火炕，这是东北的特色，冬天睡在上面非常暖和。窗户很大，可以看到外面的田野和山脉，视野非常好。</p>
            <div class="note-images">
              <img src="/image/HomestayExperienceNoteDetail/room_kang.jpeg" alt="火炕房间" />
              <img src="/image/HomestayExperienceNoteDetail/room_interior.jpeg" alt="房间内部" />
              <img src="/image/HomestayExperienceNoteDetail/window_view.jpeg" alt="房间窗外景色" />
            </div>
            
            <h3>农家美食</h3>
            <p>农家院的饭菜非常美味，都是用当地的新鲜食材制作的。早餐有小米粥、咸鸭蛋、咸菜和馒头，非常地道。午餐和晚餐有各种东北特色菜，如炖鸡、红烧肉、酸菜白肉等，味道非常好。我们还自己采摘了院子里的蔬菜，让老板帮忙做，新鲜又美味。</p>
            <div class="note-images">
              <img src="/image/HomestayExperienceNoteDetail/breakfast.jpeg" alt="农家早餐" />
              <img src="/image/HomestayExperienceNoteDetail/lunch.jpeg" alt="农家饭菜" />
              <img src="/image/HomestayExperienceNoteDetail/vegetables.jpeg" alt="新鲜蔬菜" />
            </div>
            
            <h3>乡村活动</h3>
            <p>在农家院的日子里，我们参加了各种乡村活动，如采摘蔬菜、喂鸡、钓鱼等。这些活动让我们感受到了乡村生活的乐趣，也让我们更加了解了农民的生活。晚上，我们在院子里生起了篝火，和老板一家一起聊天、唱歌，非常开心。</p>
            <div class="note-images">
              <img src="/image/HomestayExperienceNoteDetail/picking.jpeg" alt="采摘蔬菜" />
              <img src="/image/HomestayExperienceNoteDetail/fishing.jpeg" alt="钓鱼" />
              <img src="/image/HomestayExperienceNoteDetail/bonfire.jpeg" alt="篝火晚会" />
            </div>
            
            <h3>当地文化</h3>
            <p>农家院的老板非常热情，给我们介绍了当地的文化和习俗。我们了解了东北的传统节日、民间故事和生活方式，这些都让我们对东北文化有了更深入的了解。老板还教我们说了一些东北方言，非常有趣。</p>
            
            <h3>总结</h3>
            <p>这次农家院住宿体验让我们远离了城市的喧嚣，感受到了乡村的宁静和美好。在这里，我们不仅休息了身心，还体验了不同的生活方式，了解了当地的文化。这是一次非常难忘的经历，我们一定会再来的！</p>
          </div>
        </div>
        <div class="note-actions">
          <button class="action-btn like">
            <span class="action-icon">❤️</span>
            <span class="action-text">1,560</span>
          </button>
          <button class="action-btn comment">
            <span class="action-icon">💬</span>
            <span class="action-text">423</span>
          </button>
          <button class="action-btn favorite">
            <span class="action-icon">⭐</span>
            <span class="action-text">987</span>
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
                <img src="/image/HomestayExperienceNoteDetail/user_avatar_1.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@旅行爱好者</span>
                  <span class="comment-date">2026-03-29</span>
                </div>
              </div>
              <button class="comment-like">❤️ 67</button>
            </div>
            <div class="comment-content">
              <p>农家院看起来很舒适！请问具体是在哪里？价格怎么样？我们一家也想找个周末去体验一下。</p>
            </div>
            <div class="comment-reply">
              <button class="reply-btn">回复</button>
            </div>
          </div>
          <div class="comment-item">
            <div class="comment-header">
              <div class="user-info">
                <img src="/image/HomestayExperienceNoteDetail/user_avatar_2.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@城市居民</span>
                  <span class="comment-date">2026-03-30</span>
                </div>
              </div>
              <button class="comment-like">❤️ 45</button>
            </div>
            <div class="comment-content">
              <p>我也去过类似的农家院，确实很惬意。远离城市的喧嚣，亲近自然，吃着农家菜，感觉整个人都放松了。</p>
            </div>
            <div class="comment-reply">
              <button class="reply-btn">回复</button>
            </div>
          </div>
          <div class="comment-item">
            <div class="comment-header">
              <div class="user-info">
                <img src="/image/HomestayExperienceNoteDetail/user_avatar_3.jpeg" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@美食达人</span>
                  <span class="comment-date">2026-04-01</span>
                </div>
              </div>
              <button class="comment-like">❤️ 32</button>
            </div>
            <div class="comment-content">
              <p>农家菜看起来好美味！特别是那个炖鸡，看起来就很正宗。下次去东北一定要体验一下农家院的美食。</p>
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