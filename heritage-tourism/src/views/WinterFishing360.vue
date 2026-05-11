<template>
  <div class="winter-fishing-360">
    <!-- 顶部悬浮导航 -->
    <header class="floating-nav">
      <div class="container">
        <div class="nav-content">
          <div class="logo" @click="goHome">吉林遗珍</div>
          <button class="back-btn" @click="goBack">返回</button>
          <div class="scene-selector">
            <select v-model="selectedScene" @change="changeScene">
              <option value="net-pulling">冰面拉网</option>
              <option value="harvest">渔获丰收</option>
              <option value="ceremony">祭湖醒网仪式</option>
            </select>
          </div>
          <div class="audio-control">
            <button class="audio-btn" @click="toggleAudio">
              {{ isPlaying ? '🔊 播放中' : '🔇 静音' }}
            </button>
          </div>
          <button class="share-btn">分享</button>
        </div>
      </div>
    </header>

    <!-- 主视觉区（360°全景） -->
    <div class="panorama-container">
      <div id="panorama" ref="panoramaRef" class="panorama-view">
        <div class="loading">加载中...</div>
      </div>
      
      <!-- 黑屏过渡效果 -->
      <div v-if="showBlackScreen" class="black-screen" :class="{ 'door-open': doorOpening }">
        <div class="door-left"></div>
        <div class="door-right"></div>
      </div>
      
      <!-- 欢迎文字效果 -->
      <transition name="welcome-fade">
        <div v-if="showWelcomeText" class="welcome-text">
          <h1>欢迎来到查干湖冬捕</h1>
          <p>体验千年渔猎文化的魅力</p>
        </div>
      </transition>
      
      <!-- 热点信息卡片 -->
      <div v-if="showHotspotCard" class="hotspot-card">
        <button class="close-card" @click="closeHotspotCard">&times;</button>
        <h3>{{ hotspotInfo.title }}</h3>
        <p>{{ hotspotInfo.content }}</p>
        <div v-if="hotspotInfo.history" class="history-info">
          <h4>历史文化</h4>
          <p>{{ hotspotInfo.history }}</p>
        </div>
        <button v-if="hotspotInfo.action" class="preview-btn" @click="handleHotspotAction(hotspotInfo.action)">
          {{ hotspotInfo.actionText }}
        </button>
      </div>
    </div>

    <!-- 底部悬浮操作栏 -->
    <footer class="floating-footer">
      <div class="container">
        <div class="footer-content">
          <div class="view-control">
            <button class="control-btn" @click="toggleViewMode">
              {{ isFirstPerson ? '第三人称' : '第一人称' }}
            </button>
            <button class="control-btn" @click="toggleAutoTour">
              {{ autoTour ? '停止导览' : '开启导览' }}
            </button>
          </div>
          <button class="fullscreen-btn" @click="toggleFullscreen">全屏</button>
          <button class="book-btn" @click="bookWinterFishingTour">预订冬捕3日游</button>
        </div>
      </div>
    </footer>

    <!-- 侧边栏（可收起） -->
    <aside class="sidebar" :class="{ 'collapsed': sidebarCollapsed }">
      <button class="toggle-sidebar" @click="toggleSidebar">
        {{ sidebarCollapsed ? '展开' : '收起' }}
      </button>
      <div class="sidebar-content">
        <h3>查干湖冬捕非遗介绍</h3>
        <p>{{ winterFishingDescription }}</p>
        
        <h3>冬捕季时间</h3>
        <div class="season-info">
          <p>每年12月中旬至次年2月</p>
          <p>最佳观赏时间：12月28日（冬捕节）</p>
        </div>
        
        <h3>周边乡宿推荐</h3>
        <div class="homestay-recommendations">
          <div class="homestay-item" v-for="homestay in homestays" :key="homestay.id">
            <h4>{{ homestay.name }}</h4>
            <p>{{ homestay.description }}</p>
            <button class="btn btn-sm">查看</button>
          </div>
        </div>
        
        <h3>渔猎文创推荐</h3>
        <div class="文创-recommendations">
          <div class="文创-item" v-for="product in products" :key="product.id">
            <h4>{{ product.name }}</h4>
            <p>{{ product.description }}</p>
            <button class="btn btn-sm">查看</button>
          </div>
        </div>
        
        <!-- 互动游戏入口 -->
        <div class="game-entry">
          <button class="game-btn" @click="showIceFishingGame = true">
            🎣 冬捕小游戏
          </button>
        </div>
      </div>
    </aside>
    
    <!-- 游戏模态框 -->
    <IceFishingGame
      :visible="showIceFishingGame"
      @close="showIceFishingGame = false"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import IceFishingGame from './IceFishingGame.vue'

const router = useRouter()

// 游戏状态
const showIceFishingGame = ref(false)
const panoramaRef = ref(null)
const selectedScene = ref('net-pulling')
const showHotspotCard = ref(false)
const hotspotInfo = ref({})
const isFirstPerson = ref(true)
const autoTour = ref(false)
const isMuted = ref(false)
const sidebarCollapsed = ref(false)
const isPlaying = ref(false)
const audioElement = ref(null)
const showBlackScreen = ref(false)
const doorOpening = ref(false)
const showWelcomeText = ref(false)

// 场景数据
const scenes = {
  'net-pulling': {
    name: '冰面拉网',
    description: '查干湖冬捕的核心环节，渔民们在冰面上协作拉网，收获鲜鱼。',
    panoramaImage: '/panorama/buyu.png'
  },
  'harvest': {
    name: '渔获丰收',
    description: '渔网出水，鲜鱼跳跃，渔民们收获丰收的喜悦。',
    panoramaImage: '/panorama/buyu.png'
  },
  'ceremony': {
    name: '祭湖醒网仪式',
    description: '查干湖冬捕的传统仪式，祈求丰收和平安。',
    panoramaImage: '/panorama/buyu.png'
  }
}

// 当前场景
const currentScene = computed(() => scenes[selectedScene.value])

// 冬捕描述
const winterFishingDescription = '查干湖冬捕是中国吉林省的传统渔业活动，已有上千年历史，被列入国家级非物质文化遗产名录。每年冬季，渔民们在结冰的湖面上凿冰洞、下网、拉网，收获鲜鱼。冬捕过程中还保留着传统的祭湖醒网仪式，体现了对自然的敬畏和感恩。'

// 热点信息
const hotspotInfos = {
  'net': {
    title: '渔网',
    content: '查干湖冬捕使用的渔网长达2000多米，宽约20米，是渔民们在冰下捕鱼的重要工具。渔网由专业工匠手工编织，非常结实耐用。',
    history: '传统渔网编织技艺已有数百年历史，是查干湖渔民的传家本领。'
  },
  'winch': {
    title: '马拉绞盘',
    content: '马拉绞盘是冬捕中用于拉网的重要工具，由马匹拉动绞盘，将渔网从冰下缓缓拉出。这是一种传统的拉网方式，体现了人与自然的和谐共处。',
    history: '马拉绞盘的使用可以追溯到古代，是查干湖冬捕的特色之一。'
  },
  'tools': {
    title: '冬捕工具',
    content: '冬捕工具包括冰镩、穿杆、扭矛等，这些工具都是渔民们根据长期的实践经验设计的，用于凿冰洞、下网、拉网等操作。',
    history: '这些工具的使用方法和制作工艺代代相传，是查干湖冬捕文化的重要组成部分。'
  },
  'fish': {
    title: '查干湖有机鱼',
    content: '查干湖盛产胖头鱼、鲤鱼、鲫鱼等多种淡水鱼，肉质鲜美，营养丰富。这里的鱼都是自然生长，是真正的有机食品。',
    history: '查干湖有机鱼已获得国家有机认证，远销国内外，深受消费者喜爱。',
    action: 'viewFish',
    actionText: '查看渔获展示'
  }
}

// 周边乡宿
const homestays = [
  {
    id: 1,
    name: '查干湖渔家乐',
    description: '位于湖边的传统渔家乐，提供新鲜的湖鱼和舒适的住宿环境。'
  },
  {
    id: 2,
    name: '冰雪民宿',
    description: '特色冰雪主题民宿，体验东北传统火炕，欣赏湖景。'
  },
  {
    id: 3,
    name: '生态度假村',
    description: '生态环保度假村，提供多种休闲娱乐设施。'
  }
]

// 渔猎文创
const products = [
  {
    id: 1,
    name: '冬捕纪念币',
    description: '查干湖冬捕主题纪念币，采用传统工艺制作。'
  },
  {
    id: 2,
    name: '鱼形挂件',
    description: '以查干湖鲜鱼为原型的精美挂件，寓意年年有余。'
  },
  {
    id: 3,
    name: '冬捕文化书签',
    description: '精美的冬捕文化主题书签，展现传统渔猎文化。'
  }
]

// 返回首页
const goHome = () => {
  router.push('/')
}

// 返回上一页
const goBack = () => {
  router.back()
}

// 切换场景
const changeScene = () => {
  initPannellum()
  console.log('切换到场景:', selectedScene.value)
  
  // 切换场景时自动播放音频
  if (!isPlaying.value) {
    isPlaying.value = true
    if (audioElement.value) {
      audioElement.value.play().catch(err => {
        console.error('音频播放失败:', err)
      })
    }
  }
}

// 初始化音频
const initAudio = () => {
  if (audioElement.value) {
    audioElement.value.pause()
    audioElement.value.currentTime = 0
  }
  
  const audio = new Audio()
  audio.src = '/peiying/songhuayan.mp3'
  audio.loop = true
  audio.volume = 0.5
  audioElement.value = audio
  
  if (isPlaying.value) {
    audio.play().catch(err => {
      console.error('音频播放失败:', err)
    })
  }
}

// 切换音频播放/暂停
const toggleAudio = () => {
  if (!audioElement.value) {
    initAudio()
  }
  
  if (isPlaying.value) {
    audioElement.value.pause()
  } else {
    audioElement.value.play().catch(err => {
      console.error('音频播放失败:', err)
    })
  }
  isPlaying.value = !isPlaying.value
}

// 初始化 Pannellum 360°全景
const initPannellum = () => {
  const panorama = panoramaRef.value
  if (panorama) {
    if (window.pannellumInstance) {
      window.pannellumInstance.destroy()
    }
    
    const panoramaImage = currentScene.value.panoramaImage
    console.log('初始化Pannellum，图片:', panoramaImage)
    
    // 配置热点
    const hotspots = [
      {
        pitch: 0,
        yaw: -45,
        type: 'info',
        text: '渔网',
        id: 'hotspot-net',
        CSSClass: 'preview-hotspot'
      },
      {
        pitch: -5,
        yaw: 45,
        type: 'info',
        text: '马拉绞盘',
        id: 'hotspot-winch',
        CSSClass: 'preview-hotspot'
      },
      {
        pitch: 5,
        yaw: 0,
        type: 'info',
        text: '冬捕工具',
        id: 'hotspot-tools',
        CSSClass: 'preview-hotspot'
      },
      {
        pitch: -10,
        yaw: 90,
        type: 'info',
        text: '查干湖有机鱼',
        id: 'hotspot-fish',
        CSSClass: 'preview-hotspot'
      }
    ]
    console.log('热点配置:', hotspots)
    
    // 初始化 Pannellum
    window.pannellumInstance = pannellum.viewer('panorama', {
      type: 'equirectangular',
      panorama: panoramaImage,
      autoLoad: true,
      showControls: true,
      hotSpots: hotspots
    })
    console.log('Pannellum实例创建成功:', window.pannellumInstance)
    
    // 隐藏加载提示
    const loading = panorama.querySelector('.loading')
    if (loading) {
      loading.style.display = 'none'
    }
    
    // 绑定热点点击事件
    window.pannellumInstance.on('hotspot-click', function(hotspot) {
      console.log('=== 冬捕场景热点点击 ===')
      
      let hotspotText = ''
      if (hotspot && hotspot.target) {
        const spanElement = hotspot.target.querySelector('span')
        if (spanElement) {
          hotspotText = spanElement.textContent || spanElement.innerText || ''
        }
      }
      
      console.log('热点文本:', hotspotText)
      
      if (hotspotText.includes('渔网')) {
        showHotspotInfo('net')
      } else if (hotspotText.includes('马拉绞盘')) {
        showHotspotInfo('winch')
      } else if (hotspotText.includes('冬捕工具')) {
        showHotspotInfo('tools')
      } else if (hotspotText.includes('查干湖有机鱼')) {
        showHotspotInfo('fish')
      } else {
        console.log('点击了未知热点')
      }
    })
    
    console.log('=== 热点点击事件绑定完成 ===')
  } else {
    console.error('panoramaRef不存在')
  }
}

// 显示热点信息
const showHotspotInfo = (type) => {
  hotspotInfo.value = hotspotInfos[type]
  showHotspotCard.value = true
}

// 关闭热点信息
const closeHotspotCard = () => {
  showHotspotCard.value = false
}

// 处理热点操作
const handleHotspotAction = (action) => {
  if (action === 'viewFish') {
    createImageViewer('/panorama/buyu.png')
    closeHotspotCard()
  }
}

// 切换视角模式
const toggleViewMode = () => {
  isFirstPerson.value = !isFirstPerson.value
}

// 切换自动导览
const toggleAutoTour = () => {
  autoTour.value = !autoTour.value
  if (window.pannellumInstance) {
    if (autoTour.value) {
      // 开始自动导览
    } else {
      // 停止自动导览
    }
  }
}

// 切换全屏
const toggleFullscreen = () => {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen()
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen()
    }
  }
}

// 预订冬捕3日游
const bookWinterFishingTour = () => {
  router.push('/intelligent-tour/winter-fishing')
}

// 切换侧边栏
const toggleSidebar = () => {
  sidebarCollapsed.value = !sidebarCollapsed.value
}

// 创建图片查看器
const createImageViewer = (imageUrl) => {
  console.log('创建图片查看器，图片URL:', imageUrl)
  
  let viewer = document.getElementById('image-viewer')
  if (viewer) {
    document.body.removeChild(viewer)
  }
  
  viewer = document.createElement('div')
  viewer.id = 'image-viewer'
  viewer.style.position = 'fixed'
  viewer.style.top = '0'
  viewer.style.left = '0'
  viewer.style.width = '100vw'
  viewer.style.height = '100vh'
  viewer.style.backgroundColor = 'rgba(0, 0, 0, 0.9)'
  viewer.style.display = 'flex'
  viewer.style.justifyContent = 'center'
  viewer.style.alignItems = 'center'
  viewer.style.zIndex = '9999'
  viewer.style.cursor = 'pointer'
  
  const img = document.createElement('img')
  img.src = imageUrl
  img.style.maxWidth = '90%'
  img.style.maxHeight = '90%'
  img.style.objectFit = 'contain'
  
  viewer.appendChild(img)
  
  viewer.addEventListener('click', () => {
    document.body.removeChild(viewer)
  })
  
  document.body.appendChild(viewer)
  console.log('图片查看器创建成功')
}

// 显示欢迎文字
const showWelcomeMessage = () => {
  showWelcomeText.value = true
  setTimeout(() => {
    showWelcomeText.value = false
  }, 4000)
}

// 生命周期钩子
onMounted(() => {
  initPannellum()
  initAudio()
  
  // 页面加载完成后自动播放音频
  setTimeout(() => {
    isPlaying.value = true
    if (audioElement.value) {
      audioElement.value.play().catch(err => {
        console.error('音频播放失败:', err)
      })
    }
  }, 1000)
  
  setTimeout(() => {
    showWelcomeMessage()
  }, 500)
})

onUnmounted(() => {
  if (window.pannellumInstance) {
    window.pannellumInstance.destroy()
  }
  
  if (audioElement.value) {
    audioElement.value.pause()
    audioElement.value = null
  }
})
</script>

<style scoped>
/* 全局样式 */
.winter-fishing-360 {
  position: relative;
  height: 100vh;
  overflow: hidden;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
}

/* 背景装饰元素 */
.winter-fishing-360::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 30%, rgba(76, 175, 80, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(33, 150, 243, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 40% 80%, rgba(255, 193, 7, 0.08) 0%, transparent 50%);
  z-index: 0;
}

/* 顶部导航栏 */
.floating-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  z-index: 1000;
  backdrop-filter: blur(12px);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
}

.nav-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 0;
  max-width: 1200px;
  margin: 0 auto;
  width: 90%;
}

.logo {
  font-size: 24px;
  font-weight: 700;
  cursor: pointer;
  font-family: 'Microsoft YaHei', sans-serif;
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
}

.back-btn,
.share-btn,
.audio-btn {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  font-size: 16px;
  cursor: pointer;
  padding: 10px 20px;
  border-radius: 8px;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
}

.back-btn:hover,
.share-btn:hover,
.audio-btn:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
}

.audio-control {
  margin-right: 12px;
}

.audio-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  padding: 10px 16px;
}

.scene-selector select {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 16px;
  font-family: 'Microsoft YaHei', sans-serif;
  cursor: pointer;
  appearance: none;
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="white" viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>');
  background-repeat: no-repeat;
  background-position: right 12px center;
  padding-right: 40px;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
}

.scene-selector select:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.1));
  border-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
}

/* 主视觉区 */
.panorama-container {
  position: relative;
  width: 100%;
  height: 100vh;
  z-index: 1;
}

.panorama-view {
  width: 100%;
  height: 100%;
  position: relative;
  border-radius: 0;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.panorama-view::before {
  content: '';
  position: absolute;
  top: 20px;
  left: 20px;
  right: 20px;
  bottom: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  pointer-events: none;
  z-index: 2;
}

.panorama-view::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.1) 0%,
    rgba(0, 0, 0, 0) 20%,
    rgba(0, 0, 0, 0) 80%,
    rgba(0, 0, 0, 0.1) 100%
  );
  pointer-events: none;
  z-index: 2;
}

.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 18px;
  font-family: 'Microsoft YaHei', sans-serif;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.5));
  padding: 20px 40px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(10px);
  z-index: 10;
}

/* 热点样式 */
.pnlm-hotspot.preview-hotspot {
  background: linear-gradient(135deg, #2196F3, #1976D2);
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  color: white;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 100px;
  height: auto;
}

.pnlm-hotspot.preview-hotspot:hover {
  background: linear-gradient(135deg, #1976D2, #1565C0);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(33, 150, 243, 0.4);
}

/* 黑屏过渡效果 */
.black-screen {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #000;
  z-index: 2000;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.door-left,
.door-right {
  position: absolute;
  top: 0;
  width: 50%;
  height: 100%;
  background-color: #000;
  transition: transform 1.5s cubic-bezier(0.4, 0.0, 0.2, 1);
}

.door-left {
  left: 0;
  transform: translateX(0);
}

.door-right {
  right: 0;
  transform: translateX(0);
}

.black-screen.door-open .door-left {
  transform: translateX(-100%);
}

.black-screen.door-open .door-right {
  transform: translateX(100%);
}

/* 欢迎文字效果 */
.welcome-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  z-index: 1500;
  color: white;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
  pointer-events: none;
}

.welcome-text h1 {
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 16px;
  color: #fff;
  text-shadow: 0 0 20px rgba(33, 150, 243, 0.8);
}

.welcome-text p {
  font-size: 24px;
  color: rgba(255, 255, 255, 0.9);
}

.welcome-fade-enter-active {
  animation: welcomeIn 0.8s ease-out;
}

.welcome-fade-leave-active {
  animation: welcomeOut 1s ease-in;
}

@keyframes welcomeIn {
  0% {
    opacity: 0;
    transform: translate(-50%, -50%) scale(0.8);
  }
  100% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
}

@keyframes welcomeOut {
  0% {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
  100% {
    opacity: 0;
    transform: translate(-50%, -50%) scale(1.1);
  }
}

/* 热点信息卡片 */
.hotspot-card {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.9));
  padding: 30px;
  border-radius: 16px;
  width: 80%;
  max-width: 500px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
  z-index: 1001;
  border: 1px solid rgba(33, 150, 243, 0.2);
  animation: slideIn 0.3s ease-out;
  backdrop-filter: blur(10px);
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translate(-50%, -50%) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
}

.close-card {
  position: absolute;
  top: 16px;
  right: 16px;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.05));
  border: 1px solid rgba(0, 0, 0, 0.1);
  font-size: 20px;
  cursor: pointer;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  color: #333;
}

.close-card:hover {
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.1));
  transform: scale(1.1);
}

.hotspot-card h3 {
  margin-top: 0;
  margin-bottom: 20px;
  color: #2196F3;
  font-family: 'Microsoft YaHei', sans-serif;
  font-size: 22px;
  font-weight: 600;
  border-bottom: 2px solid rgba(33, 150, 243, 0.2);
  padding-bottom: 10px;
}

.hotspot-card p {
  margin-bottom: 20px;
  line-height: 1.6;
  color: #333;
  font-size: 16px;
}

.history-info {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid rgba(33, 150, 243, 0.2);
}

.history-info h4 {
  margin-top: 0;
  margin-bottom: 12px;
  font-size: 16px;
  color: #2196F3;
  font-weight: 600;
}

.preview-btn {
  background: linear-gradient(135deg, #2196F3, #1976D2);
  color: white;
  border: none;
  padding: 14px 28px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
  font-size: 16px;
  margin-top: 24px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.preview-btn:hover {
  background: linear-gradient(135deg, #1976D2, #1565C0);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(33, 150, 243, 0.4);
}

/* 底部悬浮操作栏 */
.floating-footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  z-index: 1000;
  backdrop-filter: blur(12px);
  box-shadow: 0 -2px 20px rgba(0, 0, 0, 0.3);
}

.footer-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 0;
  max-width: 1200px;
  margin: 0 auto;
  width: 90%;
}

.view-control {
  display: flex;
  gap: 12px;
}

.control-btn {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
  font-size: 14px;
}

.control-btn:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
}

.fullscreen-btn {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
  font-size: 14px;
}

.fullscreen-btn:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
}

.book-btn {
  background: linear-gradient(135deg, #2196F3, #1976D2);
  color: white;
  border: none;
  padding: 14px 28px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
  font-size: 16px;
}

.book-btn:hover {
  background: linear-gradient(135deg, #1976D2, #1565C0);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(33, 150, 243, 0.4);
}

/* 侧边栏 */
.sidebar {
  position: fixed;
  right: 0;
  top: 0;
  bottom: 0;
  width: 320px;
  background-color: rgba(0, 0, 0, 0.85);
  color: white;
  z-index: 999;
  transition: transform 0.3s ease;
  backdrop-filter: blur(12px);
  box-shadow: -2px 0 20px rgba(0, 0, 0, 0.3);
}

.sidebar.collapsed {
  transform: translateX(270px);
}

.toggle-sidebar {
  position: absolute;
  left: -60px;
  top: 50%;
  transform: translateY(-50%);
  background: linear-gradient(135deg, #2196F3, #1976D2);
  color: white;
  border: none;
  padding: 16px 12px;
  border-radius: 12px 0 0 12px;
  cursor: pointer;
  writing-mode: vertical-rl;
  text-orientation: mixed;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: -2px 0 10px rgba(33, 150, 243, 0.3);
}

.toggle-sidebar:hover {
  background: linear-gradient(135deg, #1976D2, #1565C0);
  transform: translateY(-50%) scale(1.05);
}

.sidebar-content {
  padding: 24px;
  height: 100%;
  overflow-y: auto;
}

.sidebar-content h3 {
  margin-top: 0;
  margin-bottom: 16px;
  color: #2196F3;
  font-family: 'Microsoft YaHei', sans-serif;
  font-size: 18px;
  border-bottom: 2px solid rgba(33, 150, 243, 0.3);
  padding-bottom: 8px;
}

.sidebar-content p {
  margin-bottom: 24px;
  line-height: 1.6;
  opacity: 0.85;
  font-size: 14px;
}

.season-info {
  background-color: rgba(255, 255, 255, 0.1);
  padding: 16px;
  border-radius: 8px;
  margin-bottom: 24px;
}

.season-info p {
  margin: 0 0 8px 0;
  font-size: 14px;
}

.homestay-recommendations,
.文创-recommendations {
  margin-top: 24px;
}

.homestay-item,
.文创-item {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 16px;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.homestay-item:hover,
.文创-item:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.1));
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
  border-color: rgba(33, 150, 243, 0.3);
}

.homestay-item h4,
.文创-item h4 {
  margin: 0 0 8px 0;
  font-size: 16px;
  color: #2196F3;
}

.homestay-item p,
.文创-item p {
  margin: 0 0 16px 0;
  font-size: 14px;
  opacity: 0.8;
  line-height: 1.5;
}

.homestay-item .btn-sm,
.文创-item .btn-sm {
  font-size: 14px;
  padding: 8px 20px;
  background: linear-gradient(135deg, #2196F3, #1976D2);
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.homestay-item .btn-sm:hover,
.文创-item .btn-sm:hover {
  background: linear-gradient(135deg, #1976D2, #1565C0);
  transform: translateY(-1px);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .nav-content {
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
  }
  
  .logo {
    font-size: 20px;
  }
  
  .scene-selector {
    order: 3;
    width: 100%;
  }
  
  .scene-selector select {
    width: 100%;
  }
  
  .footer-content {
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
  }
  
  .sidebar {
    width: 280px;
  }
  
  .sidebar.collapsed {
    transform: translateX(230px);
  }
}

/* 游戏入口样式 */
.game-entry {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.game-btn {
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.game-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
}
</style>