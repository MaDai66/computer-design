<template>
  <div 
    class="float-button" 
    @click="$emit('click')"
    @mouseenter="isHovered = true"
    @mouseleave="isHovered = false"
    :class="{ 'active': isHovered }"
  >
    <div class="glow-ring outer"></div>
    <div class="glow-ring inner"></div>
    <div class="float-icon">
      <img src="/aji.png" alt="阿吉" class="avatar-img" />
    </div>
    <div v-if="unreadCount > 0" class="unread-badge">{{ unreadCount > 9 ? '9+' : unreadCount }}</div>
    <div class="snow-particles">
      <span class="snowflake" v-for="i in 6" :key="i" :class="`snowflake-${i}`"></span>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  customIcon: String
})

defineEmits(['click'])

const isHovered = ref(false)
const unreadCount = ref(1)
</script>

<style scoped>
.float-button {
  position: fixed;
  right: 24px;
  bottom: 24px;
  width: 64px;
  height: 64px;
  background: rgba(250, 246, 235, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 8px 32px rgba(194, 139, 78, 0.4), 0 0 0 1px rgba(194, 139, 78, 0.2);
  border: 2px solid rgba(194, 139, 78, 0.3);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 9999;
  user-select: none;
  overflow: hidden;
  animation: breathe 3s ease-in-out infinite;
}

@keyframes breathe {
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 8px 32px rgba(194, 139, 78, 0.4), 0 0 0 1px rgba(194, 139, 78, 0.2);
  }
  50% {
    transform: scale(1.05);
    box-shadow: 0 12px 40px rgba(194, 139, 78, 0.5), 0 0 0 1px rgba(194, 139, 78, 0.3);
  }
}

.float-button:hover {
  transform: scale(1.18);
  box-shadow: 0 16px 48px rgba(194, 139, 78, 0.5), 0 0 0 2px rgba(194, 139, 78, 0.4);
}

.float-button.active {
  transform: scale(1.18);
}

.glow-ring {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
}

.glow-ring.outer {
  inset: -8px;
  border: 2px solid rgba(255, 215, 0, 0.3);
  animation: ring-pulse 3s ease-in-out infinite;
}

.glow-ring.inner {
  inset: -4px;
  border: 1px solid rgba(255, 215, 0, 0.5);
  animation: ring-pulse 3s ease-in-out infinite 0.5s;
}

@keyframes ring-pulse {
  0%, 100% {
    opacity: 0.3;
    transform: scale(1);
  }
  50% {
    opacity: 0.8;
    transform: scale(1.1);
  }
}

.float-icon {
  width: 40px;
  height: 40px;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid rgba(255, 215, 0, 0.4);
  box-shadow: 0 0 12px rgba(255, 215, 0, 0.3);
}

.custom-icon {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.avatar-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.unread-badge {
  position: absolute;
  top: -6px;
  right: -6px;
  background: linear-gradient(135deg, #9C2F2F 0%, #C28B4E 100%);
  color: white;
  font-size: 12px;
  font-weight: bold;
  min-width: 20px;
  height: 20px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 5px;
  box-shadow: 0 2px 10px rgba(156, 47, 47, 0.6);
  animation: shake 1.5s ease-in-out infinite;
  border: 2px solid #FAF6EB;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-1px); }
  75% { transform: translateX(1px); }
}

.snow-particles {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.snowflake {
  position: absolute;
  width: 6px;
  height: 6px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 50%;
  box-shadow: 0 0 4px rgba(255, 255, 255, 0.6);
  animation: snowfall 3s ease-in-out infinite;
}

.snowflake::before,
.snowflake::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: inherit;
  border-radius: inherit;
  box-shadow: inherit;
}

.snowflake::before {
  transform: rotate(60deg);
}

.snowflake::after {
  transform: rotate(120deg);
}

.snowflake-1 { top: 10px; left: 12px; animation-delay: 0s; }
.snowflake-2 { top: 20px; right: 8px; animation-delay: 0.5s; }
.snowflake-3 { top: 35px; left: 8px; animation-delay: 1s; }
.snowflake-4 { top: 15px; left: 28px; animation-delay: 1.5s; }
.snowflake-5 { top: 30px; right: 15px; animation-delay: 2s; }
.snowflake-6 { top: 45px; left: 20px; animation-delay: 2.5s; }

@keyframes snowfall {
  0%, 100% {
    opacity: 0;
    transform: translateY(-5px) scale(0.5);
  }
  50% {
    opacity: 1;
    transform: translateY(5px) scale(1);
  }
}
</style>