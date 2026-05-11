import api from './axios'

const orderAPI = {
  // 创建订单
  createOrder: async (orderData) => {
    try {
      const response = await api.post('/orders/create/', orderData)
      return response
    } catch (error) {
      console.error('创建订单失败:', error)
      throw error
    }
  },
  
  // 获取订单列表
  getOrders: async () => {
    try {
      const response = await api.get('/orders/')
      return response
    } catch (error) {
      console.error('获取订单失败:', error)
      throw error
    }
  },
  
  // 更新订单状态
  updateOrder: async (orderId, status) => {
    try {
      const response = await api.patch(`/orders/${orderId}/update-status/`, { status })
      return response
    } catch (error) {
      console.error('更新订单失败:', error)
      throw error
    }
  },
  
  // 删除订单
  deleteOrder: async (orderId) => {
    try {
      const response = await api.delete(`/orders/${orderId}/delete/`)
      return response
    } catch (error) {
      console.error('删除订单失败:', error)
      throw error
    }
  }
}

export default orderAPI
