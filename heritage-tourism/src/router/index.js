import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SmartTour from '../views/SmartTour.vue'
import TourRouteDetail from '../views/TourRouteDetail.vue'
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
import ActivityDetail from '../views/ActivityDetail.vue'
import PaperCuttingDetail from '../views/PaperCuttingDetail.vue'
import NongakDanceDetail from '../views/NongakDanceDetail.vue'
import ChaganLakeOpeningCeremony from '../views/ChaganLakeOpeningCeremony.vue'
import TravelNoteDetail from '../views/TravelNoteDetail.vue'
import KoreanRiceCakeNoteDetail from '../views/KoreanRiceCakeNoteDetail.vue'
import HomestayExperienceNoteDetail from '../views/HomestayExperienceNoteDetail.vue'
import HeritageArtistDetail from '../views/HeritageArtistDetail.vue'
import GenericProductDetail from '../views/GenericProductDetail.vue'
import CloudWorkshop from '../views/CloudWorkshop.vue'
import ARInteraction from '../views/ARInteraction.vue'
import WinterFishing360 from '../views/WinterFishing360.vue'
import HeritageCategoryDemo from '../views/HeritageCategoryDemo.vue'

// 后台管理组件
import AdminLogin from '../admin/views/Login.vue'
import AdminLayout from '../admin/components/AdminLayout.vue'
import Dashboard from '../admin/views/Dashboard.vue'
import ContentManagement from '../admin/views/ContentManagement.vue'
import UserManagement from '../admin/views/UserManagement.vue'
import OrderManagement from '../admin/views/OrderManagement.vue'
import Analytics from '../admin/views/Analytics.vue'
import Settings from '../admin/views/Settings.vue'

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
  { 
    path: '/product-detail/:id', 
    name: 'ProductDetail', 
    component: GenericProductDetail 
  },
  // 统一的旅游路线详情页
  {
    path: '/tour-detail',
    name: 'TourDetail',
    component: TourRouteDetail
  },
  {
    path: '/tour-detail/:id',
    name: 'TourDetailWithId',
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
  // 兼容旧路由的旅游详情页
  {
    path: '/tour-route-detail',
    name: 'TourRouteDetail',
    component: TourRouteDetail
  },
  {
    path: '/tour-route-detail/:id',
    name: 'TourRouteDetailWithId',
    component: TourRouteDetail
  },
  {
    path: '/chagan-lake-tour-detail',
    name: 'ChaganLakeTourDetail',
    component: TourRouteDetail
  },
  {
    path: '/korean-village-tour-detail',
    name: 'KoreanVillageTourDetail',
    component: TourRouteDetail
  },
  {
    path: '/chagan-lake-opening-ceremony',
    name: 'ChaganLakeOpeningCeremony',
    component: ChaganLakeOpeningCeremony
  },
  {
    path: '/ginseng-product-detail/:id?',
    name: 'GinsengProductDetail',
    component: GenericProductDetail
  },
  {
    path: '/corn-product-detail/:id?',
    name: 'CornProductDetail',
    component: GenericProductDetail
  },
  {
    path: '/honey-product-detail/:id?',
    name: 'HoneyProductDetail',
    component: GenericProductDetail
  },
  {
    path: '/kimchi-product-detail/:id?',
    name: 'KimchiProductDetail',
    component: GenericProductDetail
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
    component: TourRouteDetail
  },
  {
    path: '/heritage-artist-detail/:id',
    name: 'HeritageArtistDetail',
    component: HeritageArtistDetail
  },
  {
    path: '/korean-rice-cake-product-detail/:id?',
    name: 'KoreanRiceCakeProductDetail',
    component: GenericProductDetail
  },
  {
    path: '/chagan-lake-fish-product-detail/:id?',
    name: 'ChaganLakeFishProductDetail',
    component: GenericProductDetail
  },
  {
    path: '/songhua-lake-egg-product-detail/:id?',
    name: 'SonghuaLakeEggProductDetail',
    component: GenericProductDetail
  },
  {
    path: '/cultural-gift-box-product-detail/:id?',
    name: 'CulturalGiftBoxProductDetail',
    component: GenericProductDetail
  },
  {
    path: '/winter-fishing-souvenir-product-detail/:id?',
    name: 'WinterFishingSouvenirProductDetail',
    component: GenericProductDetail
  },
  {
    path: '/scenery-photography-product-detail/:id?',
    name: 'SceneryPhotographyProductDetail',
    component: GenericProductDetail
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
  {
    path: '/heritage-category-demo',
    name: 'HeritageCategoryDemo',
    component: HeritageCategoryDemo
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
      },
      {
        path: 'settings',
        name: 'Settings',
        component: Settings
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
