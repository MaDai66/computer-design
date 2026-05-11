import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'

// 导入API服务
import { userAPI } from './api/users'
import { heritageAPI } from './api/heritage'
import { tourAPI } from './api/tours'
import { activityAPI } from './api/activities'
import { productAPI } from './api/products'
import { homestayAPI } from './api/homestay'
import { communityAPI } from './api/community'

const app = createApp(App)

// 注册API服务到全局
app.config.globalProperties.$api = {
  user: userAPI,
  heritage: heritageAPI,
  tour: tourAPI,
  activity: activityAPI,
  product: productAPI,
  homestay: homestayAPI,
  community: communityAPI
}

app.use(router)
app.mount('#app')
