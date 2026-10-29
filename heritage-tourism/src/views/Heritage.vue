<template>
  <div class="heritage" :style="{ '--bg-image': `url(${backgroundImage})` }">
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1>吉林遗珍</h1>
        <p>探索吉林非物质文化遗产</p>
      </div>
    </section>



    <!-- 传承人画廊 -->
    <section class="heritage-artists">
      <div class="container">
        <h2>传承人画廊</h2>
        <div class="artists-grid">
          <div class="artist-card" v-for="artist in artists" :key="artist.id">
            <img :src="artist.image" :alt="artist.name" />
            <div class="artist-info">
              <h3>{{ artist.name }}</h3>
              <p class="artist-skill">{{ artist.skill }}</p>
              <p class="artist-desc">{{ artist.description }}</p>
              <button class="btn btn-secondary" @click="viewArtistDetail(artist.id)">查看详情</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- VR/AR体验入口 -->
    <section class="vr-ar-experience">
      <div class="container">
        <h2>VR/AR体验</h2>
        <div class="vr-ar-grid">
          <div class="vr-ar-card">
            <div class="vr-ar-icon">
              <span>🥽</span>
            </div>
            <h3>云游工坊</h3>
            <p>360°全景体验非遗手工作坊</p>
            <button class="btn btn-primary" @click="goToCloudWorkshop">立即体验</button>
          </div>
          <div class="vr-ar-card">
            <div class="vr-ar-icon">
              <span>📱</span>
            </div>
            <h3>AR互动</h3>
            <p>扫描二维码，AR体验非遗文化</p>
            <button class="btn btn-primary" @click="goToARInteraction">立即体验</button>
          </div>
          <div class="vr-ar-card">
            <div class="vr-ar-icon">
              <span>🎥</span>
            </div>
            <h3>360°冬捕现场</h3>
            <p>沉浸式体验查干湖冬捕</p>
            <button class="btn btn-primary" @click="goToWinterFishing360">立即体验</button>
          </div>
        </div>
      </div>
    </section>



    <!-- 短视频/直播流 -->
    <section class="heritage-videos">
      <div class="container">
        <h2>非遗短视频</h2>
        <div class="videos-grid">
          <div class="video-card" v-for="video in videos" :key="video.id" @click="playVideo(video)" style="cursor: pointer;">
            <div class="video-thumbnail">
              <img :src="video.thumbnail" :alt="video.title" />
              <div class="video-duration">{{ video.duration }}</div>
              <div class="video-play-button">
                <span class="play-icon">▶</span>
              </div>
            </div>
            <div class="video-info">
              <h3>{{ video.title }}</h3>
              <p class="video-artist">{{ video.artist }}</p>
              <div class="video-stats">
                <span>{{ video.views }}次观看</span>
                <span>{{ video.likes }}赞</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 视频播放器 -->
    <div v-if="showVideoPlayer" class="video-player-overlay" @click="closeVideoPlayer">
      <div class="video-player-container" @click.stop>
        <button class="close-button" @click="closeVideoPlayer">&times;</button>
        <video ref="videoPlayer" controls autoplay style="width: 100%; height: 100%;">
          <source :src="currentVideoUrl" type="video/mp4">
          您的浏览器不支持视频播放
        </video>
      </div>
    </div>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import video1 from '@/assets/1.mp4'
import video2 from '@/assets/2.mp4'
import video3 from '@/assets/3.mp4'
import video4 from '@/assets/4.mp4'
import nongleImage from '@/assets/农乐舞.jpg'
import dongbuImage from '@/assets/冬捕.jpg'
import papercuttingImage from '@/assets/剪纸.jpg'
import backgroundImage from '@/assets/beijing.png'

const router = useRouter()
const showBackToTop = ref(false)

// 视频播放器
const showVideoPlayer = ref(false)
const currentVideoUrl = ref('')
const videoPlayer = ref(null)

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

const viewArtistDetail = (artistId) => {
  router.push(`/heritage-artist-detail/${artistId}`)
}

// 播放视频
const playVideo = (video) => {
  // 在页面内显示视频播放器
  currentVideoUrl.value = video.videoUrl || ''
  showVideoPlayer.value = true
  // 确保视频播放器加载后自动播放
  setTimeout(() => {
    if (videoPlayer.value) {
      videoPlayer.value.play().catch(error => {
        console.log('视频播放失败:', error)
      })
    }
  }, 100)
}

// 关闭视频播放器
const closeVideoPlayer = () => {
  showVideoPlayer.value = false
  if (videoPlayer.value) {
    videoPlayer.value.pause()
    videoPlayer.value.currentTime = 0
  }
  currentVideoUrl.value = ''
}

// 导航到云游工坊
const goToCloudWorkshop = () => {
  router.push('/cloud-workshop')
}

// 导航到AR互动
const goToARInteraction = () => {
  router.push('/ar-interaction')
}

// 导航到360°冬捕现场
const goToWinterFishing360 = () => {
  router.push('/winter-fishing-360')
}

const artists = [
  {
    id: 1,
    name: '王阿姨',
    skill: '长白山满族剪纸',
    description: '从事剪纸艺术30余年，作品多次获奖',
    image: '/image/Heritage/9e8485af5e3ffa2b5423a01f973be93c.jpeg'
  },
  {
    id: 2,
    name: '金师傅',
    skill: '朝鲜族打糕制作',
    description: '朝鲜族传统打糕技艺传承人',
    image: '/image/Heritage/d12541d119557602dc0ae3d38ac85c83.jpeg'
  },
  {
    id: 3,
    name: '张师傅',
    skill: '查干湖冬捕',
    description: '冬捕技艺传承人，有着丰富的冬捕经验',
    image: '/image/Heritage/bf52353b03672ad83d478e101cbb9431.jpeg'
  },
  {
    id: 4,
    name: '李师傅',
    skill: '松花湖传统渔业',
    description: '传统渔业技艺传承人，熟悉松花湖水域',
    image: '/image/Heritage/84a2da87c260b8e53d050442739112a6.jpeg'
  }
]

const videos = [
  {
    id: 1,
    title: '吉林非遗文化全景',
    artist: '吉林省文化厅',
    thumbnail: papercuttingImage,
    duration: '10:15',
    views: '25.3万',
    likes: '6.7万',
    videoUrl: video1
  },
  {
    id: 2,
    title: '满族传统服饰制作',
    artist: '满族文化协会',
    thumbnail: papercuttingImage,
    duration: '07:45',
    views: '18.9万',
    likes: '4.2万',
    videoUrl: video2
  },
  {
    id: 3,
    title: '朝鲜族传统舞蹈表演',
    artist: '延边歌舞团',
    thumbnail: nongleImage,
    duration: '09:30',
    views: '22.6万',
    likes: '5.8万',
    videoUrl: video3
  },
  {
    id: 4,
    title: '吉林传统美食制作',
    artist: '吉林烹饪协会',
    thumbnail: dongbuImage,
    duration: '08:20',
    views: '16.7万',
    likes: '4.5万',
    videoUrl: video4
  }
]

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
/* Page Header */
.heritage {
  position: relative;
  min-height: 100vh;
}

.heritage::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: var(--bg-image);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.3;
  z-index: -1;
  animation: slideInFromLeft 1.5s ease-out;
}

@keyframes slideInFromLeft {
  0% {
    transform: translateX(-100%);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 0.3;
  }
}

.page-header {
  background-color: var(--primary-color);
  color: var(--white);
  padding: 64px 0;
  text-align: center;
}

.page-header h1 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
  color: var(--white);
}

.page-header p {
  font-size: 18px;
  margin-bottom: 0;
}



/* Heritage Artists */
.heritage-artists {
  padding: 64px 0;
}

.heritage-artists h2 {
  text-align: center;
  margin-bottom: 32px;
}

.artists-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.artist-card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.artist-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.artist-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.artist-info {
  padding: 20px;
}

.artist-info h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 4px;
}

.artist-skill {
  font-size: 14px;
  color: var(--primary-color);
  margin-bottom: 8px;
  font-weight: 500;
}

.artist-desc {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 16px;
  line-height: 1.5;
}

/* VR/AR Experience */
.vr-ar-experience {
  padding: 64px 0;
}

.vr-ar-experience h2 {
  text-align: center;
  margin-bottom: 32px;
}

.vr-ar-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.vr-ar-card {
  background-color: var(--bg-color);
  border-radius: var(--radius-lg);
  padding: 32px;
  text-align: center;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.vr-ar-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.vr-ar-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.vr-ar-card h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 8px;
}

.vr-ar-card p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 24px;
}



/* Heritage Videos */
.heritage-videos {
  padding: 64px 0;
}

.heritage-videos h2 {
  text-align: center;
  margin-bottom: 32px;
}

.videos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.video-card {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.video-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.video-thumbnail {
  position: relative;
}

.video-thumbnail img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: var(--transition);
}

.video-card:hover .video-thumbnail img {
  filter: brightness(0.7);
}

.video-duration {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background-color: rgba(0, 0, 0, 0.7);
  color: var(--white);
  padding: 2px 6px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  z-index: 1;
}

.video-play-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  transition: var(--transition);
  z-index: 1;
  opacity: 0;
  visibility: hidden;
}

.video-card:hover .video-play-button {
  opacity: 1;
  visibility: visible;
}

.video-play-button:hover {
  background-color: rgba(0, 0, 0, 0.8);
  transform: translate(-50%, -50%) scale(1.1);
}

.play-icon {
  color: var(--white);
  font-size: 24px;
  margin-left: 4px;
}

.video-info {
  padding: 16px;
}

.video-info h3 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 4px;
}

.video-artist {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 8px;
}

.video-stats {
  display: flex;
  gap: 16px;
  font-size: 12px;
  color: var(--text-light);
}

/* Responsive */
@media (max-width: 768px) {
  .page-header {
    padding: 48px 0;
  }
  
  .page-header h1 {
    font-size: 28px;
  }
  
  .heritage-map,
  .heritage-artists,
  .vr-ar-experience,
  .heritage-videos {
    padding: 48px 0;
  }
  

  
  .back-to-top {
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
}

/* Video Player */
.video-player-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.video-player-container {
  position: relative;
  width: 90%;
  max-width: 800px;
  height: 80%;
  max-height: 600px;
}

.close-button {
  position: absolute;
  top: -40px;
  right: 0;
  background-color: var(--primary-color);
  color: var(--white);
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  font-size: 20px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
}

.close-button:hover {
  background-color: var(--primary-dark);
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
</style>