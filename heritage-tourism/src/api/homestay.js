import api from './axios'

export const homestayAPI = {
  // 获取民宿列表
  getHomestayList: () => {
    return api.get('/homestay/')
  },
  // 获取民宿详情
  getHomestayDetail: (id) => {
    return api.get(`/homestay/${id}/`)
  },
  // 获取民宿体验
  getHomestayExperience: () => {
    return api.get('/homestay/experience/')
  }
}
