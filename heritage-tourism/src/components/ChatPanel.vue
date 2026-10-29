<template>
  <Transition name="slide-right">
    <div v-if="visible" class="chat-overlay" @click.self="$emit('close')">
      <div class="chat-panel">
        <div class="chat-header">
          <div class="header-decoration-top"></div>
          <div class="header-decoration-bottom"></div>
          <div class="header-left">
            <div class="avatar">
              <img src="/aji.png" alt="阿吉" class="avatar-img" />
            </div>
            <div class="header-info">
              <h3>吉韵遗风 AI 助手</h3>
              <div class="online-status">
                <span class="status-dot"></span>
                <span class="status-text">在线</span>
              </div>
            </div>
          </div>
          <div class="header-right">
            <button class="menu-btn" @click="showMenu = !showMenu">
              <svg viewBox="0 0 24 24" fill="none" stroke="#C28B4E" stroke-width="2">
                <line x1="3" y1="12" x2="21" y2="12"/>
                <line x1="3" y1="6" x2="21" y2="6"/>
                <line x1="3" y1="18" x2="21" y2="18"/>
              </svg>
            </button>
            <button class="close-btn" @click="$emit('close')">
              <svg viewBox="0 0 24 24" fill="none" stroke="#C28B4E" stroke-width="2">
                <line x1="18" y1="6" x2="6" y2="18"/>
                <line x1="6" y1="6" x2="18" y2="18"/>
              </svg>
            </button>
          </div>
        </div>
        
        <div v-if="showMenu" class="menu-dropdown">
          <button class="menu-item" @click="clearMessages">
            <svg viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2">
              <path d="M3 6h18"/>
              <path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/>
              <path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/>
            </svg>
            <span>清空对话</span>
          </button>
        </div>
        
        <div class="chat-messages" ref="messagesContainer">
          <div class="watermark">吉</div>
          <div 
            v-for="(msg, index) in messages" 
            :key="index" 
            class="message-item"
            :class="{ 'user': msg.isUser, 'bot': !msg.isUser }"
          >
            <div class="message-avatar">
              <svg 
                v-if="msg.isUser"
                viewBox="0 0 24 24" 
                fill="none" 
                stroke="#9C2F2F" 
                stroke-width="2"
              >
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="12" cy="7" r="4" />
              </svg>
              <img 
                v-else
                src="/aji.png" 
                alt="阿吉" 
                class="msg-avatar-img" 
              />
            </div>
            <div class="message-content">
              <MarkdownRenderer v-if="!msg.isUser" :content="displayMessages[index] || msg.content" />
              <p v-else>{{ msg.content }}</p>
            </div>
          </div>
          
          <div v-if="isLoading" class="loading-indicator">
            <div class="loading-dots">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
        
        <div class="quick-actions">
          <button 
            v-for="action in quickActions" 
            :key="action.key"
            class="action-btn"
            @click="handleQuickAction(action.key)"
          >
            <span class="action-icon">{{ action.icon }}</span>
            <span class="action-text">{{ action.label }}</span>
          </button>
        </div>
        
        <div class="chat-input">
          <input 
            v-model="inputMessage"
            :disabled="isLoading"
            placeholder="请问有什么可以帮助您的？"
            @keyup.enter="sendMessage"
            class="chat-input-field"
          />
          <button 
            class="send-btn" 
            @click="sendMessage"
            :disabled="!inputMessage.trim() || isLoading"
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
              <path d="M12 19V5M18 12l-6-6-6 6" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, nextTick, watch, onMounted } from 'vue'
import MarkdownRenderer from './MarkdownRenderer.vue'

const props = defineProps({
  visible: Boolean
})

defineEmits(['close'])

const API_BASE_URL = import.meta.env.VITE_CHAT_API_BASE_URL || 'http://localhost:3000'

const inputMessage = ref('')
const messages = ref([])
const displayMessages = ref([])
const isLoading = ref(false)
const showMenu = ref(false)
const messagesContainer = ref(null)

const quickActions = [
  { key: 'changbaishan', label: '长白山路线', icon: '🗻' },
  { key: 'northeast', label: '东北非遗', icon: '🎭' },
  { key: 'chaoxianzu', label: '朝鲜族体验', icon: '🥁' },
  { key: 'winter', label: '冬季旅游推荐', icon: '❄️' }
]

const welcomeMessage = `您好，我是阿吉～

可以帮您：
🎭 推荐非遗体验
🗺️ 规划东北路线
🏨 推荐特色民宿
🛍️ 查找文创商品`

const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

watch(() => messages.value.length, scrollToBottom)

onMounted(() => {
  if (props.visible && messages.value.length === 0) {
    messages.value.push({ content: welcomeMessage, isUser: false })
    displayMessages.value.push(welcomeMessage)
  }
})

watch(() => props.visible, (newVal) => {
  if (newVal && messages.value.length === 0) {
    messages.value.push({ content: welcomeMessage, isUser: false })
    displayMessages.value.push(welcomeMessage)
  }
})

const typeWriterEffect = async (content, index) => {
  displayMessages.value[index] = ''
  for (let i = 0; i <= content.length; i++) {
    displayMessages.value[index] = content.slice(0, i)
    scrollToBottom()
    await new Promise(resolve => setTimeout(resolve, 30))
  }
}

const sendMessage = async () => {
  const content = inputMessage.value.trim()
  if (!content || isLoading.value) return
  
  messages.value.push({ content, isUser: true })
  displayMessages.value.push(content)
  inputMessage.value = ''
  isLoading.value = true
  
  try {
    const response = await fetch(`${API_BASE_URL}/api/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        messages: messages.value.map(msg => ({
          role: msg.isUser ? 'user' : 'assistant',
          content: msg.content
        }))
      })
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const reader = response.body?.getReader()
    if (!reader) {
      throw new Error('No response body')
    }
    
    const decoder = new TextDecoder('utf-8')
    let botResponse = ''
    const botMessageId = messages.value.length
    
    messages.value.push({ content: '', isUser: false })
    displayMessages.value.push('')
    
    while (true) {
      const { done, value } = await reader.read()
      
      if (done) break
      
      const chunk = decoder.decode(value)
      const lines = chunk.split('\n')
      
      for (const line of lines) {
        if (line.startsWith('data: ')) {
          try {
            const data = JSON.parse(line.slice(6))
            if (data.content) {
              botResponse += data.content
              messages.value[botMessageId].content = botResponse
              displayMessages.value[botMessageId] = botResponse
              scrollToBottom()
            }
          } catch {
            continue
          }
        }
      }
    }
    
    if (!botResponse) {
      messages.value[botMessageId].content = '抱歉，我无法回答您的问题。'
      displayMessages.value[botMessageId] = '抱歉，我无法回答您的问题。'
    }
  } catch (error) {
    console.error('API call error:', error)
    const fallbackResponses = [
      '哎呀，网络开小差了，让我想想...',
      '抱歉，连接有点问题，我来直接为您解答吧～',
      '网络不太稳定呢，我先为您提供一些信息参考'
    ]
    const randomResponse = fallbackResponses[Math.floor(Math.random() * fallbackResponses.length)]
    messages.value.push({ 
      content: randomResponse, 
      isUser: false 
    })
    displayMessages.value.push(randomResponse)
  } finally {
    isLoading.value = false
  }
}

const handleQuickAction = (actionKey) => {
  const prompts = {
    changbaishan: '推荐长白山旅游路线',
    northeast: '介绍东北非遗文化',
    chaoxianzu: '推荐朝鲜族文化体验',
    winter: '推荐东北冬季旅游'
  }
  inputMessage.value = prompts[actionKey] || ''
}

const clearMessages = () => {
  messages.value = [{ content: welcomeMessage, isUser: false }]
  displayMessages.value = [welcomeMessage]
  showMenu.value = false
}
</script>

<style scoped>
.chat-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(44, 92, 77, 0.2);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  display: flex;
  justify-content: flex-end;
  z-index: 9998;
}

.chat-panel {
  width: 100%;
  max-width: 420px;
  height: 100%;
  background: rgba(250, 246, 235, 0.98);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  display: flex;
  flex-direction: column;
  box-shadow: -8px 0 40px rgba(156, 47, 47, 0.15);
  position: relative;
  border-radius: 24px 0 0 24px;
  overflow: hidden;
}

.chat-header {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px;
  background: linear-gradient(135deg, rgba(250, 246, 235, 0.98) 0%, rgba(232, 213, 184, 0.4) 100%);
  border-bottom: 1px solid rgba(194, 139, 78, 0.15);
}

.header-decoration-top {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #9C2F2F 0%, #C28B4E 30%, #FFD700 50%, #C28B4E 70%, #9C2F2F 100%);
  border-radius: 2px 2px 0 0;
}

.header-decoration-bottom {
  position: absolute;
  bottom: -2px;
  left: 20%;
  right: 20%;
  height: 3px;
  background: linear-gradient(90deg, transparent 0%, rgba(194, 139, 78, 0.3) 50%, transparent 100%);
  border-radius: 0 0 2px 2px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 14px;
}

.avatar {
  width: 52px;
  height: 52px;
  background: linear-gradient(135deg, #FAF6EB 0%, #E8D5B8 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 3px solid rgba(194, 139, 78, 0.3);
  box-shadow: 0 4px 12px rgba(194, 139, 78, 0.2), inset 0 0 10px rgba(255, 215, 0, 0.1);
  position: relative;
}

.avatar::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 50%;
  border: 1px solid rgba(255, 215, 0, 0.4);
  animation: avatar-glow 3s ease-in-out infinite;
}

.avatar-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

@keyframes avatar-glow {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.8; }
}

.header-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.header-info h3 {
  color: #2C5C4D;
  font-size: 16px;
  font-weight: 600;
  margin: 0;
  font-family: 'STKaiti', 'KaiTi', serif;
  letter-spacing: 1px;
}

.online-status {
  display: flex;
  align-items: center;
  gap: 6px;
}

.status-dot {
  width: 8px;
  height: 8px;
  background: #2C5C4D;
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.1); }
}

.status-text {
  font-size: 12px;
  color: #2C5C4D;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 6px;
}

.menu-btn,
.close-btn {
  width: 36px;
  height: 36px;
  background: rgba(194, 139, 78, 0.08);
  border: none;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.menu-btn:hover,
.close-btn:hover {
  background: rgba(194, 139, 78, 0.18);
  transform: scale(1.05);
}

.menu-dropdown {
  position: absolute;
  top: 85px;
  right: 24px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 14px;
  box-shadow: 0 8px 30px rgba(156, 47, 47, 0.15);
  border: 1px solid rgba(194, 139, 78, 0.15);
  overflow: hidden;
  z-index: 10;
  min-width: 140px;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 20px;
  background: none;
  border: none;
  cursor: pointer;
  width: 100%;
  color: #444;
  font-size: 14px;
  transition: all 0.2s;
}

.menu-item:hover {
  background: rgba(194, 139, 78, 0.08);
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px 20px;
  position: relative;
  background-image: 
    url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M20 3c-3 5-6 8-10 10 3-3 6-6 10-9 3 3 6 6 10 9-3-5-6-8-10-10z' fill='%23C28B4E' fill-opacity='0.04'/%3E%3C/svg%3E"),
    url("data:image/svg+xml,%3Csvg width='24' height='24' viewBox='0 0 24 24' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M12 2L9 6l-3-2-3 4 2 1-2 4 3-1 3 3 3-3 3 1-2-4-2-1-3-4 3 2z' fill='%23FFD700' fill-opacity='0.03'/%3E%3C/svg%3E");
}

.chat-messages::-webkit-scrollbar {
  width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
  background: rgba(194, 139, 78, 0.05);
  border-radius: 3px;
}

.chat-messages::-webkit-scrollbar-thumb {
  background: rgba(194, 139, 78, 0.3);
  border-radius: 3px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
  background: rgba(194, 139, 78, 0.5);
}

.watermark {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 140px;
  color: rgba(194, 139, 78, 0.025);
  pointer-events: none;
  font-family: 'STKaiti', 'KaiTi', serif;
  z-index: 0;
}

.message-item {
  display: flex;
  gap: 10px;
  max-width: 90%;
  position: relative;
  z-index: 1;
  margin-bottom: 20px;
}

.message-item.user {
  margin-left: auto;
  flex-direction: row-reverse;
}

.message-item.user .message-content {
  background: linear-gradient(135deg, rgba(156, 47, 47, 0.12) 0%, rgba(194, 139, 78, 0.08) 100%);
  color: #333;
  border-radius: 18px 18px 6px 18px;
  border: 1px solid rgba(156, 47, 47, 0.15);
}

.message-item.bot {
  margin-right: auto;
}

.message-item.bot .message-content {
  background: rgba(255, 255, 255, 0.95);
  color: #333;
  border-radius: 18px 18px 18px 6px;
  border: 1px solid rgba(194, 139, 78, 0.15);
  box-shadow: 0 2px 12px rgba(194, 139, 78, 0.08);
}

.message-avatar {
  flex-shrink: 0;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.message-item.user .message-avatar {
  background: linear-gradient(135deg, rgba(156, 47, 47, 0.15) 0%, rgba(194, 139, 78, 0.1) 100%);
  border: 1px solid rgba(156, 47, 47, 0.2);
}

.message-item.bot .message-avatar {
  background: linear-gradient(135deg, rgba(194, 139, 78, 0.15) 0%, rgba(255, 215, 0, 0.1) 100%);
  border: 1px solid rgba(194, 139, 78, 0.2);
}

.msg-avatar-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.message-content {
  padding: 14px 18px;
  word-break: break-word;
  position: relative;
}

.message-content::before {
  content: '';
  position: absolute;
  width: 8px;
  height: 8px;
  background: inherit;
  border: inherit;
}

.message-item.user .message-content::before {
  right: -4px;
  top: 14px;
  transform: rotate(45deg);
  border-left: none;
  border-bottom: none;
}

.message-item.bot .message-content::before {
  left: -4px;
  top: 14px;
  transform: rotate(45deg);
  border-right: none;
  border-top: none;
}

.message-content p {
  margin: 0;
  font-size: 14px;
  line-height: 1.65;
  color: #444;
}

.loading-indicator {
  display: flex;
  justify-content: flex-start;
  padding: 12px 0;
}

.loading-dots {
  display: flex;
  gap: 8px;
  padding: 10px 16px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 20px;
  border: 1px solid rgba(194, 139, 78, 0.15);
}

.loading-dots span {
  width: 10px;
  height: 10px;
  background: linear-gradient(135deg, #C28B4E 0%, #FFD700 100%);
  border-radius: 50%;
  animation: loading 1.4s infinite ease-in-out both;
  box-shadow: 0 0 6px rgba(194, 139, 78, 0.4);
}

.loading-dots span:nth-child(1) { animation-delay: -0.32s; }
.loading-dots span:nth-child(2) { animation-delay: -0.16s; }
.loading-dots span:nth-child(3) { animation-delay: 0s; }

@keyframes loading {
  0%, 80%, 100% {
    transform: scale(0.6);
    opacity: 0.5;
  }
  40% {
    transform: scale(1);
    opacity: 1;
  }
}

.quick-actions {
  display: flex;
  gap: 10px;
  padding: 14px 16px;
  border-top: 1px solid rgba(194, 139, 78, 0.1);
  border-bottom: 1px solid rgba(194, 139, 78, 0.1);
  overflow-x: auto;
  background: rgba(255, 255, 255, 0.5);
}

.quick-actions::-webkit-scrollbar {
  height: 0;
}

.action-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 10px 14px;
  background: rgba(255, 255, 255, 0.85);
  border: 1.5px solid rgba(194, 139, 78, 0.2);
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  min-width: 75px;
  flex-shrink: 0;
}

.action-btn:hover {
  background: linear-gradient(135deg, rgba(194, 139, 78, 0.1) 0%, rgba(255, 215, 0, 0.05) 100%);
  border-color: rgba(194, 139, 78, 0.4);
  transform: translateY(-3px);
  box-shadow: 0 4px 16px rgba(194, 139, 78, 0.15);
}

.action-icon {
  font-size: 22px;
}

.action-text {
  font-size: 12px;
  color: #555;
  font-weight: 500;
}

.chat-input {
  display: flex;
  gap: 12px;
  padding: 14px 16px;
  background: rgba(255, 255, 255, 0.9);
  border-top: 1px solid rgba(194, 139, 78, 0.15);
}

.chat-input-field {
  flex: 1;
  height: 42px;
  padding: 0 16px;
  border-radius: 26px;
  border: 1.5px solid rgba(194, 139, 78, 0.25);
  background: rgba(250, 246, 235, 0.6);
  font-size: 14px;
  transition: all 0.25s;
  outline: none;
}

.chat-input-field:hover {
  border-color: rgba(194, 139, 78, 0.5);
  box-shadow: 0 0 0 3px rgba(194, 139, 78, 0.08);
}

.chat-input-field:focus {
  border-color: #C28B4E;
  box-shadow: 0 0 0 3px rgba(194, 139, 78, 0.12);
}

.chat-input-field::placeholder {
  color: rgba(194, 139, 78, 0.5);
}

.chat-input-field:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.send-btn {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #9C2F2F 0%, #C28B4E 100%);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 16px rgba(156, 47, 47, 0.4);
}

.send-btn:hover:not(:disabled) {
  transform: scale(1.08);
  box-shadow: 0 6px 20px rgba(156, 47, 47, 0.5);
}

.send-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.slide-right-enter-active,
.slide-right-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.slide-right-enter-from,
.slide-right-leave-to {
  opacity: 0;
}

.slide-right-enter-from .chat-panel,
.slide-right-leave-to .chat-panel {
  transform: translateX(100%);
}

@media (max-width: 768px) {
  .chat-panel {
    width: 94%;
    max-width: none;
    border-radius: 24px 24px 0 0;
    position: absolute;
    bottom: 0;
    left: 3%;
    right: 3%;
    height: 88vh;
    box-shadow: 0 -8px 40px rgba(156, 47, 47, 0.15);
  }
  
  .slide-right-enter-from .chat-panel,
  .slide-right-leave-to .chat-panel {
    transform: translateY(100%);
  }
  
  .chat-header {
    padding: 16px 20px;
  }
  
  .avatar {
    width: 46px;
    height: 46px;
  }
  
  .header-info h3 {
    font-size: 15px;
  }
  
  .action-btn {
    min-width: 65px;
    padding: 8px 12px;
  }
  
  .action-icon {
    font-size: 20px;
  }
  
  .action-text {
    font-size: 11px;
  }
}
</style>