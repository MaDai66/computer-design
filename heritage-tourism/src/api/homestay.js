import api from './axios'

export const homestayAPI = {
  getHomestayList: (params = {}) => api.get('/homestay/', { params }),
  getHomestayDetail: (id) => api.get(`/homestay/${id}/`),
  createHomestay: (data) => api.post('/homestay/', data),
  updateHomestay: (id, data) => api.put(`/homestay/${id}/`, data),
  deleteHomestay: (id) => api.delete(`/homestay/${id}/`),
  getExperiences: (params = {}) => api.get('/homestay/experiences/', { params }),
  getExperienceById: (id) => api.get(`/homestay/experiences/${id}/`),
  createExperience: (data) => api.post('/homestay/experiences/', data),
  updateExperience: (id, data) => api.put(`/homestay/experiences/${id}/`, data),
  deleteExperience: (id) => api.delete(`/homestay/experiences/${id}/`)
}
