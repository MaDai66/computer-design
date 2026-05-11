import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  },
  withCredentials: true
})

// 请求拦截器
api.interceptors.request.use(
  config => {
    // 添加token认证信息
    const token = localStorage.getItem('adminToken') || localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  response => {
    // 处理204状态码（无内容响应）
    if (response.status === 204) {
      return { success: true }
    }
    return response.data
  },
  error => {
    console.error('API Error:', error)
    // 处理401错误（未授权）
    if (error.response && error.response.status === 401) {
      // 检查是否是登录请求，如果是登录请求，不要重定向
      const isLoginRequest = error.config.url.includes('/login/')
      if (!isLoginRequest) {
        // 清除登录状态
        localStorage.removeItem('adminToken')
        localStorage.removeItem('adminUser')
        // 跳转到登录页
        window.location.href = '/admin/login'
      }
    }
    return Promise.reject(error)
  }
)

export default api
