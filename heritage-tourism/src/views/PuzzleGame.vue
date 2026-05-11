<template>
  <div v-if="visible" class="puzzle-modal">
    <div class="modal-content">
      <button class="close-modal" @click="close">&times;</button>
      <h3>剪纸拼图小游戏</h3>
      <div class="puzzle-container">
        <div class="puzzle-board">
          <div 
            v-for="(piece, index) in puzzlePieces" 
            :key="index"
            class="puzzle-piece"
            :class="{ 'correct': piece.correct }"
            @click="selectPiece(index)"
            :style="{
              backgroundImage: `url('/src/assets/pintu/${piece.value}.png')`,
              left: piece.x + 'px',
              top: piece.y + 'px'
            }"
          ></div>
        </div>
        <div class="puzzle-preview">
          <img src="/src/assets/pintu/all.png" alt="完整剪纸" />
          <p>参考图片</p>
        </div>
      </div>
      <div class="puzzle-stats">
        <p>步数: {{ moveCount }}</p>
        <p>时间: {{ timeElapsed }}秒</p>
      </div>
      <div class="puzzle-controls">
        <button class="btn btn-primary" @click="resetPuzzle">重新开始</button>
        <button class="btn btn-secondary" @click="close">关闭</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// 组件参数
const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  }
})

// 组件事件
const emit = defineEmits(['close'])

// 拼图游戏相关
const puzzlePieces = ref([])
const moveCount = ref(0)
const timeElapsed = ref(0)
const timer = ref(null)
const selectedPiece = ref(null)

// 初始化拼图
const initPuzzle = () => {
  // 初始化拼图块
  const pieces = []
  const positions = [
    { x: 0, y: 0 },
    { x: 100, y: 0 },
    { x: 200, y: 0 },
    { x: 0, y: 100 },
    { x: 100, y: 100 },
    { x: 200, y: 100 },
    { x: 0, y: 200 },
    { x: 100, y: 200 },
    { x: 200, y: 200 }
  ]
  
  // 创建拼图块数据
  for (let i = 1; i <= 9; i++) {
    pieces.push({
      value: i,
      correctValue: i,
      x: positions[i-1].x,
      y: positions[i-1].y,
      correct: true
    })
  }
  
  // 打乱拼图
  shufflePuzzle(pieces)
  puzzlePieces.value = pieces
  moveCount.value = 0
  timeElapsed.value = 0
  
  // 开始计时
  startTimer()
}

// 打乱拼图
const shufflePuzzle = (pieces) => {
  for (let i = pieces.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[pieces[i].value, pieces[j].value] = [pieces[j].value, pieces[i].value]
    pieces[i].correct = pieces[i].value === pieces[i].correctValue
    pieces[j].correct = pieces[j].value === pieces[j].correctValue
  }
}

// 开始计时
const startTimer = () => {
  if (timer.value) {
    clearInterval(timer.value)
  }
  timer.value = setInterval(() => {
    timeElapsed.value++
  }, 1000)
}

// 停止计时
const stopTimer = () => {
  if (timer.value) {
    clearInterval(timer.value)
    timer.value = null
  }
}

// 选择拼图块
const selectPiece = (index) => {
  if (selectedPiece.value === null) {
    // 选择第一个块
    selectedPiece.value = index
  } else {
    // 交换两个块
    if (selectedPiece.value !== index) {
      ;[puzzlePieces.value[selectedPiece.value].value, puzzlePieces.value[index].value] = 
        [puzzlePieces.value[index].value, puzzlePieces.value[selectedPiece.value].value]
      
      // 更新正确状态
      puzzlePieces.value[selectedPiece.value].correct = 
        puzzlePieces.value[selectedPiece.value].value === puzzlePieces.value[selectedPiece.value].correctValue
      puzzlePieces.value[index].correct = 
        puzzlePieces.value[index].value === puzzlePieces.value[index].correctValue
      
      moveCount.value++
      
      // 检查是否完成
      checkPuzzleComplete()
    }
    selectedPiece.value = null
  }
}

// 检查拼图是否完成
const checkPuzzleComplete = () => {
  const allCorrect = puzzlePieces.value.every(piece => piece.correct)
  if (allCorrect) {
    stopTimer()
    setTimeout(() => {
      alert('恭喜你完成了拼图！\n步数：' + moveCount.value + '\n时间：' + timeElapsed.value + '秒')
    }, 500)
  }
}

// 关闭拼图游戏
const close = () => {
  stopTimer()
  emit('close')
}

// 重置拼图
const resetPuzzle = () => {
  initPuzzle()
}

// 组件挂载时初始化
onMounted(() => {
  if (props.visible) {
    initPuzzle()
  }
})

// 组件卸载时清理
onUnmounted(() => {
  stopTimer()
})
</script>

<style scoped>
/* 拼图游戏样式 */
.puzzle-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
  backdrop-filter: blur(10px);
}

.puzzle-modal .modal-content {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.9));
  padding: 30px;
  border-radius: 16px;
  width: 90%;
  max-width: 700px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
  z-index: 2001;
  border: 1px solid rgba(76, 175, 80, 0.2);
  animation: slideIn 0.3s ease-out;
  text-align: center;
}

.puzzle-modal .close-modal {
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

.puzzle-modal .close-modal:hover {
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.1));
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.puzzle-modal h3 {
  margin-top: 0;
  margin-bottom: 24px;
  color: #4CAF50;
  font-family: 'Microsoft YaHei', sans-serif;
  font-size: 24px;
  font-weight: 600;
}

.puzzle-container {
  display: flex;
  gap: 30px;
  margin-bottom: 24px;
  justify-content: center;
  align-items: flex-start;
}

.puzzle-board {
  position: relative;
  width: 300px;
  height: 300px;
  border: 2px solid #4CAF50;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.puzzle-piece {
  position: absolute;
  width: 100px;
  height: 100px;
  background-size: cover;
  background-position: center;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 4px;
}

.puzzle-piece:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
  z-index: 10;
}

.puzzle-piece.correct {
  box-shadow: 0 0 15px rgba(76, 175, 80, 0.6);
  border-color: #4CAF50;
}

.puzzle-preview {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.puzzle-preview img {
  width: 150px;
  height: 150px;
  border: 2px solid #4CAF50;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  margin-bottom: 12px;
}

.puzzle-preview p {
  margin: 0;
  font-size: 14px;
  color: #666;
  font-weight: 500;
}

.puzzle-stats {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-bottom: 24px;
  padding: 16px;
  background: linear-gradient(135deg, rgba(76, 175, 80, 0.1), rgba(76, 175, 80, 0.05));
  border-radius: 8px;
}

.puzzle-stats p {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  color: #333;
}

.puzzle-controls {
  display: flex;
  gap: 16px;
  justify-content: center;
}

.puzzle-controls .btn {
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.puzzle-controls .btn-primary {
  background: linear-gradient(135deg, #4CAF50, #8BC34A);
  color: white;
  border: none;
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
}

.puzzle-controls .btn-primary:hover {
  background: linear-gradient(135deg, #45a049, #7cb342);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(76, 175, 80, 0.4);
}

.puzzle-controls .btn-secondary {
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.05));
  color: #333;
  border: 1px solid rgba(0, 0, 0, 0.2);
}

.puzzle-controls .btn-secondary:hover {
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.1));
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .puzzle-container {
    flex-direction: column;
    align-items: center;
  }
  
  .puzzle-board {
    width: 270px;
    height: 270px;
  }
  
  .puzzle-piece {
    width: 90px;
    height: 90px;
  }
  
  .puzzle-piece {
    left: calc(var(--x) * 90px);
    top: calc(var(--y) * 90px);
  }
  
  .puzzle-preview img {
    width: 120px;
    height: 120px;
  }
  
  .puzzle-controls {
    flex-direction: column;
    align-items: center;
  }
  
  .puzzle-controls .btn {
    width: 100%;
    max-width: 200px;
  }
}

/* 动画 */
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
</style>