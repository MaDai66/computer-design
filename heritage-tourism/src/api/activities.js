import api from './axios'

export const activityAPI = {
  getActivityList: (params = {}) => api.get('/activities/', { params }),
  getActivityDetail: (id) => api.get(`/activities/${id}/`),
  createActivity: (data) => api.post('/activities/', data),
  updateActivity: (id, data) => api.put(`/activities/${id}/`, data),
  deleteActivity: (id) => api.delete(`/activities/${id}/`),
  getUpcomingActivities: (params = {}) => api.get('/activities/', { params })
}
