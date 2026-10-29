<script setup>
import { ref } from 'vue'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import FloatButton from './components/FloatButton.vue'
import ChatPanel from './components/ChatPanel.vue'

const showChat = ref(false)

const handleFloatButtonClick = () => {
  showChat.value = true
}

const handleCloseChat = () => {
  showChat.value = false
}
</script>

<template>
  <div class="app">
    <Navbar />
    <main class="main-content">
      <router-view />
    </main>
    <Footer />
    
    <FloatButton @click="handleFloatButtonClick" />
    <ChatPanel :visible="showChat" @close="handleCloseChat" />
  </div>
</template>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.main-content {
  flex: 1;
}
</style>