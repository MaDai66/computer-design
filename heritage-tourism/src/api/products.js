import api from './axios'

export const productAPI = {
  getProductList: (params = {}) => api.get('/products/', { params }),
  getProductDetail: (id) => api.get(`/products/${id}/`),
  getProductReviews: (id) => api.get(`/products/${id}/reviews/`)
}
