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
          <span class="current">朝鲜族打糕体验</span>
        </div>
      </div>
    </div>

    <div class="container">
      <!-- 游记主信息 -->
      <section class="note-main">
        <div class="note-header">
          <h1>朝鲜族打糕体验</h1>
          <div class="note-meta">
            <router-link to="/user/美食爱好者" class="author">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Food%20blogger%20avatar%20profile%20picture&image_size=portrait_4_3" alt="美食爱好者" />
              <span>@美食爱好者</span>
            </router-link>
            <span class="publish-date">2026-04-05</span>
            <span class="views">阅读 8,500</span>
          </div>
          <div class="note-tags">
            <span class="tag tag-blue">朝鲜族</span>
            <span class="tag tag-green">非遗体验</span>
            <span class="tag tag-orange">美食</span>
          </div>
        </div>
        <div class="note-content">
          <div class="note-cover">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20rice%20cake%20making%20experience%20traditional%20craft&image_size=landscape_16_9" alt="朝鲜族打糕体验" />
          </div>
          <div class="note-text">
            <p>今天终于体验了朝鲜族传统的打糕制作，真的是一次非常有趣的文化体验！</p>
            
            <h3>打糕制作过程</h3>
            <p>打糕是朝鲜族的传统美食，制作过程非常有特色。我们首先看到了准备好的糯米，已经浸泡了几个小时，然后蒸熟。蒸熟的糯米被放在一个大木槽里，然后用木槌反复捶打。</p>
            <div class="note-images">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Steamed%20glutinous%20rice%20for%20rice%20cake&image_size=portrait_4_3" alt="蒸熟的糯米" />
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20rice%20cake%20making%20with%20wooden%20hammer&image_size=portrait_4_3" alt="捶打糯米" />
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20rice%20cake%20dough%20preparation&image_size=portrait_4_3" alt="打糕面团" />
            </div>
            <p>捶打的过程需要两个人配合，一个人捶打，另一个人在旁边翻动糯米团，确保每一部分都被均匀地捶打。这个过程需要一定的力量和技巧，看起来简单，实际操作起来还是有点难度的。</p>
            
            <h3>自己动手体验</h3>
            <p>在师傅的指导下，我们每个人都有机会亲自尝试捶打糯米。虽然一开始有点手忙脚乱，但在师傅的耐心指导下，我们逐渐掌握了技巧。捶打的过程不仅是制作美食，更是一种文化体验。</p>
            <div class="note-images">
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tourist%20trying%20to%20make%20Korean%20rice%20cake&image_size=portrait_4_3" alt="游客体验打糕" />
              <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20rice%20cake%20making%20class&image_size=portrait_4_3" alt="打糕制作课堂" />
              <img :src="dagao3" alt="成品打糕" />
            </div>
            
            <h3>品尝成果</h3>
            <p>制作完成后，我们品尝了自己亲手制作的打糕。刚做好的打糕非常软糯，口感香甜，配上红豆沙和黄豆粉，味道非常好。师傅还教我们如何正确地食用打糕，以及打糕在朝鲜族文化中的重要地位。</p>
            
            <h3>文化体验</h3>
            <p>除了制作打糕，我们还了解了朝鲜族的饮食文化和传统习俗。师傅向我们介绍了打糕在朝鲜族节日和重要场合中的作用，以及朝鲜族的其他传统美食。</p>
            
            <h3>总结</h3>
            <p>这次朝鲜族打糕体验不仅让我们学到了传统的制作技艺，更让我们深入了解了朝鲜族的文化。这是一次非常有意义的体验，强烈推荐给喜欢美食和文化的朋友们！</p>
          </div>
        </div>
        <div class="note-actions">
          <button class="action-btn like">
            <span class="action-icon">❤️</span>
            <span class="action-text">890</span>
          </button>
          <button class="action-btn comment">
            <span class="action-icon">💬</span>
            <span class="action-text">156</span>
          </button>
          <button class="action-btn favorite">
            <span class="action-icon">⭐</span>
            <span class="action-text">589</span>
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
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@美食达人</span>
                  <span class="comment-date">2026-04-06</span>
                </div>
              </div>
              <button class="comment-like">❤️ 45</button>
            </div>
            <div class="comment-content">
              <p>看起来好有趣！我也想体验一下打糕制作，请问具体是在哪里体验的？需要提前预约吗？</p>
            </div>
            <div class="comment-reply">
              <button class="reply-btn">回复</button>
            </div>
          </div>
          <div class="comment-item">
            <div class="comment-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%202&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@文化探索者</span>
                  <span class="comment-date">2026-04-07</span>
                </div>
              </div>
              <button class="comment-like">❤️ 28</button>
            </div>
            <div class="comment-content">
              <p>打糕看起来好美味！朝鲜族的传统美食文化真的很丰富，有机会一定要去体验一下。</p>
            </div>
            <div class="comment-reply">
              <button class="reply-btn">回复</button>
            </div>
          </div>
          <div class="comment-item">
            <div class="comment-header">
              <div class="user-info">
                <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=User%20avatar%20profile%20picture%203&image_size=portrait_4_3" alt="用户头像" />
                <div class="user-details">
                  <span class="user-name">@旅行爱好者</span>
                  <span class="comment-date">2026-04-08</span>
                </div>
              </div>
              <button class="comment-like">❤️ 19</button>
            </div>
            <div class="comment-content">
              <p>谢谢分享！我上个月也去体验了打糕制作，确实很有趣。师傅还教了我们一些朝鲜族的传统礼仪，收获满满。</p>
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
import dagao3 from '@/assets/dagao/3.png'

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