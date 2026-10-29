<template>
  <div class="product-detail">
    <div class="container">
      <div v-if="loading" class="loading-state">
        <p>加载中...</p>
      </div>

      <div v-else-if="error" class="error-state">
        <p>{{ error }}</p>
        <button class="btn btn-secondary" @click="fetchProduct">重新加载</button>
      </div>

      <template v-else-if="product && product.id">
        <section class="product-main">
          <div class="product-header">
            <h1>{{ product.name }}</h1>
            <div class="product-tags">
              <span v-if="product.origin" class="tag tag-orange">原产地</span>
              <span v-if="product.tags && product.tags.includes('助农')" class="tag tag-green">助农</span>
            </div>
            <div class="product-price">
              <span class="price">¥{{ product.price }} / {{ product.unit }}</span>
              <span class="stock">库存: {{ product.stock }}{{ product.unit }}</span>
            </div>
            <div class="product-stats">
              <span class="sales">销量: {{ product.sales_count }}{{ product.unit }}</span>
              <span class="rating">⭐⭐⭐⭐⭐ {{ product.rating }} ({{ product.review_count }}条评价)</span>
            </div>
          </div>
          <div class="product-images">
            <div class="main-image">
              <img :src="getImageUrl(product.image)" :alt="product.name" />
            </div>
            <div class="gallery">
              <img v-for="(img, index) in product.images" :key="index" :src="getImageUrl(img)" :alt="`${product.name}图片${index+1}`" />
            </div>
          </div>
        </section>

        <section class="product-description">
          <h2>商品描述</h2>
          <div class="description-content">
            <p v-if="product.description">
              {{ product.description }}
            </p>
            <p v-else>暂无描述</p>
          </div>
        </section>

        <section class="product-specs">
          <h2>规格参数</h2>
          <div class="specs-content">
            <table class="specs-table">
              <tbody>
                <tr v-for="(spec, key) in product.specifications" :key="key">
                  <th>{{ key }}</th>
                  <td>{{ spec }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <section class="product-origin">
          <h2>产地溯源</h2>
          <div class="origin-content">
            <div class="farmer-info">
              <h3>{{ product.farmer_name }}</h3>
              <p>{{ product.farmer_description }}</p>
            </div>
            <div class="process-info">
              <h3>{{ product.process_title }}</h3>
              <ol>
                <li v-for="(step, index) in product.process_steps" :key="index">{{ step }}</li>
              </ol>
            </div>
          </div>
        </section>

        <section class="product-quality">
          <h2>质检报告</h2>
          <div class="quality-content">
            <p>{{ product.quality_description }}</p>
            <div v-if="product.quality_image" class="quality-image">
              <img :src="getImageUrl(product.quality_image)" alt="质检报告" />
            </div>
          </div>
        </section>

        <section class="purchase-section">
          <h2>购买</h2>
          <div class="purchase-content">
            <div class="price-info">
              <span class="current-price">¥{{ product.price }}</span>
              <span v-if="product.original_price" class="original-price">¥{{ product.original_price }}</span>
              <span v-if="product.discount" class="discount">{{ product.discount }}</span>
            </div>
            <div class="quantity-control">
              <label>数量</label>
              <div class="quantity-input">
                <button class="btn-minus" @click="decreaseQuantity">&minus;</button>
                <input type="number" v-model="quantity" min="1" />
                <button class="btn-plus" @click="increaseQuantity">&plus;</button>
              </div>
            </div>
            <div class="purchase-buttons">
              <button class="btn btn-secondary add-to-cart">加入购物车</button>
              <button class="btn btn-primary buy-now" @click="openPurchaseModal">立即购买</button>
            </div>
          </div>
        </section>

        <section class="user-reviews">
          <h2>用户评价</h2>
          <div class="reviews-header">
            <div class="rating-overall">
              <span class="rating-score">{{ product.rating }}</span>
              <span class="rating-stars">⭐⭐⭐⭐⭐</span>
              <span class="rating-count">{{ product.review_count }}条评价</span>
            </div>
            <div class="review-filter">
              <button class="filter-btn" :class="{ active: activeFilter === 'all' }" @click="activeFilter = 'all'">全部评价</button>
              <button class="filter-btn" :class="{ active: activeFilter === 'good' }" @click="activeFilter = 'good'">好评</button>
              <button class="filter-btn" :class="{ active: activeFilter === 'medium' }" @click="activeFilter = 'medium'">中评</button>
              <button class="filter-btn" :class="{ active: activeFilter === 'bad' }" @click="activeFilter = 'bad'">差评</button>
              <button class="filter-btn" :class="{ active: activeFilter === 'image' }" @click="activeFilter = 'image'">有图</button>
            </div>
          </div>
          <div class="reviews-list">
            <div v-for="review in filteredReviews" :key="review.id" class="review-item">
              <div class="review-header">
                <div class="user-info">
                  <img :src="getImageUrl(review.avatar)" alt="用户头像" />
                  <div class="user-details">
                    <span class="user-name">{{ review.user_name }}</span>
                    <span class="review-date">{{ review.date }}</span>
                  </div>
                </div>
                <div class="review-rating">
                  <span>{{ '⭐'.repeat(review.rating) }}</span>
                </div>
              </div>
              <div class="review-content">
                <p>{{ review.content }}</p>
                <div v-if="review.images && review.images.length" class="review-images">
                  <img v-for="(img, index) in review.images" :key="index" :src="getImageUrl(img)" :alt="`评价图片${index+1}`" />
                </div>
              </div>
            </div>
          </div>
        </section>
      </template>
    </div>

    <button v-if="showBackToTop" class="back-to-top" @click="scrollToTop">
      ↑
    </button>

    <div v-if="showPurchaseModal" class="modal-overlay" @click="closePurchaseModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3>购买{{ product.name }}</h3>
          <button class="close-btn" @click="closePurchaseModal">&times;</button>
        </div>
        <div class="modal-body">
          <div class="form-group">
            <label for="purchase-name">姓名</label>
            <input type="text" id="purchase-name" v-model="purchaseForm.name" placeholder="请输入您的姓名" />
          </div>
          <div class="form-group">
            <label for="purchase-phone">手机号码</label>
            <input type="tel" id="purchase-phone" v-model="purchaseForm.phone" placeholder="请输入您的手机号码" />
          </div>
          <div class="form-group">
            <label for="purchase-email">电子邮箱</label>
            <input type="email" id="purchase-email" v-model="purchaseForm.email" placeholder="请输入您的电子邮箱" />
          </div>
          <div class="form-group">
            <label for="purchase-address">收货地址</label>
            <textarea id="purchase-address" v-model="purchaseForm.address" placeholder="请输入您的收货地址" rows="3"></textarea>
          </div>
          <div class="form-group">
            <label for="purchase-quantity">购买数量</label>
            <input type="number" id="purchase-quantity" v-model="purchaseForm.quantity" min="1" />
          </div>
          <div class="form-group checkbox-group">
            <input type="checkbox" id="purchase-agree" v-model="purchaseForm.agree" />
            <label for="purchase-agree">我已阅读并同意购买协议和隐私政策</label>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-secondary" @click="closePurchaseModal">取消</button>
          <button class="btn btn-primary" @click="submitPurchase" :disabled="!purchaseForm.agree">确认购买</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { productAPI } from '@/api/products'
import orderAPI from '../api/orders'
import api from '../api/axios'

const route = useRoute()
const router = useRouter()
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const showBackToTop = ref(false)
const showPurchaseModal = ref(false)
const loading = ref(false)
const error = ref(null)

const mockProducts = {
  3: {
    id: 3,
    name: '长白山野生人参',
    description: '长白山野生人参是吉林省的特产，生长在长白山原始森林中，是一种珍贵的中药材。本品选用5年以上的野生人参，经过精心采挖、清洗、烘干等工艺制作而成，保留了人参的天然营养成分。长白山野生人参具有补气养血、益精填髓、强身健体等功效，是滋补养生的佳品。本品包装精美，是送礼和自享的理想选择。',
    image: '/media/Gifts/e4217f9472adace2508ecd7dbabcca40.jpeg',
    images: ['/media/Gifts/89a4b5a38eb9668ab9ae1d085c08f0fc.jpeg', '/media/Gifts/c0246d484a8efffea1cb54944c9e69aa.jpeg', '/media/Gifts/c76373f2b8b4d93acc3cb675bef765f3.jpeg', '/media/Gifts/0f42f70f4d763c5869cdca5d4a6fa012.jpeg'],
    price: 298,
    original_price: 398,
    discount: '7.5折',
    unit: '盒',
    stock: 500,
    sales_count: 1280,
    rating: 4.9,
    review_count: 320,
    tags: ['助农'],
    origin: '吉林省长白山',
    specifications: {
      '规格': '50g/盒（含2-3支）',
      '产地': '吉林省长白山',
      '生长周期': '5年以上',
      '储存方式': '阴凉干燥处保存',
      '保质期': '24个月',
      '包装': '精美礼盒装'
    },
    farmer_name: '长白山农户',
    farmer_description: '本品由长白山当地农户采挖，采用传统采挖方式，确保人参的品质和功效。农户严格遵循采挖规范，只采集5年以上的野生人参，保护长白山的生态环境。',
    process_title: '采挖流程',
    process_steps: [
      '每年9-10月，农户进入长白山原始森林寻找野生人参',
      '发现人参后，小心采挖，保留完整的根须',
      '采挖后立即进行清洗和初步处理',
      '在阳光下自然晾晒，或采用低温烘干技术',
      '经过质检后，进行精美包装'
    ],
    quality_description: '本品经过严格的质量检测，符合国家中药材质量标准。检测项目包括重金属含量、农药残留、微生物指标等，确保产品安全可靠。',
    quality_image: '/media/Gifts/0f42f70f4d763c5869cdca5d4a6fa012.jpeg',
    reviews: [
      { id: 1, user_name: '@养生达人', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '长白山野生人参品质非常好，根须完整，闻起来有浓郁的参香。泡出来的参茶味道醇厚，喝了一段时间后感觉精力充沛，睡眠质量也有所改善。包装也很精美，送人体面。非常推荐！', images: ['/media/Gifts/89a4b5a38eb9668ab9ae1d085c08f0fc.jpeg', '/media/Gifts/c76373f2b8b4d93acc3cb675bef765f3.jpeg'], date: '2026-04-10' },
      { id: 2, user_name: '@健康生活', avatar: '/media/Gifts/968d83f5fe772c5ce06a8107228a3fd3.jpeg', rating: 5, content: '第一次购买长白山野生人参，收到后非常满意。人参的品质很好，根须完整，大小适中。包装精美，送礼很合适。客服态度也很好，解答了我很多关于人参食用方法的问题。会回购的！', images: [], date: '2026-04-05' },
      { id: 3, user_name: '@送礼首选', avatar: '/media/Gifts/bbb0350f1afc796ad6c25dbbc472148c.jpeg', rating: 5, content: '给父母买的，他们很喜欢。人参品质不错，煮出来的汤味道很好，父母说喝了之后感觉身体更有精力了。包装也很精美，看起来很高档。价格也很合理，比实体店便宜很多。非常满意的一次购物！', images: [], date: '2026-03-28' }
    ]
  },
  4: {
    id: 4,
    name: '查干湖有机鱼',
    description: '查干湖有机鱼产自吉林省查干湖，是国家地理标志产品。查干湖水域广阔，水质清澈，鱼类资源丰富。本品选用查干湖特有的有机鲤鱼，经过严格的质量检测，确保产品的新鲜和安全。查干湖有机鱼肉质鲜嫩，营养丰富，是家庭聚餐和节日送礼的佳品。',
    image: '/media/Gifts/24a0af046e886cba3aae92567ffb5dbe.jpeg',
    images: [],
    price: 168,
    original_price: 198,
    discount: '8.5折',
    unit: '条',
    stock: 200,
    sales_count: 856,
    rating: 4.8,
    review_count: 210,
    tags: ['助农'],
    origin: '吉林省查干湖',
    specifications: {
      '规格': '约3-4斤/条',
      '产地': '吉林省查干湖',
      '储存方式': '冷冻保存',
      '保质期': '18个月',
      '包装': '真空包装'
    },
    farmer_name: '查干湖渔民',
    farmer_description: '本品由查干湖当地渔民捕捞，采用传统捕捞方式，确保鱼类的新鲜和品质。渔民严格遵循有机养殖规范，不使用任何化学添加剂，保护查干湖的生态环境。',
    process_title: '捕捞流程',
    process_steps: [
      '每年冬季，渔民在查干湖进行大规模冬捕',
      '使用传统网具进行捕捞',
      '捕捞后立即进行分拣和处理',
      '快速冷冻，保持鱼类的新鲜度',
      '经过质检后，进行真空包装'
    ],
    quality_description: '本品经过严格的质量检测，符合有机食品标准。检测项目包括重金属含量、农药残留、微生物指标等，确保产品安全可靠。',
    quality_image: '',
    reviews: [
      { id: 1, user_name: '@美食爱好者', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '查干湖有机鱼真的很好吃，肉质鲜嫩，没有腥味。家里人都很喜欢，已经回购好几次了。包装也很用心，收到的时候鱼还是冻得很结实。非常推荐！', images: [], date: '2026-04-08' },
      { id: 2, user_name: '@家庭主妇', avatar: '/media/Gifts/968d83f5fe772c5ce06a8107228a3fd3.jpeg', rating: 5, content: '给孩子做了鱼汤，孩子非常喜欢喝。鱼很新鲜，肉很多，刺也不多。价格也很实惠，比超市便宜很多。非常满意！', images: [], date: '2026-04-02' }
    ]
  },
  5: {
    id: 5,
    name: '吉林有机玉米',
    description: '吉林有机玉米是吉林省的特产，采用有机种植方式，不使用化肥和农药，保证玉米的纯天然品质。本品来自吉林肥沃的黑土地，阳光充足，水源纯净，种植出的玉米口感香甜，营养丰富。吉林有机玉米富含膳食纤维、维生素和矿物质，是健康饮食的理想选择。煮食口感软糯香甜，是家庭日常饮食的美味食材。',
    image: '/media/Gifts/c2ae3f76786b07410ac2fbe6fef7b3f2.jpeg',
    images: ['/media/Gifts/4767d3b83a64b584aed445c0d57958c6.jpeg', '/media/Gifts/47f80c3daf89298b260f18d4bc9e8493.jpeg', '/media/Gifts/cd014228e9011e016eb19f017fc197c7.jpeg', '/media/Gifts/68d71e23ad36b8ef4c54e7c4d2a3bec9.jpeg'],
    price: 39.9,
    original_price: 49.9,
    discount: '8折',
    unit: '斤',
    stock: 1000,
    sales_count: 2560,
    rating: 4.8,
    review_count: 520,
    tags: ['助农'],
    origin: '吉林省',
    specifications: {
      '规格': '5斤装（约8-10根）',
      '产地': '吉林省',
      '种植方式': '有机种植',
      '储存方式': '阴凉干燥处保存',
      '保质期': '7天（新鲜）',
      '包装': '环保真空包装'
    },
    farmer_name: '吉林农户',
    farmer_description: '本品由吉林当地农户种植，采用传统有机种植方式，不使用化肥和农药，确保玉米的纯天然品质。农户严格遵循有机种植规范，保护土壤和生态环境。',
    process_title: '种植流程',
    process_steps: [
      '选择优质有机玉米种子',
      '在吉林肥沃的黑土地上种植',
      '采用有机肥料和天然防治方法',
      '人工采摘，确保新鲜',
      '真空包装，保持新鲜'
    ],
    quality_description: '本品经过严格的质量检测，符合有机食品标准。检测项目包括农药残留、重金属含量、微生物指标等，确保产品安全可靠。',
    quality_image: '/media/Gifts/596a020dd9ad3ddf814535a710f5d453.jpeg',
    reviews: [
      { id: 1, user_name: '@健康生活', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '吉林有机玉米非常好吃，口感香甜软糯，煮出来的玉米香气四溢。包装也很新鲜，收到的时候玉米还是很嫩的。价格也很合理，比超市买的有机玉米便宜很多。非常推荐！', images: ['/media/Gifts/4767d3b83a64b584aed445c0d57958c6.jpeg', '/media/Gifts/68d71e23ad36b8ef4c54e7c4d2a3bec9.jpeg'], date: '2026-04-10' },
      { id: 2, user_name: '@美食爱好者', avatar: '/media/Gifts/968d83f5fe772c5ce06a8107228a3fd3.jpeg', rating: 5, content: '第一次购买吉林有机玉米，收到后非常满意。玉米颗粒饱满，颜色金黄，煮出来的味道香甜，比普通玉米好吃很多。包装也很用心，真空包装保持了玉米的新鲜度。会回购的！', images: [], date: '2026-04-05' },
      { id: 3, user_name: '@家庭主妇', avatar: '/media/Gifts/bbb0350f1afc796ad6c25dbbc472148c.jpeg', rating: 5, content: '给孩子买的，孩子非常喜欢吃。玉米很新鲜，没有农药残留，吃着放心。煮起来也很方便，15分钟就好了。价格也很实惠，比超市便宜。非常满意的一次购物！', images: [], date: '2026-03-28' }
    ]
  },
  6: {
    id: 6,
    name: '长白山天然蜂蜜',
    description: '长白山天然蜂蜜产自吉林省长白山，是一种珍贵的天然食品。本品由当地养蜂人采集长白山百花蜜，经过传统工艺加工而成，保留了蜂蜜的天然营养成分。长白山天然蜂蜜色泽金黄，口感醇厚，具有润肺止咳、润肠通便等功效，是滋补养生的佳品。',
    image: '/media/HoneyProductDetail/main.jpeg',
    images: [],
    price: 88,
    original_price: 118,
    discount: '7.4折',
    unit: '瓶',
    stock: 300,
    sales_count: 650,
    rating: 4.9,
    review_count: 180,
    tags: ['助农'],
    origin: '吉林省长白山',
    specifications: {
      '规格': '500g/瓶',
      '产地': '吉林省长白山',
      '储存方式': '阴凉干燥处保存',
      '保质期': '24个月',
      '包装': '玻璃瓶装'
    },
    farmer_name: '长白山养蜂人',
    farmer_description: '本品由长白山当地养蜂人采集，采用传统养蜂方式，确保蜂蜜的品质和纯度。养蜂人严格遵循有机养蜂规范，不使用任何化学添加剂，保护蜜蜂和生态环境。',
    process_title: '采蜜流程',
    process_steps: [
      '春季，蜜蜂采集长白山百花蜜',
      '养蜂人定期检查蜂箱',
      '使用传统方法采集蜂蜜',
      '经过过滤和消毒处理',
      '装入玻璃瓶中，密封保存'
    ],
    quality_description: '本品经过严格的质量检测，符合国家食品安全标准。检测项目包括水分含量、蔗糖含量、微生物指标等，确保产品安全可靠。',
    quality_image: '',
    reviews: [
      { id: 1, user_name: '@养生达人', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '长白山天然蜂蜜非常纯正，口感醇厚，有淡淡的花香。每天早上喝一杯蜂蜜水，感觉整个人都精神了。包装也很精美，送礼很有面子。非常推荐！', images: [], date: '2026-04-06' }
    ]
  },
  7: {
    id: 7,
    name: '朝鲜族传统泡菜',
    description: '朝鲜族传统泡菜是吉林省朝鲜族的传统美食，采用传统工艺腌制而成。本品选用新鲜的白菜、萝卜等蔬菜，配以辣椒、大蒜、生姜等调料，经过自然发酵而成。朝鲜族传统泡菜口感酸辣爽口，富含乳酸菌，有助于消化，是餐桌上的美味配菜。',
    image: '/media/KimchiProductDetail/main.jpeg',
    images: [],
    price: 45,
    original_price: 58,
    discount: '7.8折',
    unit: '罐',
    stock: 400,
    sales_count: 920,
    rating: 4.7,
    review_count: 280,
    tags: ['助农'],
    origin: '吉林省延边朝鲜族自治州',
    specifications: {
      '规格': '500g/罐',
      '产地': '吉林省延边朝鲜族自治州',
      '储存方式': '冷藏保存',
      '保质期': '6个月',
      '包装': '罐装'
    },
    farmer_name: '朝鲜族农户',
    farmer_description: '本品由延边朝鲜族农户腌制，采用传统腌制工艺，确保泡菜的正宗口味。农户严格遵循传统配方，不使用任何防腐剂和添加剂，保持泡菜的天然风味。',
    process_title: '腌制流程',
    process_steps: [
      '选用新鲜的白菜和萝卜',
      '清洗干净，晾干水分',
      '准备辣椒面、大蒜、生姜等调料',
      '将调料均匀涂抹在蔬菜上',
      '放入密封容器中，自然发酵'
    ],
    quality_description: '本品经过严格的质量检测，符合国家食品安全标准。检测项目包括酸度、亚硝酸盐含量、微生物指标等，确保产品安全可靠。',
    quality_image: '',
    reviews: [
      { id: 1, user_name: '@美食爱好者', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '朝鲜族传统泡菜味道很正宗，酸辣爽口，配米饭吃非常下饭。家里人都很喜欢，已经回购好几次了。价格也很实惠，比超市卖的好吃很多。非常满意！', images: [], date: '2026-04-04' }
    ]
  },
  8: {
    id: 8,
    name: '朝鲜族打糕',
    description: '朝鲜族打糕是吉林省朝鲜族的传统美食，采用传统工艺制作而成。本品选用优质糯米，经过浸泡、蒸煮、捶打等工序制成。朝鲜族打糕口感软糯香甜，是节日和喜庆场合的必备食品。本品有多种口味可选，包括原味、红豆味、花生味等。',
    image: '/media/KoreanRiceCakeProductDetail/main.jpeg',
    images: [],
    price: 35,
    original_price: 45,
    discount: '7.8折',
    unit: '盒',
    stock: 250,
    sales_count: 480,
    rating: 4.8,
    review_count: 150,
    tags: ['助农'],
    origin: '吉林省延边朝鲜族自治州',
    specifications: {
      '规格': '300g/盒',
      '产地': '吉林省延边朝鲜族自治州',
      '储存方式': '冷藏保存',
      '保质期': '7天',
      '包装': '盒装'
    },
    farmer_name: '朝鲜族糕点师傅',
    farmer_description: '本品由延边朝鲜族糕点师傅制作，采用传统打糕工艺，确保打糕的正宗口味。师傅严格遵循传统配方，不使用任何添加剂，保持打糕的天然风味。',
    process_title: '制作流程',
    process_steps: [
      '选用优质糯米，浸泡4-6小时',
      '将糯米蒸熟',
      '用木锤反复捶打',
      '将打好的糯米切成小块',
      '根据口味添加红豆沙、花生粉等馅料'
    ],
    quality_description: '本品经过严格的质量检测，符合国家食品安全标准。检测项目包括水分含量、微生物指标等，确保产品安全可靠。',
    quality_image: '',
    reviews: [
      { id: 1, user_name: '@甜品爱好者', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '朝鲜族打糕口感软糯香甜，非常好吃。红豆味的特别受欢迎，家里的孩子特别喜欢。包装也很精美，送礼很合适。会回购的！', images: [], date: '2026-04-03' }
    ]
  },
  9: {
    id: 9,
    name: '松花湖咸鸭蛋',
    description: '松花湖咸鸭蛋产自吉林省松花湖，是一种特色美食。本品选用松花湖周边农户散养的鸭蛋，经过传统工艺腌制而成。松花湖咸鸭蛋蛋黄饱满，色泽金黄，油香四溢，是早餐和佐餐的佳品。',
    image: '/media/SonghuaLakeEggProductDetail/main.jpeg',
    images: [],
    price: 58,
    original_price: 78,
    discount: '7.4折',
    unit: '盒',
    stock: 350,
    sales_count: 720,
    rating: 4.7,
    review_count: 220,
    tags: ['助农'],
    origin: '吉林省松花湖',
    specifications: {
      '规格': '20枚/盒',
      '产地': '吉林省松花湖',
      '储存方式': '冷藏保存',
      '保质期': '3个月',
      '包装': '盒装'
    },
    farmer_name: '松花湖农户',
    farmer_description: '本品由松花湖周边农户腌制，采用传统腌制工艺，确保咸鸭蛋的品质和口感。农户严格遵循传统配方，不使用任何添加剂，保持咸鸭蛋的天然风味。',
    process_title: '腌制流程',
    process_steps: [
      '选用新鲜的鸭蛋',
      '清洗干净，晾干水分',
      '准备盐水和香料',
      '将鸭蛋放入盐水中腌制',
      '腌制20-30天后，取出煮熟'
    ],
    quality_description: '本品经过严格的质量检测，符合国家食品安全标准。检测项目包括盐分含量、微生物指标等，确保产品安全可靠。',
    quality_image: '',
    reviews: [
      { id: 1, user_name: '@早餐达人', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '松花湖咸鸭蛋非常好吃，蛋黄油很多，吃起来很香。早上配粥吃特别合适。价格也很实惠，比超市卖的好吃很多。非常满意！', images: [], date: '2026-04-02' }
    ]
  },
  10: {
    id: 10,
    name: '非遗文创礼盒',
    description: '非遗文创礼盒精选吉林省非物质文化遗产手工艺品，包括剪纸、刺绣、木雕等多种传统手工艺品。本品包装精美，是送礼和收藏的理想选择。每一件手工艺品都由非遗传承人亲手制作，具有很高的艺术价值和收藏价值。',
    image: '/media/CulturalGiftBoxProductDetail/main.jpeg',
    images: [],
    price: 388,
    original_price: 488,
    discount: '7.9折',
    unit: '盒',
    stock: 100,
    sales_count: 180,
    rating: 4.9,
    review_count: 85,
    tags: [],
    origin: '吉林省',
    specifications: {
      '规格': '礼盒装',
      '产地': '吉林省',
      '包含': '剪纸、刺绣、木雕各一件',
      '包装': '精美礼盒'
    },
    farmer_name: '非遗传承人',
    farmer_description: '本品由吉林省非遗传承人亲手制作，每一件手工艺品都凝聚了传承人数十年的技艺和心血。传承人严格遵循传统工艺，确保每一件作品的品质和艺术性。',
    process_title: '制作流程',
    process_steps: [
      '选用优质原材料',
      '根据传统工艺进行制作',
      '精心打磨和装饰',
      '进行质量检查',
      '装入精美礼盒'
    ],
    quality_description: '本品经过严格的质量检测，确保每一件手工艺品的品质和艺术性。每件作品都附有非遗传承人的亲笔签名和证书。',
    quality_image: '',
    reviews: [
      { id: 1, user_name: '@文化爱好者', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '非遗文创礼盒非常精美，里面的手工艺品都很有特色。送给朋友作为生日礼物，朋友非常喜欢。包装也很大气，很有面子。非常推荐！', images: [], date: '2026-04-01' }
    ]
  },
  11: {
    id: 11,
    name: '冬捕纪念套装',
    description: '冬捕纪念套装是查干湖冬捕文化的纪念收藏品，包含冬捕主题的特色纪念品，如冬捕鱼模型、纪念徽章、明信片等。本品包装精美，是纪念查干湖冬捕文化的理想选择。',
    image: '/media/WinterFishingSouvenirProductDetail/main.jpeg',
    images: [],
    price: 168,
    original_price: 198,
    discount: '8.5折',
    unit: '套',
    stock: 150,
    sales_count: 320,
    rating: 4.8,
    review_count: 95,
    tags: [],
    origin: '吉林省查干湖',
    specifications: {
      '规格': '套装',
      '产地': '吉林省查干湖',
      '包含': '鱼模型、徽章、明信片',
      '包装': '精美礼盒'
    },
    farmer_name: '查干湖文创团队',
    farmer_description: '本品由查干湖文创团队设计制作，融合了查干湖冬捕文化的特色元素。团队成员深入了解冬捕文化，确保每一件纪念品都具有代表性和纪念意义。',
    process_title: '设计制作流程',
    process_steps: [
      '收集冬捕文化素材',
      '进行创意设计',
      '选用优质材料制作',
      '进行质量检查',
      '装入精美礼盒'
    ],
    quality_description: '本品经过严格的质量检测，确保每一件纪念品的品质和艺术性。每件套装都附有冬捕文化介绍手册。',
    quality_image: '',
    reviews: [
      { id: 1, user_name: '@旅游爱好者', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '冬捕纪念套装很有纪念意义，送给去过查干湖旅游的朋友，朋友非常喜欢。包装也很精美，很有特色。会推荐给其他朋友的！', images: [], date: '2026-03-30' }
    ]
  },
  12: {
    id: 12,
    name: '吉林风光摄影集',
    description: '吉林风光摄影集精选吉林省各地的自然风光和人文景观，由著名摄影师精心拍摄。本品包含长白山、松花湖、查干湖等著名景点的精美照片，是了解吉林自然风光的理想选择。摄影集采用高品质纸张印刷，画面清晰，色彩鲜艳。',
    image: '/media/SceneryPhotographyProductDetail/main.jpeg',
    images: [],
    price: 228,
    original_price: 288,
    discount: '7.9折',
    unit: '本',
    stock: 80,
    sales_count: 150,
    rating: 4.9,
    review_count: 65,
    tags: [],
    origin: '吉林省',
    specifications: {
      '规格': '精装本',
      '产地': '吉林省',
      '页数': '128页',
      '包装': '精装礼盒'
    },
    farmer_name: '吉林摄影家协会',
    farmer_description: '本品由吉林摄影家协会组织拍摄，汇集了省内著名摄影师的优秀作品。摄影师们深入吉林各地，捕捉最美的自然风光和人文景观。',
    process_title: '制作流程',
    process_steps: [
      '摄影师深入各地拍摄',
      '精选优秀作品',
      '进行后期处理',
      '设计排版',
      '采用高品质纸张印刷'
    ],
    quality_description: '本品采用高品质铜版纸印刷，画面清晰，色彩鲜艳。每本摄影集都附有摄影师签名和作品介绍。',
    quality_image: '',
    reviews: [
      { id: 1, user_name: '@摄影爱好者', avatar: '/media/Gifts/c84ffc36243ca6be1925a0dc36dd972e.jpeg', rating: 5, content: '吉林风光摄影集非常精美，里面的照片拍得非常漂亮。送给喜欢摄影的朋友，朋友赞不绝口。印刷质量也很好，物超所值！', images: [], date: '2026-03-28' }
    ]
  }
}

const product = ref({
  id: '',
  name: '',
  description: '',
  image: '',
  images: [],
  price: 0,
  original_price: null,
  discount: '',
  unit: '',
  stock: 0,
  sales_count: 0,
  rating: 0,
  review_count: 0,
  tags: [],
  origin: '',
  specifications: {},
  farmer_name: '',
  farmer_description: '',
  process_title: '',
  process_steps: [],
  quality_description: '',
  quality_image: '',
  reviews: []
})

const purchaseForm = ref({
  name: '',
  phone: '',
  email: '',
  address: '',
  quantity: 1,
  agree: false
})

const quantity = ref(1)
const activeFilter = ref('all')

const getImageUrl = (imagePath) => {
  if (!imagePath) return '/image/default-product.jpeg'
  if (imagePath.startsWith('http')) return imagePath
  if (imagePath.startsWith('/media')) return apiBaseUrl + imagePath
  if (imagePath.startsWith('/image')) return imagePath
  return apiBaseUrl + imagePath
}

const decreaseQuantity = () => {
  if (quantity.value > 1) {
    quantity.value--
  }
}

const increaseQuantity = () => {
  quantity.value++
}

const filteredReviews = computed(() => {
  let reviews = product.value.reviews || []
  switch (activeFilter.value) {
    case 'good':
      return reviews.filter(r => r.rating >= 4)
    case 'medium':
      return reviews.filter(r => r.rating === 3)
    case 'bad':
      return reviews.filter(r => r.rating <= 2)
    case 'image':
      return reviews.filter(r => r.images && r.images.length > 0)
    default:
      return reviews
  }
})

const getMockProductByName = (productId) => {
  const path = route.path.toLowerCase()
  
  if (path.includes('songhua-lake-egg')) {
    return mockProducts[9]
  } else if (path.includes('winter-fishing-souvenir')) {
    return mockProducts[11]
  } else if (path.includes('cultural-gift-box')) {
    return mockProducts[10]
  } else if (path.includes('scenery-photography')) {
    return mockProducts[12]
  } else if (path.includes('chagan-lake-fish')) {
    return mockProducts[4]
  } else if (path.includes('korean-rice-cake')) {
    return mockProducts[8]
  } else if (path.includes('ginseng')) {
    return mockProducts[3]
  } else if (path.includes('corn')) {
    return mockProducts[5]
  } else if (path.includes('honey')) {
    return mockProducts[6]
  } else if (path.includes('kimchi')) {
    return mockProducts[7]
  } else if (path.includes('fish')) {
    return mockProducts[4]
  } else if (path.includes('egg')) {
    return mockProducts[9]
  } else if (path.includes('gift-box')) {
    return mockProducts[10]
  } else if (path.includes('souvenir')) {
    return mockProducts[11]
  } else if (path.includes('photography')) {
    return mockProducts[12]
  } else if (path.includes('rice-cake')) {
    return mockProducts[8]
  }
  
  if (mockProducts[productId]) {
    return mockProducts[productId]
  }
  
  const mockKeys = Object.keys(mockProducts)
  if (mockKeys.length > 0) {
    return mockProducts[mockKeys[0]]
  }
  return null
}

const fetchProduct = async () => {
  loading.value = true
  error.value = null
  try {
    const productId = route.params.id || route.params.productId
    const mockProduct = getMockProductByName(productId)
    
    if (mockProduct) {
      product.value = mockProduct
    } else {
      product.value = {
        id: '1',
        name: '商品名称',
        description: '暂无描述',
        image: '',
        images: [],
        price: 0,
        original_price: null,
        discount: '',
        unit: '件',
        stock: 0,
        sales_count: 0,
        rating: 0,
        review_count: 0,
        tags: [],
        origin: '',
        specifications: {
          '规格': '暂无信息',
          '产地': '暂无信息',
          '储存方式': '暂无信息',
          '保质期': '暂无信息',
          '包装': '暂无信息'
        },
        farmer_name: '农户信息',
        farmer_description: '暂无描述',
        process_title: '制作流程',
        process_steps: ['暂无步骤信息'],
        quality_description: '暂无质检信息',
        quality_image: '',
        reviews: [
          { id: 1, user_name: '@用户', avatar: '', rating: 5, content: '商品很好，非常满意！', images: [], date: '2026-01-01' }
        ]
      }
    }
  } catch (err) {
    console.error('获取产品详情失败:', err)
    const productId = route.params.id || route.params.productId
    const mockProduct = getMockProductByName(productId)
    if (mockProduct) {
      product.value = mockProduct
    } else {
      error.value = '加载产品详情失败，请稍后重试'
    }
  } finally {
    loading.value = false
  }
}

const openPurchaseModal = () => {
  const user = localStorage.getItem('user')
  if (!user) {
    alert('请先登录')
    router.push('/login')
    return
  }
  purchaseForm.value.quantity = quantity.value
  showPurchaseModal.value = true
}

const closePurchaseModal = () => {
  showPurchaseModal.value = false
}

const submitPurchase = async () => {
  // 检查登录状态
  let user = null
  try { user = JSON.parse(localStorage.getItem('user')) } catch (e) {}
  if (!user || !user.id) {
    alert('请先登录')
    router.push('/login')
    return
  }
  
  if (!purchaseForm.value.agree) {
    alert('请先同意购买协议和隐私政策')
    return
  }
  
  if (!purchaseForm.value.name || !purchaseForm.value.phone) {
    alert('请填写姓名和手机号码')
    return
  }
  
  if (!purchaseForm.value.address) {
    alert('请填写收货地址')
    return
  }
  
  try {
    loading.value = true
    const productId = product.value.id
    
    console.log('=== 商品购买信息 ===')
    console.log('productId:', productId)
    console.log('purchaseForm:', purchaseForm.value)
    console.log('product:', product.value)
    
    const orderData = {
      product_id: productId,
      user_id: user.id,
      quantity: purchaseForm.value.quantity || 1,
      contact_name: purchaseForm.value.name,
      contact_phone: purchaseForm.value.phone,
      contact_address: purchaseForm.value.address,
      notes: purchaseForm.value.email ? `邮箱：${purchaseForm.value.email}` : ''
    }
    
    console.log('发送的订单数据:', orderData)
    
    // 调用后端API创建商品订单
    const response = await api.post('/orders/create_product_order/', orderData)
    
    console.log('订单创建成功，响应:', response)
    alert('购买成功！')
    closePurchaseModal()
    router.push('/profile')
  } catch (error) {
    console.error('=== 购买失败 ===')
    console.error('错误对象:', error)
    console.error('响应数据:', JSON.stringify(error.response?.data, null, 2))
    console.error('响应状态:', error.response?.status)

    const errorData = error.response?.data
    let errorMessage = ''
    if (errorData) {
      if (errorData.message) {
        errorMessage = errorData.message
      } else if (errorData.items && errorData.items.length > 0) {
        const itemErrors = errorData.items[0]
        errorMessage = Object.entries(itemErrors).map(([k, v]) => `${k}: ${v}`).join('; ')
      } else {
        errorMessage = JSON.stringify(errorData)
      }
    }
    alert('购买失败: ' + (errorMessage || error.message || '服务器错误'))
  } finally {
    loading.value = false
  }
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

const handleScroll = () => {
  showBackToTop.value = window.scrollY > 300
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  fetchProduct()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.product-detail {
  background-color: var(--bg-light);
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 48px 24px;
}

.loading-state,
.error-state {
  text-align: center;
  padding: 64px 24px;
  background-color: var(--white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
}

.loading-state p,
.error-state p {
  font-size: 16px;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.error-state p {
  color: var(--orange);
}

section {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 32px;
  box-shadow: var(--shadow);
}

section h2 {
  font-size: 24px;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 2px solid var(--primary-color);
}

.product-header h1 {
  font-size: 32px;
  font-weight: 700;
  color: var(--text-dark);
  margin-bottom: 16px;
}

.product-tags {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

.tag {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
}

.tag-orange {
  background-color: var(--accent-orange-light);
  color: var(--accent-orange);
}

.tag-green {
  background-color: var(--accent-green-light);
  color: var(--accent-green);
}

.product-price {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 16px;
}

.price {
  font-size: 24px;
  font-weight: 700;
  color: var(--accent-orange);
}

.stock {
  font-size: 16px;
  color: var(--text-medium);
}

.product-stats {
  display: flex;
  align-items: center;
  gap: 24px;
  font-size: 14px;
  color: var(--text-medium);
}

.product-images {
  margin-bottom: 24px;
}

.main-image {
  width: 100%;
  height: 400px;
  border-radius: var(--radius-md);
  overflow: hidden;
  margin-bottom: 16px;
}

.main-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.gallery img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: var(--transition);
}

.gallery img:hover {
  transform: scale(1.05);
  box-shadow: var(--shadow-hover);
}

.description-content p {
  line-height: 1.6;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.specs-table {
  width: 100%;
  border-collapse: collapse;
}

.specs-table th,
.specs-table td {
  padding: 12px;
  border-bottom: 1px solid var(--border-color);
}

.specs-table th {
  width: 150px;
  font-weight: 600;
  color: var(--text-dark);
  text-align: left;
  background-color: var(--bg-light);
}

.specs-table td {
  color: var(--text-medium);
}

.origin-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.farmer-info h3,
.process-info h3 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
}

.farmer-info p {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 0;
}

.process-info ol {
  padding-left: 20px;
  margin: 0;
}

.process-info li {
  margin-bottom: 8px;
  line-height: 1.4;
  color: var(--text-medium);
}

.quality-content p {
  line-height: 1.6;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.quality-image {
  width: 100%;
  border-radius: var(--radius-md);
  overflow: hidden;
}

.quality-image img {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.purchase-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.price-info {
  display: flex;
  align-items: center;
  gap: 16px;
}

.current-price {
  font-size: 28px;
  font-weight: 700;
  color: var(--accent-orange);
}

.original-price {
  font-size: 18px;
  color: var(--text-light);
  text-decoration: line-through;
}

.discount {
  font-size: 14px;
  color: var(--accent-orange);
  background-color: var(--accent-orange-light);
  padding: 4px 8px;
  border-radius: 12px;
}

.quantity-control {
  display: flex;
  align-items: center;
  gap: 16px;
}

.quantity-control label {
  font-weight: 500;
  color: var(--text-dark);
}

.quantity-input {
  display: flex;
  align-items: center;
  gap: 8px;
}

.quantity-input button {
  width: 32px;
  height: 32px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  background-color: var(--white);
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}

.quantity-input button:hover {
  background-color: var(--bg-light);
  border-color: var(--primary-color);
}

.quantity-input input {
  width: 60px;
  height: 32px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  text-align: center;
  font-size: 16px;
}

.quantity-input input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(26, 188, 156, 0.2);
}

.purchase-buttons {
  display: flex;
  gap: 16px;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: var(--radius-md);
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.btn-primary {
  background-color: var(--primary-color);
  color: var(--white);
}

.btn-primary:hover {
  background-color: var(--primary-hover);
}

.btn-secondary {
  background-color: var(--white);
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
}

.btn-secondary:hover {
  background-color: var(--primary-light);
}

.reviews-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 16px;
}

.rating-overall {
  display: flex;
  align-items: center;
  gap: 12px;
}

.rating-score {
  font-size: 32px;
  font-weight: 700;
  color: var(--accent-orange);
}

.rating-stars {
  font-size: 16px;
  color: var(--accent-orange);
}

.rating-count {
  font-size: 14px;
  color: var(--text-medium);
}

.review-filter {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 8px 16px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  background-color: var(--white);
  cursor: pointer;
  transition: var(--transition);
  font-size: 14px;
}

.filter-btn:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
}

.filter-btn.active {
  background-color: var(--primary-color);
  color: var(--white);
  border-color: var(--primary-color);
}

.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-bottom: 32px;
}

.review-item {
  padding: 24px;
  background-color: var(--bg-light);
  border-radius: var(--radius-md);
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-info img {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.user-details {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.user-name {
  font-weight: 500;
  color: var(--text-dark);
}

.review-date {
  font-size: 12px;
  color: var(--text-light);
}

.review-content p {
  line-height: 1.5;
  color: var(--text-medium);
  margin-bottom: 16px;
}

.review-images {
  display: flex;
  gap: 12px;
}

.review-images img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: var(--radius-sm);
}

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

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: var(--white);
  border-radius: var(--radius-lg);
  width: 90%;
  max-width: 500px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: var(--shadow-lg);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px;
  border-bottom: 1px solid var(--border-color);
}

.modal-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-dark);
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: var(--text-medium);
  cursor: pointer;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius);
  transition: var(--transition);
}

.close-btn:hover {
  background-color: var(--bg-light);
  color: var(--text-dark);
}

.modal-body {
  padding: 24px;
}

.modal-body .form-group {
  margin-bottom: 16px;
}

.modal-body label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: var(--text-dark);
}

.modal-body input,
.modal-body textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  font-size: 14px;
  transition: var(--transition);
}

.modal-body input:focus,
.modal-body textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 2px rgba(26, 188, 156, 0.2);
}

.modal-body textarea {
  resize: vertical;
  min-height: 80px;
}

.checkbox-group {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.checkbox-group input[type="checkbox"] {
  width: auto;
  margin-top: 2px;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  padding: 24px;
  border-top: 1px solid var(--border-color);
}

.modal-footer .btn {
  min-width: 100px;
}

@media (max-width: 768px) {
  .container {
    padding: 24px 16px;
  }
  
  .product-header h1 {
    font-size: 24px;
  }
  
  .main-image {
    height: 250px;
  }
  
  .gallery {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .origin-content {
    grid-template-columns: 1fr;
  }
  
  .quality-image img {
    height: 200px;
  }
  
  .purchase-buttons {
    flex-direction: column;
  }
  
  .back-to-top {
    width: 40px;
    height: 40px;
    font-size: 16px;
    bottom: 24px;
    right: 24px;
  }
  
  .modal-content {
    width: 95%;
    margin: 20px;
  }
  
  .modal-header,
  .modal-body,
  .modal-footer {
    padding: 16px;
  }
}
</style>
