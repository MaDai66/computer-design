import api from './axios'

export const heritageAPI = {
  getHeritageList: (params = {}) => api.get('/heritage/', { params }),
  getHeritageDetail: (id) => api.get(`/heritage/${id}/`),
  createHeritage: (data) => api.post('/heritage/', data),
  updateHeritage: (id, data) => api.put(`/heritage/${id}/`, data),
  deleteHeritage: (id) => api.delete(`/heritage/${id}/`),
  getExperiences: (params = {}) => api.get('/heritage/experiences/', { params }),
  getExperienceById: (id) => api.get(`/heritage/experiences/${id}/`),
  createExperience: (data) => api.post('/heritage/experiences/', data),
  updateExperience: (id, data) => api.put(`/heritage/experiences/${id}/`, data),
  deleteExperience: (id) => api.delete(`/heritage/experiences/${id}/`)
}
