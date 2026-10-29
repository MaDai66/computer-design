<template>
  <div class="markdown-content" v-html="renderedContent"></div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  content: String
})

const renderedContent = computed(() => {
  let html = props.content || ''
  
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
  
  html = html.replace(/^\*\*(.*?)\*\*$/gm, '<h3>$1</h3>')
  
  html = html.replace(/^(\d+)\.\s(.+)$/gm, '<li class="ordered-item">$1. $2</li>')
  html = html.replace(/(<li class="ordered-item">[\s\S]*?<\/li>)/g, '<ol class="ordered-list">$1</ol>')
  
  html = html.replace(/^-\s(.+)$/gm, '<li class="unordered-item">$1</li>')
  html = html.replace(/(<li class="unordered-item">[\s\S]*?<\/li>)/g, '<ul class="unordered-list">$1</ul>')
  
  html = html.replace(/<\/(ol|ul)>\s*<ol|<\/(ol|ul)>\s*<ul/g, '</$1><$2')
  
  const blocks = html.split(/\n\n+/)
  const processedBlocks = blocks.map(block => {
    if (block.startsWith('<h3') || block.startsWith('<ol') || block.startsWith('<ul')) {
      return block
    }
    return `<p>${block.trim()}</p>`
  })
  
  return processedBlocks.join('')
})
</script>

<style scoped>
.markdown-content {
  line-height: 1.8;
  color: #444;
}

h3 {
  font-size: 16px;
  font-weight: 600;
  color: #2C5C4D;
  margin: 16px 0 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(194, 139, 78, 0.2);
}

.ordered-list,
.unordered-list {
  margin: 12px 0;
  padding-left: 24px;
}

.ordered-list li,
.unordered-list li {
  margin: 8px 0;
}

.ordered-list {
  list-style-type: decimal;
}

.unordered-list {
  list-style-type: disc;
}

.unordered-list li::marker {
  color: #C28B4E;
}

p {
  margin: 12px 0;
  text-indent: 2em;
}

strong {
  color: #9C2F2F;
  font-weight: 600;
}
</style>