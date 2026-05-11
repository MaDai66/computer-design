import api from './axios'

export const activityAPI = {
  // 获取活动列表
  getActivityList: () => {
    return api.get('/activities/')
  },
  // 获取活动详情
  getActivityDetail: (id) => {
    return api.get(`/activities/${id}/`)
  },
  // 获取即将开始的活动
  getUpcomingActivities: () => {
    return api.get('/activities/upcoming/')
  }
}
