<template>
  <div class="heritage-artist-detail">
    <!-- 页面标题 -->
    <section class="page-header">
      <div class="container">
        <h1>{{ artist.name }}</h1>
        <p>{{ artist.skill }}传承人</p>
      </div>
    </section>

    <!-- 传承人详情 -->
    <section class="artist-detail">
      <div class="container">
        <div class="artist-profile">
          <div class="artist-image">
            <img :src="artist.image" :alt="artist.name" />
          </div>
          <div class="artist-info">
            <h2>{{ artist.name }}</h2>
            <p class="artist-skill">{{ artist.skill }}</p>
            <p class="artist-desc">{{ artist.description }}</p>
            <div class="artist-stats">
              <div class="stat-item">
                <span class="stat-value">{{ artist.experienceYears }}</span>
                <span class="stat-label">从业年限</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ artist.awardsCount }}</span>
                <span class="stat-label">获奖次数</span>
              </div>
              <div class="stat-item">
                <span class="stat-value">{{ artist.studentsCount }}</span>
                <span class="stat-label">传承学生</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 传承人故事 -->
        <div class="artist-story">
          <h3>传承人故事</h3>
          <p>{{ artist.story }}</p>
        </div>

        <!-- 代表作品 -->
        <div class="artist-works">
          <h3>代表作品</h3>
          <div class="works-grid">
            <div class="work-item" v-for="(work, index) in artist.works" :key="index">
              <img :src="work.image" :alt="work.name" />
              <h4>{{ work.name }}</h4>
              <p>{{ work.description }}</p>
            </div>
          </div>
        </div>

        <!-- 传承活动 -->
        <div class="artist-activities">
          <h3>传承活动</h3>
          <div class="activities-list">
            <div class="activity-item" v-for="(activity, index) in artist.activities" :key="index">
              <div class="activity-date">{{ activity.date }}</div>
              <div class="activity-content">
                <h4>{{ activity.title }}</h4>
                <p>{{ activity.description }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 传承人视频 -->
        <div class="artist-videos">
          <h3>传承人视频</h3>
          <div class="video-container" v-if="artist.videos && artist.videos.length > 0">
            <div class="video-card" @click="playVideo(artist.videos[0])">
              <div class="video-thumbnail">
                <img :src="artist.videos[0].thumbnail" :alt="artist.videos[0].title" />
                <div class="video-play-button">
                  <span class="play-icon">▶</span>
                </div>
                <div class="video-duration">{{ artist.videos[0].duration }}</div>
              </div>
              <div class="video-info">
                <h4>{{ artist.videos[0].title }}</h4>
                <div class="video-stats">
                  <span>{{ artist.videos[0].views }}次观看</span>
                  <span>{{ artist.videos[0].likes }}赞</span>
                </div>
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
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import video5 from '@/assets/5.mp4'
import video6 from '@/assets/6.mp4'
import video7 from '@/assets/7.mp4'
import video8 from '@/assets/8.mp4'
import dagaoren1 from '@/assets/dagaoren/1.png'
import dagaoren2 from '@/assets/dagaoren/2.png'
import dagaoren3 from '@/assets/dagaoren/3.png'
import dongbu1 from '@/assets/dongbu/1.png'
import dongbu2 from '@/assets/dongbu/2.png'
import dongbu3 from '@/assets/dongbu/3.png'
import yuye1 from '@/assets/yuye/1.png'
import yuye2 from '@/assets/yuye/2.png'
import yuye3 from '@/assets/yuye/3.png'

const route = useRoute()
const router = useRouter()
const showBackToTop = ref(false)

// 视频播放器
const showVideoPlayer = ref(false)
const currentVideoUrl = ref('')
const videoPlayer = ref(null)

// 传承人数据
const artistsData = [
  {
    id: 1,
    name: '王阿姨',
    skill: '长白山满族剪纸',
    description: '从事剪纸艺术30余年，作品多次获奖',
    experienceYears: 35,
    awardsCount: 12,
    studentsCount: 56,
    story: '王阿姨出生在长白山脚下的满族家庭，从小跟随祖母学习剪纸技艺。她的作品融合了满族传统图案与现代元素，多次在国内外展览中获奖。近年来，她致力于传承这门技艺，开设了多期剪纸培训班，培养了众多年轻传承人。她的作品被多个博物馆收藏，成为吉林非物质文化遗产的重要代表。',
    image: '/image/HeritageArtistDetail/9e8485af5e3ffa2b5423a01f973be93c (1).jpeg',
    works: [
      {
        name: '满族吉祥图案',
        description: '融合满族传统吉祥纹样，寓意幸福安康',
        image: '/image/HeritageArtistDetail/4767d3b83a64b584aed445c0d57958c6.jpeg'
      },
      {
        name: '长白山风光',
        description: '展现长白山壮丽景色的剪纸作品',
        image: '/image/HeritageArtistDetail/3bae17c5d3586731df15554a7ef668f8.jpeg'
      },
      {
        name: '满族民俗',
        description: '反映满族传统民俗活动的剪纸作品',
        image: '/image/HeritageArtistDetail/e3331d7de6473a804f441c229391a43b.jpeg'
      }
    ],
    activities: [
      {
        date: '2026-04-10',
        title: '满族剪纸艺术工作坊',
        description: '在长春市文化中心举办剪纸技艺培训班'
      },
      {
        date: '2026-05-15',
        title: '非遗进校园活动',
        description: '走进长春市第一中学，向学生展示剪纸技艺'
      },
      {
        date: '2026-06-20',
        title: '满族剪纸展览',
        description: '在吉林省博物馆举办个人剪纸作品展览'
      }
    ],
    videos: [
      {
        title: '满族剪纸艺术教程',
        thumbnail: '/image/HeritageArtistDetail/10dbea63503c386f9199d5f416958a4c.jpeg',
        duration: '05:23',
        views: '12.5万',
        likes: '3.2万',
        videoUrl: video5
      }
    ]
  },
  {
    id: 2,
    name: '金师傅',
    skill: '朝鲜族打糕制作',
    description: '朝鲜族传统打糕技艺传承人',
    experienceYears: 40,
    awardsCount: 8,
    studentsCount: 32,
    story: '金师傅是朝鲜族打糕制作技艺的代表性传承人，从小跟随父亲学习打糕制作。他坚持使用传统工艺，选用优质糯米，经过浸泡、蒸煮、捶打等多道工序，制作出的打糕口感细腻、香甜可口。金师傅不仅在国内传承技艺，还曾到韩国进行文化交流，为促进中韩文化交流做出了贡献。',
    image: '/image/HeritageArtistDetail/d12541d119557602dc0ae3d38ac85c83.jpeg',
    works: [
      {
        name: '传统打糕',
        description: '采用传统工艺制作的经典打糕',
        image: '/image/HeritageArtistDetail/95e32a266f181b468a2b9c2a657e21a0.jpeg'
      },
      {
        name: '红豆打糕',
        description: '加入红豆馅的特色打糕',
        image: '/image/HeritageArtistDetail/b71cbbbe7f99f67073bddffd85f7a13e.jpeg'
      },
      {
        name: '芝麻打糕',
        description: '撒有芝麻的香甜打糕',
        image: '/image/HeritageArtistDetail/d2803ab5907dff497031d0c5c26b8dca.jpeg'
      }
    ],
    activities: [
      {
        date: '2026-04-20',
        title: '朝鲜族打糕制作体验',
        description: '在延边朝鲜族自治州举办打糕制作体验活动'
      },
      {
        date: '2026-05-25',
        title: '非遗进社区',
        description: '走进长春市朝鲜族社区，教授打糕制作技艺'
      },
      {
        date: '2026-06-10',
        title: '打糕文化节',
        description: '在延吉市举办打糕文化节，展示各种打糕制作技艺'
      }
    ],
    videos: [
      {
        title: '朝鲜族打糕制作过程',
        thumbnail: '/image/HeritageArtistDetail/4a7ea9a34f51e8e369faafba911ec467.jpeg',
        duration: '08:45',
        views: '8.9万',
        likes: '2.5万',
        videoUrl: video6
      }
    ]
  },
  {
    id: 3,
    name: '张师傅',
    skill: '查干湖冬捕',
    description: '冬捕技艺传承人，有着丰富的冬捕经验',
    experienceYears: 45,
    awardsCount: 15,
    studentsCount: 28,
    story: '张师傅是查干湖冬捕技艺的代表性传承人，从小跟随父亲学习冬捕技艺。他熟悉查干湖的水域情况，掌握了传统的冬捕方法，包括选网、凿冰、下网、拉网等工序。张师傅不仅传承了冬捕技艺，还致力于保护查干湖的生态环境，确保冬捕活动的可持续发展。他的冬捕团队曾多次创造冬捕丰收纪录，成为查干湖冬捕文化的重要象征。',
    image: '/image/HeritageArtistDetail/bf52353b03672ad83d478e101cbb9431.jpeg',
    works: [
      {
        name: '冬捕仪式',
        description: '传统冬捕仪式的准备和执行',
        image: dongbu1
      },
      {
        name: '冬捕工具',
        description: '传统冬捕工具的制作和使用',
        image: dongbu2
      },
      {
        name: '冬捕丰收',
        description: '冬捕丰收的壮观场景',
        image: dongbu3
      }
    ],
    activities: [
      {
        date: '2026-01-15',
        title: '查干湖冬捕开网仪式',
        description: '主持查干湖冬捕开网仪式，展示传统冬捕技艺'
      },
      {
        date: '2026-04-15',
        title: '冬捕技艺培训班',
        description: '在查干湖举办冬捕技艺培训班，传授传统技艺'
      },
      {
        date: '2026-07-20',
        title: '冬捕文化展览',
        description: '在吉林省博物馆举办冬捕文化展览，展示冬捕历史和技艺'
      }
    ],
    videos: [
      {
        title: '查干湖冬捕纪实',
        thumbnail: '/image/HeritageArtistDetail/2b1baa74497114699eae7fa6184bffa0.jpeg',
        duration: '12:30',
        views: '15.6万',
        likes: '4.8万',
        videoUrl: video7
      }
    ]
  },
  {
    id: 4,
    name: '李师傅',
    skill: '松花湖传统渔业',
    description: '传统渔业技艺传承人，熟悉松花湖水域',
    experienceYears: 38,
    awardsCount: 6,
    studentsCount: 18,
    story: '李师傅是松花湖传统渔业技艺的代表性传承人，从小在松花湖边长大，熟悉湖水的变化和鱼类的习性。他掌握了传统的捕鱼方法，包括撒网、钓鱼、放笼等多种技艺。李师傅不仅传承了传统渔业技艺，还致力于保护松花湖的生态环境，推广可持续的渔业 practices。他经常向年轻一代传授渔业知识，确保这门技艺得以传承。',
    image: '/image/HeritageArtistDetail/84a2da87c260b8e53d050442739112a6.jpeg',
    works: [
      {
        name: '传统渔网',
        description: '手工编织的传统渔网',
        image: yuye1
      },
      {
        name: '松花湖渔获',
        description: '松花湖的新鲜渔获',
        image: yuye2
      },
      {
        name: '渔业工具',
        description: '传统渔业工具的展示',
        image: yuye3
      }
    ],
    activities: [
      {
        date: '2026-05-10',
        title: '松花湖传统渔业体验',
        description: '在松花湖举办传统渔业体验活动，教授传统捕鱼技艺'
      },
      {
        date: '2026-06-15',
        title: '渔业文化节',
        description: '在吉林市举办渔业文化节，展示传统渔业文化'
      },
      {
        date: '2026-08-20',
        title: '渔业技艺培训班',
        description: '在松花湖举办渔业技艺培训班，传授传统技艺'
      }
    ],
    videos: [
      {
        title: '松花湖传统渔业文化',
        thumbnail: '/image/HeritageArtistDetail/3ed4ad90193d4db53256926c4c262529.jpeg',
        duration: '06:15',
        views: '6.7万',
        likes: '1.9万',
        videoUrl: video8
      }
    ]
  }
]

// 根据路由参数获取传承人信息
const artist = computed(() => {
  const id = parseInt(route.params.id)
  return artistsData.find(a => a.id === id) || artistsData[0]
})

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
/* Page Header */
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

/* Artist Detail */
.artist-detail {
  padding: 64px 0;
  background-color: var(--bg-light);
}

.artist-profile {
  display: flex;
  gap: 32px;
  margin-bottom: 48px;
  background-color: var(--white);
  padding: 32px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
}

.artist-image {
  flex: 0 0 300px;
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow);
}

.artist-image img {
  width: 100%;
  height: 400px;
  object-fit: cover;
}

.artist-info {
  flex: 1;
}

.artist-info h2 {
  font-size: 28px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.artist-skill {
  font-size: 18px;
  color: var(--primary-color);
  margin-bottom: 16px;
  font-weight: 500;
}

.artist-desc {
  font-size: 16px;
  color: var(--text-medium);
  line-height: 1.6;
  margin-bottom: 24px;
}

.artist-stats {
  display: flex;
  gap: 32px;
  margin-top: 24px;
}

.stat-item {
  text-align: center;
}

.stat-value {
  display: block;
  font-size: 24px;
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 4px;
}

.stat-label {
  display: block;
  font-size: 14px;
  color: var(--text-medium);
}

/* Artist Story */
.artist-story {
  background-color: var(--white);
  padding: 32px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  margin-bottom: 32px;
}

.artist-story h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 16px;
  color: var(--text-dark);
  padding-bottom: 12px;
  border-bottom: 2px solid var(--primary-color);
}

.artist-story p {
  font-size: 16px;
  line-height: 1.6;
  color: var(--text-medium);
  margin-bottom: 0;
}

/* Artist Works */
.artist-works {
  background-color: var(--white);
  padding: 32px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  margin-bottom: 32px;
}

.artist-works h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
  color: var(--text-dark);
  padding-bottom: 12px;
  border-bottom: 2px solid var(--primary-color);
}

.works-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.work-item {
  text-align: center;
  padding: 20px;
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
  transition: var(--transition);
}

.work-item:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.work-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: var(--radius-sm);
  margin-bottom: 16px;
}

.work-item h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.work-item p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 0;
}

/* Artist Activities */
.artist-activities {
  background-color: var(--white);
  padding: 32px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  margin-bottom: 32px;
}

.artist-activities h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
  color: var(--text-dark);
  padding-bottom: 12px;
  border-bottom: 2px solid var(--primary-color);
}

.activities-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.activity-item {
  display: flex;
  gap: 24px;
  padding: 20px;
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
  transition: var(--transition);
}

.activity-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}

.activity-date {
  flex: 0 0 120px;
  font-weight: 600;
  color: var(--primary-color);
  padding-top: 4px;
}

.activity-content h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.activity-content p {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 0;
}

/* Artist Videos */
.artist-videos {
  background-color: var(--white);
  padding: 32px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  margin-bottom: 32px;
}

.artist-videos h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
  color: var(--text-dark);
  padding-bottom: 12px;
  border-bottom: 2px solid var(--primary-color);
}

.video-container {
  display: flex;
  justify-content: center;
}

.video-card {
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: var(--transition);
  cursor: pointer;
  width: 100%;
  max-width: 500px;
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
  height: 300px;
  object-fit: cover;
}

.video-play-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  transition: var(--transition);
  z-index: 1;
}

.video-play-button:hover {
  background-color: rgba(0, 0, 0, 0.8);
  transform: translate(-50%, -50%) scale(1.1);
}

.play-icon {
  color: var(--white);
  font-size: 32px;
  margin-left: 4px;
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

.video-info {
  padding: 16px;
}

.video-info h4 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-dark);
}

.video-stats {
  display: flex;
  gap: 16px;
  font-size: 14px;
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
  
  .artist-detail {
    padding: 48px 0;
  }
  
  .artist-profile {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .artist-image {
    flex: none;
    width: 100%;
    max-width: 300px;
  }
  
  .artist-stats {
    justify-content: center;
  }
  
  .activity-item {
    flex-direction: column;
    gap: 12px;
    text-align: center;
  }
  
  .activity-date {
    flex: none;
    width: 100%;
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