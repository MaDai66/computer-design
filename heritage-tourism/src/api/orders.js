import api from './axios'

export const orderAPI = {
  createOrder: (orderData) => api.post('/orders/', orderData),
  getOrders: (params = {}) => api.get('/orders/', { params }),
  getMyOrders: (params = {}) => api.get('/orders/my_orders/', { params }),
  getOrderById: (id) => api.get(`/orders/${id}/`),
  updateOrder: (id, data) => api.put(`/orders/${id}/`, data),
  deleteOrder: (id) => api.delete(`/orders/${id}/`)
}

export default orderAPI
