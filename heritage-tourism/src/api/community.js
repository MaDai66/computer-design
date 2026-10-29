import api from './axios'

export const communityAPI = {
  getCommunityList: (params = {}) => api.get('/community/', { params }),
  getCommunityDetail: (id) => api.get(`/community/${id}/`),
  createCommunityPost: (data) => api.post('/community/', data),
  updateCommunityPost: (id, data) => api.put(`/community/${id}/`, data),
  deleteCommunityPost: (id) => api.delete(`/community/${id}/`),
  getTravelNotes: (params = {}) => api.get('/community/travel-notes/', { params }),
  getTravelNoteById: (id) => api.get(`/community/travel-notes/${id}/`),
  createTravelNote: (data) => api.post('/community/travel-notes/', data),
  updateTravelNote: (id, data) => api.put(`/community/travel-notes/${id}/`, data),
  deleteTravelNote: (id) => api.delete(`/community/travel-notes/${id}/`)
}
