import api from './axios'

export const heritageAPI = {
  // 获取非遗文化列表
  getHeritageList: () => {
    return api.get('/heritage/')
  },
  // 获取非遗文化详情
  getHeritageDetail: (id) => {
    return api.get(`/heritage/${id}/`)
  },
  // 获取非遗体验
  getHeritageExperience: () => {
    return api.get('/heritage/experience/')
  }
}
