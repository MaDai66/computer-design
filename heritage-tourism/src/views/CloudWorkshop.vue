<template>
  <div class="cloud-workshop">
    <!-- 顶部导航栏（悬浮） -->
    <header class="floating-nav">
      <div class="container">
        <div class="nav-content">
          <div class="logo" @click="goHome">吉林遗珍</div>
          <button class="back-btn" @click="goBack">返回</button>
          <div class="workshop-selector">
          <select v-model="selectedWorkshop" @change="changeWorkshop">
            <option value="paper-cutting">满族剪纸工坊</option>
            <option value="paper-cutting-extended">满族剪纸工坊 - 延伸场景</option>
            <option value="inkstone">松花砚雕刻工坊</option>
            <option value="rice-cake">朝鲜族打糕制作工坊</option>
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
        <!-- Pannellum 360°全景将在这里渲染 -->
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
          <h1>欢迎来到剪纸工坊</h1>
          <p>探索满族剪纸的千年文化</p>
        </div>
      </transition>
      
      <!-- 热点信息卡片 -->
      <div v-if="showHotspotCard" class="hotspot-card">
        <button class="close-card" @click="closeHotspotCard">&times;</button>
        <h3>{{ hotspotInfo.title }}</h3>
        <p>{{ hotspotInfo.content }}</p>
        <div v-if="hotspotInfo.artist" class="artist-info">
          <h4>传承人</h4>
          <p>{{ hotspotInfo.artist }}</p>
        </div>
        <button class="preview-btn" @click="startPreview">开始预览</button>
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
          <div class="volume-control">
            
          </div>
          <button class="fullscreen-btn" @click="toggleFullscreen">全屏</button>
          <button class="book-btn" @click="bookOfflineExperience">预约线下体验</button>
        </div>
      </div>
    </footer>

    <!-- 侧边栏（可收起） -->
    <aside class="sidebar" :class="{ 'collapsed': sidebarCollapsed }">
      <button class="toggle-sidebar" @click="toggleSidebar">
        {{ sidebarCollapsed ? '展开' : '收起' }}
      </button>
      <div class="sidebar-content">
        <h3>工坊简介</h3>
        <p>{{ workshopDescription }}</p>
        
        <h3>传承人信息</h3>
        <div class="artist-profile">
          <img :src="currentWorkshop.artistImage" :alt="currentWorkshop.artistName" />
          <h4>{{ currentWorkshop.artistName }}</h4>
          <p>{{ currentWorkshop.artistDesc }}</p>
        </div>
        
        <h3>推荐</h3>
        <div class="recommendations">
          <div class="recommendation-item" v-for="item in recommendations" :key="item.id">
            <h4>{{ item.title }}</h4>
            <p>{{ item.description }}</p>
            <button class="btn btn-sm">查看</button>
          </div>
        </div>
        <h3>互动游戏</h3>
        <div class="recommendation-item" v-if="selectedWorkshop === 'paper-cutting-extended'">
          <h4>剪纸拼图小游戏</h4>
          <p>完成拼图，体验满族剪纸艺术的魅力</p>
          <button class="btn btn-sm" @click="openPuzzleGame">开始游戏</button>
        </div>

      </div>
    </aside>
    <!-- 拼图游戏组件 -->
    <PuzzleGame 
      :visible="showPuzzleGame" 
      @close="closePuzzleGame" 
    />

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import PuzzleGame from './PuzzleGame.vue'
const showPuzzleGame = ref(false)

const router = useRouter()
const panoramaRef = ref(null)
const selectedWorkshop = ref('paper-cutting')
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

// 工坊数据
const workshops = {
  'paper-cutting': {
    name: '满族剪纸工坊',
    description: '满族剪纸是中国传统民间艺术之一，具有悠久的历史和独特的艺术风格。本工坊展示了满族剪纸的制作过程，包括设计、裁剪、染色等工序。',
    artistName: '王阿姨',
    artistDesc: '从事剪纸艺术30余年，作品多次获奖，是满族剪纸的代表性传承人。',
    artistImage: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Elderly%20Chinese%20woman%20paper%20cutting%20artist&image_size=portrait_4_3',
    panoramaImage: '/panorama/jianzhi.png',
    audioFile: '/peiying/jianzhi.mp3'
  },
  'paper-cutting-extended': {
    name: '满族剪纸工坊 - 延伸场景',
    description: '满族剪纸工坊的延伸场景，展示了更多剪纸作品和制作工具，让您更深入了解满族剪纸的魅力。',
    artistName: '王阿姨',
    artistDesc: '从事剪纸艺术30余年，作品多次获奖，是满族剪纸的代表性传承人。',
    artistImage: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Elderly%20Chinese%20woman%20paper%20cutting%20artist&image_size=portrait_4_3',
    panoramaImage: '/panorama/jianzhi-jixu.png',
    audioFile: '/peiying/jianzhi.mp3'
  },
  'inkstone': {
    name: '松花砚雕刻工坊',
    description: '松花砚是吉林特产，以其石质细腻、温润如玉而闻名。本工坊展示了松花砚的雕刻技艺，从选石到雕刻完成的全过程。',
    artistName: '李师傅',
    artistDesc: '松花砚雕刻技艺传承人，从事砚台雕刻20余年，作品远销国内外。',
    artistImage: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Middle-aged%20Chinese%20man%20inkstone%20carver&image_size=portrait_4_3',
    panoramaImage: '/panorama/diaoke.png',
    audioFile: '/src/assets/peiying/songhuayan.mp3'
  },
  'rice-cake': {
    name: '朝鲜族打糕制作工坊',
    description: '朝鲜族打糕是吉林延边地区的传统美食，以其软糯香甜而受到喜爱。本工坊展示了打糕的传统制作工艺。',
    artistName: '金师傅',
    artistDesc: '朝鲜族传统打糕技艺传承人，制作打糕40余年，坚持传统工艺。',
    artistImage: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Korean%20elderly%20man%20making%20rice%20cake&image_size=portrait_4_3',
    panoramaImage: '/panorama/dagao.png',
    audioFile: '/src/assets/peiying/dagao.mp3'
  }
}

// 推荐内容
const recommendations = [
  {
    id: 1,
    title: '满族剪纸体验课',
    description: '亲手学习满族剪纸技艺，制作属于自己的剪纸作品',
    type: 'experience'
  },
  {
    id: 2,
    title: '松花砚文创产品',
    description: '精美的松花砚文创产品，兼具实用性和艺术性',
    type: 'product'
  },
  {
    id: 3,
    title: '朝鲜族美食之旅',
    description: '品尝正宗朝鲜族美食，体验朝鲜族文化',
    type: 'tour'
  }
]

// 当前工坊
const currentWorkshop = computed(() => workshops[selectedWorkshop.value])

// 工坊描述
const workshopDescription = computed(() => currentWorkshop.value.description)

// 热点信息
const hotspotInfos = {
  'tool': {
    title: '剪纸工具',
    content: '这些是满族剪纸常用的工具，包括剪刀、刻刀、蜡盘等。剪刀用于剪制简单的图案，刻刀用于精细的雕刻，蜡盘用于保护桌面。',
    artist: '王阿姨使用这些工具已有30余年，她能熟练地用剪刀剪出各种复杂的图案。'
  },
  'material': {
    title: '剪纸材料',
    content: '满族剪纸通常使用红色的宣纸，因为红色在中国传统文化中象征着吉祥和喜庆。这些纸张经过特殊处理，质地柔软，易于裁剪。',
    artist: '王阿姨说，选择好的纸张是制作精美剪纸的关键。'
  },
  'artist': {
    title: '传承人工作台',
    content: '这是王阿姨的工作台，上面摆放着她的工具和作品。她每天都会在这里创作新的剪纸作品，传承满族剪纸技艺。',
    artist: '王阿姨从事剪纸艺术30余年，她的作品多次在国内外展览中获奖。'
  }
}

// 返回上一页
const goBack = () => {
  router.back()
}

// 返回首页
const goHome = () => {
  router.push('/')
}

// 切换工坊
const changeWorkshop = () => {
  // 重新初始化 Pannellum 全景
  initPannellum()
  // 切换音频
  initAudio()
  console.log('切换到工坊:', selectedWorkshop.value)
  
  // 如果切换到延伸场景，自动播放音频
  if (selectedWorkshop.value === 'paper-cutting-extended') {
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
  // 停止当前音频
  if (audioElement.value) {
    audioElement.value.pause()
    audioElement.value.currentTime = 0
  }
  
  // 创建新的音频元素
  const audio = new Audio()
  audio.src = currentWorkshop.value.audioFile
  audio.loop = true
  audio.volume = 0.5
  audioElement.value = audio
  
  // 如果之前是播放状态，则继续播放
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
    // 清除之前的 Pannellum 实例
    if (window.pannellumInstance) {
      window.pannellumInstance.destroy()
    }
    
    const panoramaImage = currentWorkshop.value.panoramaImage
    console.log('初始化Pannellum，图片:', panoramaImage);
    
    // 配置热点
    let hotspots = [];
    if (selectedWorkshop.value === 'paper-cutting') {
      hotspots = [
        {
          pitch: 0,
          yaw: 0,
          type: 'info',
          text: '开始预览',
          id: 'hotspot3',
          CSSClass: 'preview-hotspot'
        },
        {
          pitch: 9,
          yaw: -62,
          type: 'info',
          text: '剪纸传情',
          id: 'hotspot-empty',
          CSSClass: 'preview-hotspot'
        },
        {
          pitch: 8,
          yaw: 59,
          type: 'info',
          text: '非遗传承',
          id: 'hotspot-craft',
          CSSClass: 'preview-hotspot'
        }
      ];
      console.log('热点配置:', hotspots);
    } else if (selectedWorkshop.value === 'paper-cutting-extended') {
      hotspots = [
        {
          pitch: 18,
          yaw: 60,
          type: 'info',
          text: '剪纸作品-新娘出嫁',
          id: 'hotspot-extended',
          CSSClass: 'preview-hotspot'
        },
        {
          pitch: -30,
          yaw: 0,
          type: 'info',
          text: '剪纸作品',
          id: 'hotspot-papercut',
          CSSClass: 'preview-hotspot'
        },
        {
          pitch: 10,
          yaw: 88,
          type: 'info',
          text: '剪纸小游戏',
          id: 'hotspot-more',
          CSSClass: 'preview-hotspot'
        },
        {
          pitch: -10,
          yaw: -30,
          type: 'info',
          text: '制作人工具台',
          id: 'hotspot-workbench',
          CSSClass: 'preview-hotspot'
        }
      ];
      console.log('延伸场景热点配置:', hotspots);
    } else {
      console.log('当前场景不显示热点');
    }
    
    // 初始化 Pannellum
    window.pannellumInstance = pannellum.viewer('panorama', {
      type: 'equirectangular',
      panorama: panoramaImage,
      autoLoad: true,
      showControls: true,
      hotSpots: hotspots
    })
    console.log('Pannellum实例创建成功:', window.pannellumInstance);
    
    // 隐藏加载提示
    const loading = panorama.querySelector('.loading')
    if (loading) {
      loading.style.display = 'none'
    }
    
    console.log('=== 开始绑定热点点击事件 ===');
    console.log('当前场景:', selectedWorkshop.value);
    console.log('Pannellum实例:', window.pannellumInstance);
    
    // 根据场景类型绑定不同的热点点击事件
    if (selectedWorkshop.value === 'paper-cutting') {
      // 第一个场景：区分不同热点
      console.log('绑定第一个场景热点点击事件');
      window.pannellumInstance.on('hotspot-click', function(hotspot) {
        console.log('=== 第一个场景热点点击 ===');
        
        // 获取热点文本
        let hotspotText = '';
        if (hotspot && hotspot.target) {
          const spanElement = hotspot.target.querySelector('span');
          if (spanElement) {
            hotspotText = spanElement.textContent || spanElement.innerText || '';
          }
        }
        
        console.log('热点文本:', hotspotText);
        
        if (hotspotText.includes('开始预览')) {
          console.log('调用startPreview函数');
          startPreview();
        } else if (hotspotText.includes('剪纸传情')) {
          console.log('点击了剪纸传情热点，显示文字');
          showPaperCutLoveText();
        } else if (hotspotText.includes('非遗传承')) {
          console.log('点击了非遗传承热点，显示文字');
          showIntangibleHeritageText();
        } else {
          console.log('点击了其他热点，不执行任何操作');
        }
      });
    } else if (selectedWorkshop.value === 'paper-cutting-extended') {
      // 延伸场景：使用独立的热点点击处理
      console.log('绑定延伸场景热点点击事件');
      
      // 添加DOM点击事件监听器
      setTimeout(() => {
        const panoramaContainer = document.getElementById('panorama');
        if (panoramaContainer) {
          console.log('找到全景容器，添加点击事件监听器');
          
          panoramaContainer.addEventListener('click', function(e) {
            console.log('=== 延伸场景DOM点击事件触发 ===');
            console.log('点击目标:', e.target);
            
            // 检查是否点击了热点
            let target = e.target;
            let foundHotspot = false;
            
            while (target) {
              if (target.classList && target.classList.contains('pnlm-hotspot')) {
                foundHotspot = true;
                break;
              }
              target = target.parentElement;
            }
            
            if (foundHotspot) {
              console.log('点击了热点元素:', target);
              console.log('热点元素HTML:', target.innerHTML);
              
              // 获取热点文本 - 从子span元素获取
              let hotspotText = '';
              const spanElement = target.querySelector('span');
              if (spanElement) {
                hotspotText = spanElement.textContent || spanElement.innerText || '';
                console.log('从span元素获取热点文本:', hotspotText);
              } else {
                // 尝试其他方式获取
                hotspotText = target.textContent || target.innerText || '';
                console.log('从目标元素获取热点文本:', hotspotText);
              }
              
              console.log('热点文本:', hotspotText);
              
              // 根据热点文本执行操作
              if (hotspotText.includes('剪纸小游戏') || hotspotText.includes('拼图小游戏')) {
                console.log('点击了剪纸小游戏热点，打开拼图游戏');
                openPuzzleGame();
              } else if (hotspotText.includes('剪纸作品-新娘出嫁')) {
                console.log('点击了剪纸作品-新娘出嫁热点，显示剪纸作品-新娘出嫁.png');
                createImageViewer('/panorama/剪纸作品-新娘出嫁.png');
              } else if (hotspotText.includes('剪纸作品')) {
                console.log('点击了剪纸作品热点，显示剪纸作品.png');
                createImageViewer('/panorama/剪纸作品.png');
              } else if (hotspotText.includes('制作人工具台')) {
                console.log('点击了制作人工具台热点，在新窗口中打开链接');
                window.open('https://www.kivicube.com/scenes/FdYIh1UgQLBDd82HT0QwyCFEBAVAefCt', '_blank');
              } else {
                console.log('延伸场景点击了未知热点，热点文本:', hotspotText);
              }
            } else {
              console.log('点击的不是热点');
            }
          });
          
          console.log('延伸场景DOM点击事件监听器添加完成');
        } else {
          console.error('未找到全景容器');
        }
      }, 1000); // 延迟1秒确保Pannellum完全加载
      
      console.log('延伸场景热点点击事件绑定完成');
    }
    
    console.log('=== 热点点击事件绑定完成（场景:', selectedWorkshop.value, '）===');
  } else {
    console.error('panoramaRef不存在');
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

// 切换视角模式
const toggleViewMode = () => {
  isFirstPerson.value = !isFirstPerson.value
  // Pannellum 自动支持视角控制，无需额外代码
}

// 切换自动导览
const toggleAutoTour = () => {
  autoTour.value = !autoTour.value
  // 这里可以添加自动导览逻辑
  if (window.pannellumInstance) {
    if (autoTour.value) {
      // 开始自动导览
      // 可以使用 Pannellum 的动画功能
    } else {
      // 停止自动导览
    }
  }
}

// 切换静音
const toggleMute = () => {
  isMuted.value = !isMuted.value
  // 这里可以添加音频控制逻辑
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

// 预约线下体验
const bookOfflineExperience = () => {
  // 跳转到预约页面
  router.push('/booking')
}

// 开始预览
const startPreview = () => {
  console.log('开始预览函数被调用');
  
  // 实现镜头前移/视角放大效果
  if (window.pannellumInstance) {
    console.log('Pannellum实例存在');
    try {
      // 检查Pannellum实例是否有相关方法
      if (typeof window.pannellumInstance.getHfov === 'function') {
        // 获取当前视角
        const currentHfov = window.pannellumInstance.getHfov();
        console.log('当前视场角:', currentHfov);
        
        // 目标视角（更小的视场角意味着视角放大）
        const targetHfov = 50; // 设置一个更适中的目标值
        console.log('目标视场角:', targetHfov);
        
        // 第一阶段：视角归位（如果有偏移的话）
        const resetDuration = 500; // 归位动画时长
        const startResetTime = Date.now();
        
        // 保存初始状态
        const initialHfov = currentHfov;
        const initialYaw = window.pannellumInstance.getYaw ? window.pannellumInstance.getYaw() : 0;
        const initialPitch = window.pannellumInstance.getPitch ? window.pannellumInstance.getPitch() : 0;
        
        console.log('初始视角状态 - Hfov:', initialHfov, 'Yaw:', initialYaw, 'Pitch:', initialPitch);
        
        // 第一阶段动画：视角归位
        const animateReset = () => {
          const elapsed = Date.now() - startResetTime;
          const progress = Math.min(elapsed / resetDuration, 1);
          
          // 使用自然的缓动函数（模拟人的头部移动）
          const easeProgress = 1 - Math.pow(1 - progress, 4);
          
          // 归位到中心视角
          const resetYaw = initialYaw * (1 - easeProgress);
          const resetPitch = initialPitch * (1 - easeProgress);
          const resetHfov = initialHfov + (85 - initialHfov) * easeProgress; // 归位到默认视场角85
          
          if (window.pannellumInstance.setYaw && window.pannellumInstance.setPitch && window.pannellumInstance.setHfov) {
            window.pannellumInstance.setYaw(resetYaw);
            window.pannellumInstance.setPitch(resetPitch);
            window.pannellumInstance.setHfov(resetHfov);
          }
          
          if (progress < 1) {
            requestAnimationFrame(animateReset);
          } else {
            // 归位完成后开始第二阶段：视角推进
            console.log('视角归位完成，开始推进动画');
            startZoomAnimation(85, targetHfov, 2500);
          }
        };
        
        // 开始归位动画
        animateReset();
      } else {
        console.error('Pannellum实例没有getHfov方法');
        // 尝试直接设置视场角
        if (typeof window.pannellumInstance.setHfov === 'function') {
          console.log('直接设置视场角为50');
          window.pannellumInstance.setHfov(50);
        }
      }
    } catch (error) {
      console.error('执行预览时出错:', error);
    }
  } else {
    console.error('Pannellum实例不存在');
  }
}

// 第二阶段：视角推进动画
const startZoomAnimation = (startHfov, endHfov, duration) => {
  const startTime = Date.now();
  console.log('推进动画开始 - 起始:', startHfov, '目标:', endHfov, '时长:', duration);
  
  // 设置2.5秒后的黑屏计时器
  const blackScreenDelay = 2800; // 2.5秒
  let blackScreenTriggered = false;
  
  const checkBlackScreenTime = setInterval(() => {
    const elapsed = Date.now() - startTime;
    if (elapsed >= blackScreenDelay && !blackScreenTriggered) {
      blackScreenTriggered = true;
      triggerBlackScreenTransition();
      clearInterval(checkBlackScreenTime);
    }
  }, 50); // 每50毫秒检查一次
  
  // 模拟人的步伐节奏：分多段，每段有轻微的起伏
  const steps = 3; // 分成3步
  const stepDuration = duration / steps;
  
  let currentStep = 0;
  
  const animateStep = () => {
    if (currentStep >= steps) {
      console.log('推进动画完成');
      return;
    }
    
    const stepStartTime = Date.now();
    const stepStartHfov = startHfov + (endHfov - startHfov) * (currentStep / steps);
    const stepEndHfov = startHfov + (endHfov - startHfov) * ((currentStep + 1) / steps);
    
    const animatePerStep = () => {
      const elapsed = Date.now() - stepStartTime;
      const progress = Math.min(elapsed / stepDuration, 1);
      
      // 每一步使用自然的缓动函数，模拟人走路时的视线移动
      // 开始和结束时慢，中间稍快
      let easeProgress;
      if (progress < 0.3) {
        // 开始阶段：缓慢启动
        easeProgress = Math.pow(progress / 0.3, 2) * 0.3;
      } else if (progress < 0.7) {
        // 中间阶段：匀速前进
        easeProgress = 0.3 + (progress - 0.3) / 0.4 * 0.4;
      } else {
        // 结束阶段：缓慢停止，带轻微的"踩实"感
        const tailProgress = (progress - 0.7) / 0.3;
        easeProgress = 0.7 + (tailProgress - Math.pow(tailProgress, 2) * 0.3) * 0.3;
      }
      
      // 计算当前视场角
      const currentZoomHfov = stepStartHfov + (stepEndHfov - stepStartHfov) * easeProgress;
      
      // 设置新的视场角
      if (typeof window.pannellumInstance.setHfov === 'function') {
        window.pannellumInstance.setHfov(currentZoomHfov);
      }
      
      if (progress < 1) {
        requestAnimationFrame(animatePerStep);
      } else {
        // 这一步完成，开始下一步
        currentStep++;
        animateStep();
      }
    };
    
    animatePerStep();
  };
  
  animateStep();
}

// 显示剪纸传情文字
const showPaperCutLoveText = () => {
  console.log('显示剪纸传情文字');
  
  // 创建文字容器
  const textContainer = document.createElement('div');
  textContainer.id = 'paper-cut-love-text';
  textContainer.style.cssText = `
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 10000;
    color: white;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.8s ease-in-out;
  `;
  
  // 添加文字内容
  textContainer.innerHTML = `
    <h1 style="font-size: 48px; font-weight: bold; margin-bottom: 16px; color: #fff; text-shadow: 0 0 20px rgba(255, 68, 68, 0.8);">剪纸传情</h1>
    <p style="font-size: 24px; color: rgba(255, 255, 255, 0.9); max-width: 700px; line-height: 1.8;">在每一张红纸上，巧手剪出吉祥图案。剪纸传情，既是艺术，也承载着满族人对家人、亲友的祝福。</p>
  `;
  
  // 添加到页面
  document.body.appendChild(textContainer);
  
  // 淡入动画
  setTimeout(() => {
    textContainer.style.opacity = '1';
  }, 50);
  
  // 5-8秒后淡出并移除
  setTimeout(() => {
    textContainer.style.opacity = '0';
    setTimeout(() => {
      if (document.body.contains(textContainer)) {
        document.body.removeChild(textContainer);
      }
    }, 800);
  }, 6500); // 显示6.5秒
};

// 显示非遗传承文字
const showIntangibleHeritageText = () => {
  console.log('显示非遗传承文字');
  
  // 创建文字容器
  const textContainer = document.createElement('div');
  textContainer.id = 'intangible-heritage-text';
  textContainer.style.cssText = `
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 10000;
    color: white;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.8s ease-in-out;
  `;
  
  // 添加文字内容
  textContainer.innerHTML = `
    <h1 style="font-size: 48px; font-weight: bold; margin-bottom: 16px; color: #fff; text-shadow: 0 0 20px rgba(76, 175, 80, 0.8);">非遗传承</h1>
    <p style="font-size: 24px; color: rgba(255, 255, 255, 0.9); max-width: 700px; line-height: 1.8;">匠心传承百年，红纸剪刀间，书写民族文化的珍贵记忆。</p>
  `;
  
  // 添加到页面
  document.body.appendChild(textContainer);
  
  // 淡入动画
  setTimeout(() => {
    textContainer.style.opacity = '1';
  }, 50);
  
  // 5-8秒后淡出并移除
  setTimeout(() => {
    textContainer.style.opacity = '0';
    setTimeout(() => {
      if (document.body.contains(textContainer)) {
        document.body.removeChild(textContainer);
      }
    }, 800);
  }, 6500); // 显示6.5秒
};

// 黑屏过渡效果
const triggerBlackScreenTransition = () => {
  console.log('触发黑屏过渡效果');
  
  // 显示黑屏
  showBlackScreen.value = true;
  doorOpening.value = false;
  
  // 黑屏完全显示后，门开始打开
  setTimeout(() => {
    console.log('门开始打开');
    doorOpening.value = true;
    
    // 门完全打开后，隐藏黑屏并切换场景
    setTimeout(() => {
      console.log('切换到延伸场景');
      showBlackScreen.value = false;
      doorOpening.value = false;
      
      // 切换到延伸场景
      selectedWorkshop.value = 'paper-cutting-extended';
      changeWorkshop();
      
      // 场景切换完成后显示欢迎文字
      setTimeout(() => {
        console.log('显示欢迎文字');
        showWelcomeText.value = true;
        
        // 3秒后文字消失
        setTimeout(() => {
          console.log('文字消失');
          showWelcomeText.value = false;
        }, 3000);
      }, 500); // 等待场景切换完成
    }, 1500); // 门打开动画时长1.5秒
  }, 800); // 黑屏显示时长
}

const toggleSidebar = () => {
  sidebarCollapsed.value = !sidebarCollapsed.value
}

// 监听热点点击
const handleHotspotClick = (hotspotId) => {
  console.log('处理热点点击:', hotspotId);
  // 点击hotspot3（满族剪纸工坊的热点）时触发开始预览
  if (hotspotId === 'hotspot3') {
    console.log('调用startPreview函数');
    startPreview();
  }
}

// 创建图片查看器
const createImageViewer = (imageUrl) => {
  console.log('创建图片查看器，图片URL:', imageUrl);
  
  // 检查是否已经存在图片查看器
  let viewer = document.getElementById('image-viewer');
  if (viewer) {
    document.body.removeChild(viewer);
  }
  
  // 创建图片查看器元素
  viewer = document.createElement('div');
  viewer.id = 'image-viewer';
  viewer.style.position = 'fixed';
  viewer.style.top = '0';
  viewer.style.left = '0';
  viewer.style.width = '100vw';
  viewer.style.height = '100vh';
  viewer.style.backgroundColor = 'rgba(0, 0, 0, 0.9)';
  viewer.style.display = 'flex';
  viewer.style.justifyContent = 'center';
  viewer.style.alignItems = 'center';
  viewer.style.zIndex = '9999';
  viewer.style.cursor = 'pointer';
  
  // 创建图片元素
  const img = document.createElement('img');
  img.src = imageUrl;
  img.style.maxWidth = '90%';
  img.style.maxHeight = '90%';
  img.style.objectFit = 'contain';
  
  // 添加到查看器
  viewer.appendChild(img);
  
  // 点击查看器关闭
  viewer.addEventListener('click', () => {
    document.body.removeChild(viewer);
  });
  
  // 添加到文档
  document.body.appendChild(viewer);
  console.log('图片查看器创建成功');
}

// 打开拼图游戏
const openPuzzleGame = () => {
  console.log('打开拼图游戏');
  showPuzzleGame.value = true;
}

// 关闭拼图游戏
const closePuzzleGame = () => {
  console.log('关闭拼图游戏');
  showPuzzleGame.value = false;
}

// 模拟360°全景加载
onMounted(() => {
  // 初始化 Pannellum 全景
  initPannellum()
  // 初始化音频
  initAudio()
  
  // 监听 Pannellum 热点点击事件
  const clickHandler = (e) => {
    // 只有在第一个场景时才处理热点点击
    if (selectedWorkshop.value !== 'paper-cutting') {
      return; // 在延伸场景中不处理，让Pannellum原生事件绑定处理
    }
    
    console.log('第一个场景点击事件触发');
    // 检查是否点击了热点或热点的子元素
    let hotspotElement = e.target;
    while (hotspotElement) {
      if (hotspotElement.classList && hotspotElement.classList.contains('pnlm-hotspot')) {
        console.log('找到热点元素:', hotspotElement);
        console.log('热点元素属性:', hotspotElement.attributes);
        break;
      }
      hotspotElement = hotspotElement.parentElement;
    }
    
    if (hotspotElement) {
      const hotspotId = hotspotElement.getAttribute('data-hotspot-id');
      console.log('点击了热点:', hotspotId);
      
      // 获取热点文本
      let hotspotText = '';
      const spanElement = hotspotElement.querySelector('span');
      if (spanElement) {
        hotspotText = spanElement.textContent || spanElement.innerText || '';
      }
      console.log('热点文本:', hotspotText);
      
      // 根据热点文本执行不同操作
      if (hotspotText.includes('开始预览')) {
        console.log('在第一个场景，调用startPreview函数');
        startPreview();
      } else if (hotspotText.includes('剪纸传情')) {
        console.log('在第一个场景，调用showPaperCutLoveText函数');
        showPaperCutLoveText();
      } else if (hotspotText.includes('非遗传承')) {
        console.log('在第一个场景，调用showIntangibleHeritageText函数');
        showIntangibleHeritageText();
      } else {
        console.log('点击了其他热点，不执行任何操作');
      }
    }
  }
  
  window.addEventListener('click', clickHandler)
  
  // 保存事件监听器引用，以便在卸载时移除
  window.pannellumClickHandler = clickHandler
  
})

onUnmounted(() => {
  // 销毁 Pannellum 实例
  if (window.pannellumInstance) {
    window.pannellumInstance.destroy()
  }
  
  // 停止并清理音频
  if (audioElement.value) {
    audioElement.value.pause()
    audioElement.value = null
  }
  
  // 移除事件监听器
  if (window.pannellumClickHandler) {
    window.removeEventListener('click', window.pannellumClickHandler)
  }
})
</script>

<style scoped>
/* 全局样式 */
.cloud-workshop {
  position: relative;
  height: 100vh;
  overflow: hidden;
  background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #1a1a1a 100%);
}

/* 背景装饰元素 */
.cloud-workshop::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 30%, rgba(76, 175, 80, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(76, 175, 80, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 40% 80%, rgba(76, 175, 80, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 70% 20%, rgba(76, 175, 80, 0.08) 0%, transparent 50%);
  z-index: 0;
}

/* 纹理覆盖 */
.cloud-workshop::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><rect width="100" height="100" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/></svg>');
  z-index: 0;
  pointer-events: none;
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

.audio-btn:hover {
  background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(76, 175, 80, 0.1));
  border-color: rgba(76, 175, 80, 0.3);
}

.workshop-selector {
  position: relative;
}

.workshop-selector select {
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

.workshop-selector select:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.1));
  border-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
}

.workshop-selector select:focus {
  outline: none;
  border-color: #4CAF50;
  box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.2);
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
  background-size: cover;
  background-position: center;
  border-radius: 0;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

/* 全景视图装饰边框 */
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

/* 全景视图渐变遮罩 */
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
  animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translate(-50%, -50%) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
}

/* 热点 */
.hotspot {
  position: absolute;
  width: 48px;
  height: 48px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
}

.hotspot-1 {
  top: 40%;
  left: 30%;
}

.hotspot-2 {
  top: 60%;
  left: 70%;
}

.hotspot-3 {
  top: 50%;
  left: 50%;
}

.hotspot-icon {
  font-size: 24px;
  color: #4CAF50;
  animation: pulse 2s infinite;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 20px rgba(76, 175, 80, 0.6);
}

.hotspot::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  border: 2px solid rgba(76, 175, 80, 0.6);
  border-radius: 50%;
  animation: pulse-ring 2s infinite;
}

/* 预览热点样式 */
.preview-hotspot {
  /* Pannellum热点样式 */
}

/* 自定义热点按钮样式 */
.pnlm-hotspot.preview-hotspot {
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  color: white;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 120px;
  height: auto;
}

.pnlm-hotspot.preview-hotspot:hover {
  background: linear-gradient(135deg, #45a049, #7cb342);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(76, 175, 80, 0.4);
}

.pnlm-hotspot.preview-hotspot .pnlm-hotspot-text {
  color: white !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  text-shadow: none !important;
  margin: 0 !important;
  padding: 0 !important;
}

@keyframes pulse {
  0% {
    transform: scale(1);
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.6);
  }
  50% {
    transform: scale(1.1);
    box-shadow: 0 0 30px rgba(76, 175, 80, 0.8);
  }
  100% {
    transform: scale(1);
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.6);
  }
}

@keyframes pulse-ring {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  100% {
    transform: scale(2);
    opacity: 0;
  }
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

/* 门打开效果 - 从中间向两边慢慢打开 */
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
  text-shadow: 0 0 20px rgba(76, 175, 80, 0.8);
}

.welcome-text p {
  font-size: 24px;
  color: rgba(255, 255, 255, 0.9);
}

/* 欢迎文字淡入淡出动画 */
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
  border: 1px solid rgba(76, 175, 80, 0.2);
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
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.hotspot-card h3 {
  margin-top: 0;
  margin-bottom: 20px;
  color: #4CAF50;
  font-family: 'Microsoft YaHei', sans-serif;
  font-size: 22px;
  font-weight: 600;
  border-bottom: 2px solid rgba(76, 175, 80, 0.2);
  padding-bottom: 10px;
}

.hotspot-card p {
  margin-bottom: 20px;
  line-height: 1.6;
  color: #333;
  font-size: 16px;
}

.artist-info {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid rgba(76, 175, 80, 0.2);
}

.artist-info h4 {
  margin-top: 0;
  margin-bottom: 12px;
  font-size: 16px;
  color: #4CAF50;
  font-weight: 600;
}

.artist-info p {
  margin-bottom: 0;
  font-size: 14px;
  color: #555;
  line-height: 1.5;
}

/* 预览按钮 */
.preview-btn {
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
  color: white;
  border: none;
  padding: 14px 28px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
  font-size: 16px;
  margin-top: 24px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.preview-btn:hover {
  background: linear-gradient(135deg, #45a049, #7cb342);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(76, 175, 80, 0.4);
}

.preview-btn:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
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
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
  color: white;
  border: none;
  padding: 14px 28px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
  font-size: 16px;
}

.book-btn:hover {
  background: linear-gradient(135deg, #45a049, #7cb342);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(76, 175, 80, 0.4);
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
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
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
  box-shadow: -2px 0 10px rgba(76, 175, 80, 0.3);
}

.toggle-sidebar:hover {
  background: linear-gradient(135deg, #45a049, #7cb342);
  transform: translateY(-50%) scale(1.05);
  box-shadow: -4px 0 15px rgba(76, 175, 80, 0.4);
}

.sidebar-content {
  padding: 24px;
  height: 100%;
  overflow-y: auto;
}

.sidebar-content h3 {
  margin-top: 0;
  margin-bottom: 16px;
  color: #4CAF50;
  font-family: 'Microsoft YaHei', sans-serif;
  font-size: 18px;
  border-bottom: 2px solid rgba(76, 175, 80, 0.3);
  padding-bottom: 8px;
}

.sidebar-content p {
  margin-bottom: 24px;
  line-height: 1.6;
  opacity: 0.85;
  font-size: 14px;
}

.artist-profile {
  margin-bottom: 32px;
  text-align: center;
}

.artist-profile img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 16px;
  border: 3px solid rgba(76, 175, 80, 0.5);
  transition: transform 0.3s ease;
}

.artist-profile img:hover {
  transform: scale(1.05);
  border-color: #4CAF50;
  box-shadow: 0 0 20px rgba(76, 175, 80, 0.5);
}

.artist-profile h4 {
  margin: 0 0 8px 0;
  font-size: 16px;
  color: #4CAF50;
}

.recommendations {
  margin-top: 32px;
}

.recommendation-item {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 16px;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.recommendation-item:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.1));
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
  border-color: rgba(76, 175, 80, 0.3);
}

.recommendation-item h4 {
  margin: 0 0 8px 0;
  font-size: 16px;
  color: #4CAF50;
}

.recommendation-item p {
  margin: 0 0 16px 0;
  font-size: 14px;
  opacity: 0.8;
  line-height: 1.5;
}

.recommendation-item .btn-sm {
  font-size: 14px;
  padding: 8px 20px;
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.recommendation-item .btn-sm:hover {
  background: linear-gradient(135deg, #45a049, #7cb342);
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(76, 175, 80, 0.3);
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
  
  .back-btn,
  .share-btn,
  .audio-btn {
    padding: 8px 16px;
    font-size: 14px;
  }
  
  .audio-control {
    margin-right: 8px;
  }
  
  .audio-btn {
    font-size: 12px;
    padding: 8px 12px;
  }
  
  .workshop-selector {
    order: 3;
    width: 100%;
    margin-top: 8px;
  }
  
  .workshop-selector select {
    width: 100%;
    padding: 10px 20px;
    font-size: 14px;
  }
  
  .footer-content {
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
  }
  
  .control-btn,
  .fullscreen-btn {
    padding: 8px 16px;
    font-size: 12px;
  }
  
  .book-btn {
    padding: 12px 24px;
    font-size: 14px;
  }
  
  .sidebar {
    width: 280px;
  }
  
  .sidebar.collapsed {
    transform: translateX(230px);
  }
  
  .toggle-sidebar {
    left: -50px;
    padding: 12px 8px;
    font-size: 12px;
  }
  
  .sidebar-content {
    padding: 16px;
  }
  
  .artist-profile img {
    width: 80px;
    height: 80px;
  }
  
  .recommendation-item {
    padding: 16px;
  }
  
  .recommendation-item .btn-sm {
    padding: 6px 16px;
    font-size: 12px;
  }
}
</style>