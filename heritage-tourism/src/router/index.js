import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SmartTour from '../views/SmartTour.vue'
import Heritage from '../views/Heritage.vue'
import Homestay from '../views/Homestay.vue'
import Gifts from '../views/Gifts.vue'
import Profile from '../views/Profile.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import RecommendList from '../views/RecommendList.vue'
import HeritageTourList from '../views/HeritageTourList.vue'
import HeritageExperienceDetail from '../views/HeritageExperienceDetail.vue'
import HomestayDetail from '../views/HomestayDetail.vue'
import ProductDetail from '../views/ProductDetail.vue'
import TourRouteDetail from '../views/TourRouteDetail.vue'
import ActivityDetail from '../views/ActivityDetail.vue'
import PaperCuttingDetail from '../views/PaperCuttingDetail.vue'
import NongakDanceDetail from '../views/NongakDanceDetail.vue'
import KoreanVillageTourDetail from '../views/KoreanVillageTourDetail.vue'
import ChaganLakeTourDetail from '../views/ChaganLakeTourDetail.vue'
import ChaganLakeOpeningCeremony from '../views/ChaganLakeOpeningCeremony.vue'
import GinsengProductDetail from '../views/GinsengProductDetail.vue'
import CornProductDetail from '../views/CornProductDetail.vue'
import HoneyProductDetail from '../views/HoneyProductDetail.vue'
import KimchiProductDetail from '../views/KimchiProductDetail.vue'
import TravelNoteDetail from '../views/TravelNoteDetail.vue'
import KoreanRiceCakeNoteDetail from '../views/KoreanRiceCakeNoteDetail.vue'
import HomestayExperienceNoteDetail from '../views/HomestayExperienceNoteDetail.vue'
import SonghuaLakeTourDetail from '../views/SonghuaLakeTourDetail.vue'
import HeritageArtistDetail from '../views/HeritageArtistDetail.vue'

import KoreanRiceCakeProductDetail from '../views/KoreanRiceCakeProductDetail.vue'
import ChaganLakeFishProductDetail from '../views/ChaganLakeFishProductDetail.vue'
import SonghuaLakeEggProductDetail from '../views/SonghuaLakeEggProductDetail.vue'
import CulturalGiftBoxProductDetail from '../views/CulturalGiftBoxProductDetail.vue'
import WinterFishingSouvenirProductDetail from '../views/WinterFishingSouvenirProductDetail.vue'
import SceneryPhotographyProductDetail from '../views/SceneryPhotographyProductDetail.vue'
import CloudWorkshop from '../views/CloudWorkshop.vue'
import ARInteraction from '../views/ARInteraction.vue'
import WinterFishing360 from '../views/WinterFishing360.vue'

// 后台管理组件
import AdminLogin from '../admin/views/Login.vue'
import AdminLayout from '../admin/components/AdminLayout.vue'
import Dashboard from '../admin/views/Dashboard.vue'
import ContentManagement from '../admin/views/ContentManagement.vue'
import UserManagement from '../admin/views/UserManagement.vue'
import OrderManagement from '../admin/views/OrderManagement.vue'
import Analytics from '../admin/views/Analytics.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/smart-tour',
    name: 'SmartTour',
    component: SmartTour
  },
  {
    path: '/heritage',
    name: 'Heritage',
    component: Heritage
  },
  {
    path: '/homestay',
    name: 'Homestay',
    component: Homestay
  },
  {
    path: '/gifts',
    name: 'Gifts',
    component: Gifts
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/recommend-list',
    name: 'RecommendList',
    component: RecommendList
  },
  {
    path: '/heritage-tour-list',
    name: 'HeritageTourList',
    component: HeritageTourList
  },
  {
    path: '/heritage-experience-detail',
    name: 'HeritageExperienceDetail',
    component: HeritageExperienceDetail
  },
  {
    path: '/homestay-detail/:id',
    name: 'HomestayDetail',
    component: HomestayDetail
  },
  { path: '/product-detail/:id', name: 'ProductDetail', component: ProductDetail },
  {
    path: '/tour-route-detail',
    name: 'TourRouteDetail',
    component: TourRouteDetail
  },
  {
    path: '/activity-detail',
    name: 'ActivityDetail',
    component: ActivityDetail
  },
  {
    path: '/paper-cutting-detail',
    name: 'PaperCuttingDetail',
    component: PaperCuttingDetail
  },
  {
    path: '/nongak-dance-detail',
    name: 'NongakDanceDetail',
    component: NongakDanceDetail
  },
  {
    path: '/korean-village-tour-detail',
    name: 'KoreanVillageTourDetail',
    component: KoreanVillageTourDetail
  },
  {
    path: '/chagan-lake-tour-detail',
    name: 'ChaganLakeTourDetail',
    component: ChaganLakeTourDetail
  },
  {
    path: '/chagan-lake-opening-ceremony',
    name: 'ChaganLakeOpeningCeremony',
    component: ChaganLakeOpeningCeremony
  },
  {
    path: '/ginseng-product-detail',
    name: 'GinsengProductDetail',
    component: GinsengProductDetail
  },
  {
    path: '/corn-product-detail',
    name: 'CornProductDetail',
    component: CornProductDetail
  },
  {
    path: '/honey-product-detail',
    name: 'HoneyProductDetail',
    component: HoneyProductDetail
  },
  {
    path: '/kimchi-product-detail',
    name: 'KimchiProductDetail',
    component: KimchiProductDetail
  },
  {
    path: '/travel-note-detail',
    name: 'TravelNoteDetail',
    component: TravelNoteDetail
  },
  {
    path: '/korean-rice-cake-note-detail',
    name: 'KoreanRiceCakeNoteDetail',
    component: KoreanRiceCakeNoteDetail
  },
  {
    path: '/homestay-experience-note-detail',
    name: 'HomestayExperienceNoteDetail',
    component: HomestayExperienceNoteDetail
  },
  {
    path: '/songhua-lake-tour-detail',
    name: 'SonghuaLakeTourDetail',
    component: SonghuaLakeTourDetail
  },
  {
    path: '/heritage-artist-detail/:id',
    name: 'HeritageArtistDetail',
    component: HeritageArtistDetail
  },

  {
    path: '/korean-rice-cake-product-detail',
    name: 'KoreanRiceCakeProductDetail',
    component: KoreanRiceCakeProductDetail
  },
  {
    path: '/chagan-lake-fish-product-detail',
    name: 'ChaganLakeFishProductDetail',
    component: ChaganLakeFishProductDetail
  },
  {
    path: '/songhua-lake-egg-product-detail',
    name: 'SonghuaLakeEggProductDetail',
    component: SonghuaLakeEggProductDetail
  },
  {
    path: '/cultural-gift-box-product-detail',
    name: 'CulturalGiftBoxProductDetail',
    component: CulturalGiftBoxProductDetail
  },
  {
    path: '/winter-fishing-souvenir-product-detail',
    name: 'WinterFishingSouvenirProductDetail',
    component: WinterFishingSouvenirProductDetail
  },
  {
    path: '/scenery-photography-product-detail',
    name: 'SceneryPhotographyProductDetail',
    component: SceneryPhotographyProductDetail
  },
  {
    path: '/cloud-workshop',
    name: 'CloudWorkshop',
    component: CloudWorkshop
  },
  {
    path: '/winter-fishing-360',
    name: 'WinterFishing360',
    component: WinterFishing360
  },
  {
    path: '/ar-interaction',
    name: 'ARInteraction',
    component: ARInteraction
  },
  
  // 后台管理路由
  {
    path: '/admin/login',
    name: 'AdminLogin',
    component: AdminLogin
  },
  {
    path: '/admin',
    name: 'Admin',
    component: AdminLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'AdminDashboard',
        component: Dashboard
      },
      {
        path: 'content',
        name: 'ContentManagement',
        component: ContentManagement
      },
      {
        path: 'users',
        name: 'UserManagement',
        component: UserManagement
      },
      {
        path: 'orders',
        name: 'OrderManagement',
        component: OrderManagement
      },
      {
        path: 'analytics',
        name: 'Analytics',
        component: Analytics
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  // 检查是否需要认证
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // 检查是否已登录
    const token = localStorage.getItem('adminToken')
    if (!token) {
      // 未登录，重定向到登录页
      next({ name: 'AdminLogin' })
    } else {
      // 已登录，继续
      next()
    }
  } else {
    // 不需要认证的页面，直接通过
    next()
  }
})

export default router