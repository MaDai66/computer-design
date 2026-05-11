import api from './axios'

export const tourAPI = {
  // 获取旅游路线列表
  getTourList: () => {
    return api.get('/tours/')
  },
  // 获取旅游路线详情
  getTourDetail: (id) => {
    return api.get(`/tours/${id}/`)
  },
  // 获取旅游路线
  getTourRoute: () => {
    return api.get('/tours/route/')
  }
}
