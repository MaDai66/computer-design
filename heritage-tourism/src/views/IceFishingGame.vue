<template>
  <!-- 模态框形式的游戏 -->
  <div v-if="visible" class="ice-fishing-modal">
    <div class="modal-overlay" @click="close"></div>
    <div class="modal-content">
      <button class="close-modal" @click="close">&times;</button>
      <h3>🎣 冰下奇遇</h3>
      <p class="game-desc">点击屏幕下钩捕鱼！</p>
      
      <div class="game-container" @click="handleClick" ref="gameCanvas">
        <!-- 冰面 -->
        <div class="ice-surface"></div>
        
        <!-- 鱼钩 -->
        <div 
          class="hook" 
          :class="{ 'dropping': isDropping, 'firing': isFiring }"
          :style="{ left: hookX + 'px', top: hookY + 'px' }"
        >
          <div class="hook-line"></div>
          <div class="hook-point"></div>
        </div>
        
        <!-- 鱼 -->
        <div 
          v-for="fish in fishes" 
          :key="fish.id"
          class="fish"
          :class="{ 'caught': fish.caught, 'flying': fish.flying }"
          :style="{ left: fish.x + 'px', top: fish.y + 'px' }"
        >
          <div class="fish-body"></div>
          <div class="fish-tail"></div>
        </div>
        
        <!-- 石头 -->
        <div 
          v-for="rock in rocks" 
          :key="rock.id"
          class="rock"
          :style="{ left: rock.x + 'px', top: rock.y + 'px' }"
        ></div>
        
        <!-- 得分弹出 -->
        <div 
          v-for="popup in scorePopups" 
          :key="popup.id"
          class="score-popup"
          :style="{ left: popup.x + 'px', top: popup.y + 'px' }"
        >
          +{{ popup.score }}kg
        </div>
      </div>
      
      <div class="game-stats">
        <div class="stat">
          <span class="stat-label">重量</span>
          <span class="stat-value">{{ score }}kg</span>
        </div>
        <div class="stat">
          <span class="stat-label">时间</span>
          <span class="stat-value">{{ timeLeft }}s</span>
        </div>
        <div class="stat" v-if="combo >= 3">
          <span class="stat-label">连击</span>
          <span class="stat-value combo">🔥 {{ combo }}x</span>
        </div>
      </div>
      
      <div class="game-controls">
        <button class="btn btn-primary" @click="startGame" v-if="!gameStarted">开始游戏</button>
        <button class="btn btn-secondary" @click="restartGame" v-if="gameStarted">重新开始</button>
      </div>
      
      <!-- 游戏结束弹窗 -->
      <div v-if="gameOver" class="game-over-overlay">
        <div class="game-over-content">
          <h3>🎉 游戏结束</h3>
          <p>最终重量：{{ score }}kg</p>
          <button class="btn btn-primary" @click="restartGame">再来一次</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

// 组件参数
const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})

// 组件事件
const emit = defineEmits(['close'])

// 游戏状态
const score = ref(0)
const timeLeft = ref(60)
const combo = ref(0)
const isFiring = ref(false)
const isDropping = ref(false)
const gameStarted = ref(false)
const gameOver = ref(false)
const gameCanvas = ref(null)

// 鱼钩位置
const hookX = ref(150)
const hookY = ref(30)
const hookSpeed = ref(3)
const dropSpeed = ref(8)

// 鱼和石头
const fishes = ref([])
const rocks = ref([])
const scorePopups = ref([])

// 定时器
let gameTimer = null
let animationTimer = null
let popupId = 0

// 初始化鱼
const initFishes = () => {
  fishes.value = [
    { id: 1, x: 80, y: 120, caught: false, flying: false, direction: 1 },
    { id: 2, x: 180, y: 160, caught: false, flying: false, direction: -1 },
    { id: 3, x: 120, y: 200, caught: false, flying: false, direction: 1 },
    { id: 4, x: 220, y: 140, caught: false, flying: false, direction: -1 },
  ]
}

// 初始化石头
const initRocks = () => {
  rocks.value = [
    { id: 1, x: 100, y: 250 },
    { id: 2, x: 200, y: 280 },
  ]
}

// 开始游戏
const startGame = () => {
  gameStarted.value = true
  gameOver.value = false
  score.value = 0
  timeLeft.value = 60
  combo.value = 0
  isFiring.value = false
  hookX.value = 150
  hookY.value = 30
  initFishes()
  initRocks()
  
  // 开始计时
  gameTimer = setInterval(() => {
    timeLeft.value--
    if (timeLeft.value <= 0) {
      endGame()
    }
  }, 1000)
  
  // 开始动画循环
  startAnimation()
}

// 动画循环
const startAnimation = () => {
  const animate = () => {
    // 鱼钩左右移动
    if (!isDropping.value) {
      hookX.value += hookSpeed.value
      if (hookX.value >= 280 || hookX.value <= 20) {
        hookSpeed.value = -hookSpeed.value
      }
    }
    
    // 鱼钩下落
    if (isDropping.value) {
      hookY.value += dropSpeed.value
      checkCollision()
    }
    
    // 鱼游动
    fishes.value.forEach(fish => {
      if (!fish.caught && !fish.flying) {
        fish.x += fish.direction * 1.5
        if (fish.x >= 280 || fish.x <= 20) {
          fish.direction = -fish.direction
        }
      }
      
      if (fish.flying) {
        fish.y -= 5
        if (fish.y < -50) {
          fish.caught = false
          fish.flying = false
          fish.y = 120 + Math.random() * 80
          fish.x = 20 + Math.random() * 260
        }
      }
    })
    
    animationTimer = requestAnimationFrame(animate)
  }
  
  animate()
}

// 碰撞检测
const checkCollision = () => {
  const hookCenterX = hookX.value + 10
  const hookCenterY = hookY.value + 20
  
  // 检测鱼
  fishes.value.forEach(fish => {
    if (!fish.caught && !fish.flying) {
      const fishCenterX = fish.x + 20
      const fishCenterY = fish.y + 15
      
      if (Math.abs(hookCenterX - fishCenterX) < 25 &&
          Math.abs(hookCenterY - fishCenterY) < 20) {
        fish.flying = true
        combo.value++
        const points = isFiring.value ? 2 : 1
        score.value += points
        
        showScorePopup(hookCenterX, hookCenterY, points)
        
        if (combo.value >= 3 && !isFiring.value) {
          isFiring.value = true
          setTimeout(() => {
            isFiring.value = false
          }, 5000)
        }
        
        resetHook()
      }
    }
  })
  
  // 检测石头
  rocks.value.forEach(rock => {
    const rockCenterX = rock.x + 15
    const rockCenterY = rock.y + 15
    
    if (Math.abs(hookCenterX - rockCenterX) < 20 &&
        Math.abs(hookCenterY - rockCenterY) < 20) {
      combo.value = 0
      timeLeft.value = Math.max(0, timeLeft.value - 3)
      resetHook()
      
      if (gameCanvas.value) {
        gameCanvas.value.style.animation = 'shake 0.3s'
        setTimeout(() => {
          gameCanvas.value.style.animation = ''
        }, 300)
      }
    }
  })
  
  if (hookY.value > 320) {
    resetHook()
  }
}

// 显示得分弹出
const showScorePopup = (x, y, points) => {
  const id = popupId++
  scorePopups.value.push({ id, x, y, score: points })
  setTimeout(() => {
    scorePopups.value = scorePopups.value.filter(p => p.id !== id)
  }, 1000)
}

// 重置鱼钩
const resetHook = () => {
  isDropping.value = false
  hookY.value = 30
}

// 点击处理
const handleClick = () => {
  if (!gameStarted.value || gameOver.value || isDropping.value) return
  isDropping.value = true
}

// 结束游戏
const endGame = () => {
  gameOver.value = true
  clearInterval(gameTimer)
  if (animationTimer) {
    cancelAnimationFrame(animationTimer)
  }
}

// 重新开始
const restartGame = () => {
  startGame()
}

// 关闭游戏
const close = () => {
  stopGame()
  emit('close')
}

// 停止游戏
const stopGame = () => {
  gameStarted.value = false
  gameOver.value = false
  score.value = 0
  timeLeft.value = 60
  combo.value = 0
  isFiring.value = false
  hookX.value = 150
  hookY.value = 30
  clearInterval(gameTimer)
  if (animationTimer) {
    cancelAnimationFrame(animationTimer)
  }
}

// 监听visible变化
watch(() => props.visible, (newVal) => {
  if (!newVal) {
    stopGame()
  }
})

onMounted(() => {
  initFishes()
  initRocks()
})

onUnmounted(() => {
  clearInterval(gameTimer)
  if (animationTimer) {
    cancelAnimationFrame(animationTimer)
  }
})
</script>

<style scoped>
.ice-fishing-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 2000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(5px);
}

.modal-content {
  position: relative;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.9));
  padding: 30px;
  border-radius: 16px;
  max-width: 400px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.close-modal {
  position: absolute;
  top: 16px;
  right: 16px;
  background: rgba(0, 0, 0, 0.1);
  border: none;
  font-size: 24px;
  cursor: pointer;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}

.close-modal:hover {
  background: rgba(0, 0, 0, 0.2);
  transform: scale(1.1);
}

.modal-content h3 {
  margin: 0 0 8px 0;
  font-size: 24px;
  text-align: center;
  color: #4CAF50;
}

.game-desc {
  margin: 0 0 16px 0;
  font-size: 14px;
  text-align: center;
  color: #666;
}

.game-container {
  position: relative;
  width: 100%;
  height: 350px;
  background: linear-gradient(to bottom, #87CEEB 0%, #00BFFF 30%, #1E90FF 100%);
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  margin-bottom: 16px;
}

.ice-surface {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0.9), rgba(200, 230, 255, 0.7));
  border-bottom: 3px solid rgba(150, 200, 255, 0.5);
}

.hook {
  position: absolute;
  width: 20px;
  height: 30px;
  transition: transform 0.2s;
}

.hook.firing {
  filter: drop-shadow(0 0 10px #ff6347);
}

.hook-line {
  position: absolute;
  top: -30px;
  left: 9px;
  width: 2px;
  height: 30px;
  background: #666;
}

.hook-point {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 20px;
  height: 20px;
  border: 3px solid #8B4513;
  border-radius: 50% 50% 50% 0;
  border-right: none;
  transform: rotate(-45deg);
}

.fish {
  position: absolute;
  width: 40px;
  height: 30px;
  transition: transform 0.3s;
}

.fish.caught {
  opacity: 0;
}

.fish.flying {
  animation: flyUp 0.5s ease-out;
}

.fish-body {
  position: absolute;
  width: 30px;
  height: 15px;
  background: linear-gradient(135deg, #FF6347, #FF4500);
  border-radius: 50%;
}

.fish-tail {
  position: absolute;
  right: -10px;
  top: 5px;
  width: 0;
  height: 0;
  border-left: 10px solid #FF6347;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
}

.rock {
  position: absolute;
  width: 30px;
  height: 25px;
  background: linear-gradient(135deg, #696969, #4A4A4A);
  border-radius: 50% 50% 45% 45%;
}

.score-popup {
  position: absolute;
  font-size: 18px;
  font-weight: bold;
  color: #FFD700;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  animation: floatUp 1s ease-out forwards;
  pointer-events: none;
}

@keyframes floatUp {
  0% {
    opacity: 1;
    transform: translateY(0);
  }
  100% {
    opacity: 0;
    transform: translateY(-50px);
  }
}

@keyframes flyUp {
  0% {
    transform: translateY(0) rotate(0deg);
  }
  100% {
    transform: translateY(-50px) rotate(360deg);
  }
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}

.game-stats {
  display: flex;
  justify-content: space-around;
  margin-bottom: 16px;
  padding: 12px;
  background: rgba(76, 175, 80, 0.1);
  border-radius: 8px;
}

.stat {
  text-align: center;
}

.stat-label {
  display: block;
  font-size: 12px;
  color: #666;
  margin-bottom: 4px;
}

.stat-value {
  font-size: 18px;
  font-weight: bold;
  color: #4CAF50;
}

.stat-value.combo {
  color: #ff6347;
}

.game-controls {
  display: flex;
  gap: 12px;
}

.game-controls .btn {
  flex: 1;
  padding: 12px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
}

.btn-primary {
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
}

.btn-secondary {
  background: rgba(0, 0, 0, 0.1);
  color: #333;
  border: 1px solid rgba(0, 0, 0, 0.2);
}

.btn-secondary:hover {
  background: rgba(0, 0, 0, 0.2);
}

.game-over-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 16px;
}

.game-over-content {
  text-align: center;
  padding: 30px;
}

.game-over-content h3 {
  margin: 0 0 16px 0;
  font-size: 28px;
  color: #FFD700;
}

.game-over-content p {
  margin: 0 0 20px 0;
  font-size: 18px;
  color: white;
}
</style>