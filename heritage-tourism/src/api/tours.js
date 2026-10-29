import api from './axios'

export const tourAPI = {
  getTourList: (params = {}) => api.get('/tours/', { params }),
  getTourDetail: (id) => api.get(`/tours/${id}/`),
  createTour: (data) => api.post('/tours/', data),
  updateTour: (id, data) => api.put(`/tours/${id}/`, data),
  deleteTour: (id) => api.delete(`/tours/${id}/`),
  getTourDays: (params = {}) => api.get('/tours/days/', { params }),
  createTourDay: (data) => api.post('/tours/days/', data),
  getTimeSlots: (params = {}) => api.get('/tours/time-slots/', { params }),
  createTimeSlot: (data) => api.post('/tours/time-slots/', data),
  getHighlights: (params = {}) => api.get('/tours/highlights/', { params }),
  createHighlight: (data) => api.post('/tours/highlights/', data),
  getCostInfo: (params = {}) => api.get('/tours/cost-info/', { params }),
  createCostInfo: (data) => api.post('/tours/cost-info/', data),
  getReviews: (params = {}) => api.get('/tours/reviews/', { params }),
  createReview: (data) => api.post('/tours/reviews/', data),
  getTourReviews: (tourId, params = {}) => api.get(`/tours/${tourId}/reviews/`, { params }),
  customizeRoute: (data) => api.post('/tours/customize/', data)
}
