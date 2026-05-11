import api from './axios'

export const productAPI = {
  // 获取产品列表
  getProductList: () => {
    return api.get('/products/')
  },
  // 获取产品详情
  getProductDetail: (id) => {
    return api.get(`/products/${id}/`)
  },
  // 获取农产品
  getAgriculturalProducts: () => {
    return api.get('/products/agricultural/')
  }
}
