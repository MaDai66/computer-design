<template>
  <div ref="panoramaRef" class="panorama-viewer"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';

const props = defineProps({
  src: {
    type: String,
    required: true
  },
  options: {
    type: Object,
    default: () => ({})
  }
});

const panoramaRef = ref(null);
let viewer = null;

onMounted(() => {
  if (window.pannellum && panoramaRef.value) {
    viewer = window.pannellum.viewer(panoramaRef.value, {
      type: 'equirectangular',
      panorama: props.src,
      autoLoad: true,
      showControls: true,
      ...props.options
    });
  }
});

onUnmounted(() => {
  if (viewer) {
    viewer.destroy();
  }
});

// 监听图片变化
watch(() => props.src, (newSrc) => {
  if (viewer) {
    // 销毁旧的viewer并创建新的
    viewer.destroy();
    viewer = window.pannellum.viewer(panoramaRef.value, {
      type: 'equirectangular',
      panorama: newSrc,
      autoLoad: true,
      showControls: true,
      ...props.options
    });
  }
});
</script>

<style scoped>
.panorama-viewer {
  width: 100%;
  height: 100%;
  min-height: 500px;
}
</style>