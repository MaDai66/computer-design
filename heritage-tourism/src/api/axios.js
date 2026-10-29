import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 15000,
  withCredentials: true
})

const isDevMode = import.meta.env.VITE_DEV_MODE === 'true'

api.interceptors.request.use(
  config => {
    if (!isDevMode) {
      const token = localStorage.getItem('adminToken') || localStorage.getItem('token')
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
      }
    }
    if (!(config.data instanceof FormData)) {
      config.headers['Content-Type'] = 'application/json'
    }
    return config
  },
  error => Promise.reject(error)
)

api.interceptors.response.use(
  response => {
    if (response.status === 204) {
      return { success: true }
    }
    return response.data
  },
  error => {
    const status = error.response?.status
    const url = error.config?.url
    
    if (isDevMode && (status === 404 || status === 401)) {
      console.debug(`[Dev Mode] API skipped: ${url} (${status})`)
    } else {
      console.error('API Error:', error)
      console.error('URL:', url)
      console.error('Status:', status)
    }
    
    const isLoginUrl = url?.includes('/login') || url?.includes('/token')
    const isOnLoginPage = window.location.pathname === '/admin/login' || window.location.pathname === '/login'
    
    if (!isDevMode && status === 401 && !isLoginUrl && !isOnLoginPage) {
      const isAdminRequest = window.location.pathname.startsWith('/admin') || localStorage.getItem('adminToken')
      
      if (isAdminRequest) {
        localStorage.removeItem('adminToken')
        localStorage.removeItem('adminUser')
      } else {
        localStorage.removeItem('token')
        localStorage.removeItem('user')
      }
    }
    return Promise.reject(error)
  }
)

export default api
