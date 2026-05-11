import api from './axios'

export const communityAPI = {
  // 获取社区帖子列表
  getCommunityList: () => {
    return api.get('/community/')
  },
  // 获取社区帖子详情
  getCommunityDetail: (id) => {
    return api.get(`/community/${id}/`)
  },
  // 获取旅游笔记
  getTravelNote: () => {
    return api.get('/community/travel-note/')
  }
}
