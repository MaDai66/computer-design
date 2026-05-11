<template>
  <div class="recommend-list">
    <div class="container">
      <h1 class="page-title">为你精选</h1>
      
      <div class="recommend-items">
        <div class="recommend-item" v-for="(item, index) in recommendItems" :key="index">
          <div class="item-image">
            <img :src="item.image" :alt="item.title" />
          </div>
          <div class="item-content">
            <div class="item-tags">
              <span v-for="(tag, tagIndex) in item.tags" :key="tagIndex" :class="['tag', `tag-${tag.type}`]">{{ tag.name }}</span>
            </div>
            <h3 class="item-title">{{ item.title }}</h3>
            <p class="item-description">{{ item.description }}</p>
            <div class="item-footer">
              <span class="item-price">{{ item.price }}</span>
              <button class="btn btn-secondary">{{ item.button }}</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 回到顶部按钮 -->
    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const showBackToTop = ref(false)

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

const recommendItems = ref([
  {
    id: 1,
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20Korean%20rice%20cake%20making%20experience%20traditional%20craft&image_size=portrait_4_3',
    title: '朝鲜族打糕制作体验',
    description: '亲手体验传统打糕制作，感受朝鲜族饮食文化',
    price: '¥88/人',
    button: '预订',
    tags: [
      { name: '非遗体验', type: 'red' },
      { name: '推荐', type: 'green' }
    ]
  },
  {
    id: 2,
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20traditional%20farmhouse%20stay%20rural%20accommodation&image_size=portrait_4_3',
    title: '长白山脚下农家院',
    description: '体验乡村生活，感受自然之美',
    price: '¥280/晚',
    button: '预订',
    tags: [
      { name: '农家自营', type: 'green' },
      { name: '热销', type: 'blue' }
    ]
  },
  {
    id: 3,
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20art%20traditional%20craft%20Jilin&image_size=portrait_4_3',
    title: '满族剪纸艺术套装',
    description: '传统剪纸工艺，精美文创礼品',
    price: '¥128',
    button: '购买',
    tags: [
      { name: '文创产品', type: 'orange' },
      { name: '满减', type: 'blue' }
    ]
  }
])

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
.recommend-list {
  padding: 48px 0;
  background-color: var(--bg-light);
}

.page-title {
  font-size: 28px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 32px;
  text-align: center;
}

.recommend-items {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.recommend-item {
  display: flex;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.recommend-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
}

.item-image {
  flex: 0 0 300px;
}

.item-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-content {
  flex: 1;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.item-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}

.tag {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
}

.tag-red {
  background-color: var(--accent-red-light);
  color: var(--accent-red);
}

.tag-green {
  background-color: var(--accent-green-light);
  color: var(--accent-green);
}

.tag-blue {
  background-color: var(--accent-blue-light);
  color: var(--accent-blue);
}

.tag-orange {
  background-color: var(--accent-orange-light);
  color: var(--accent-orange);
}

.item-title {
  font-size: 20px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 12px;
}

.item-description {
  font-size: 14px;
  color: var(--text-medium);
  line-height: 1.5;
  margin-bottom: 20px;
}

.item-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.item-price {
  font-size: 18px;
  font-weight: 600;
  color: var(--accent-orange);
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: var(--radius-md);
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.btn-secondary {
  background-color: transparent;
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
}

.btn-secondary:hover {
  background-color: var(--primary-color);
  color: var(--white);
}

/* Responsive */
@media (max-width: 768px) {
  .recommend-item {
    flex-direction: column;
  }
  
  .item-image {
    flex: 0 0 200px;
  }
  
  .item-content {
    padding: 20px;
  }
  
  .page-title {
    font-size: 24px;
  }
  
  .item-title {
    font-size: 18px;
  }
  
  .back-to-top {
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
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