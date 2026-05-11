import api from './axios'

export const userAPI = {
  // 用户注册
  register: (userData) => {
    return api.post('/users/register/', userData)
  },
  // 用户登录
  login: (credentials) => {
    return api.post('/users/login/', credentials)
  },
  // 获取用户信息
  getProfile: () => {
    return api.get('/users/profile/')
  },
  // 更新用户信息
  updateProfile: (userData) => {
    return api.post('/users/profile/', userData)
  }
}
