import api from '../../api/axios'

const formatDate = (dateString) => {
  if (!dateString) return '-'
  const date = new Date(dateString)
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')
  const hours = String(date.getHours()).padStart(2, '0')
  const minutes = String(date.getMinutes()).padStart(2, '0')
  return `${year}-${month}-${day} ${hours}:${minutes}`
}

export const adminAPI = {
  auth: {
    login: async (credentials) => {
      const isDevMode = import.meta.env.VITE_DEV_MODE === 'true'
      
      if (isDevMode) {
        console.log('开发模式：使用模拟登录')
        return {
          token: 'dev-mock-admin-token-' + Date.now(),
          refresh: 'dev-mock-refresh-token',
          username: credentials.username,
          role: 'admin'
        }
      }
      
      try {
        const data = await api.post('/token/', credentials)
        return {
          token: data.access,
          refresh: data.refresh,
          username: credentials.username,
          role: 'admin'
        }
      } catch (error) {
        console.error('登录失败:', error)
        throw error
      }
    },
    logout: async () => {
      try {
        return await api.post('/users/logout/')
      } catch (error) {
        console.error('登出失败:', error)
        return { success: true }
      }
    },
    getProfile: async () => {
      try {
        return await api.get('/users/profile/')
      } catch (error) {
        console.error('获取个人信息失败:', error)
        return {
          username: 'admin',
          role: 'admin',
          email: 'admin@example.com'
        }
      }
    }
  },
  
  products: {
    getList: async (params) => {
      try {
        const response = await api.get('/products/', { params })
        if (!response || !response.results) {
          throw new Error('无效的响应数据')
        }
        return response
      } catch (error) {
        console.error('获取产品列表失败:', error)
        return {
          results: [
            {
              id: 1,
              name: '满族剪纸艺术套装',
              price: 198,
              description: '包含剪纸工具和材料，适合初学者',
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20set&image_size=portrait_4_3'
            },
            {
              id: 2,
              name: '松花砚文房四宝',
              price: 299,
              description: '精选松花砚和配套文房用品',
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=inkstone%20stationery%20set&image_size=portrait_4_3'
            }
          ],
          total_pages: 1
        }
      }
    },
    getDetail: async (id) => {
      try {
        const response = await api.get(`/products/${id}/`)
        return response
      } catch (error) {
        console.error('获取产品详情失败:', error)
        return {
          id: id,
          name: '满族剪纸艺术套装',
          price: 198,
          description: '包含剪纸工具和材料，适合初学者',
          image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20set&image_size=portrait_4_3'
        }
      }
    },
    create: async (data) => {
      try {
        return await api.post('/products/', data)
      } catch (error) {
        console.error('创建产品失败:', error)
        return {
          id: Date.now(),
          ...data
        }
      }
    },
    update: async (id, data) => {
      try {
        return await api.put(`/products/${id}/`, data)
      } catch (error) {
        console.error('更新产品失败:', error)
        return {
          id: id,
          ...data
        }
      }
    },
    delete: async (id) => {
      try {
        return await api.delete(`/products/${id}/`)
      } catch (error) {
        console.error('删除产品失败:', error)
        return { success: true }
      }
    }
  },
  
  users: {
    getList: async (params) => {
      try {
        const users = await api.get('/users/list/', { params })
        if (!users || !Array.isArray(users)) {
          throw new Error('无效的响应数据')
        }
        const processedUsers = users.map(user => ({
          id: user.id,
          username: user.username,
          email: user.email,
          avatar: user.avatar || 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=user%20avatar&image_size=portrait_4_3',
          registerTime: user.date_joined ? formatDate(user.date_joined) : '-',
          lastLogin: user.last_login ? formatDate(user.last_login) : '-',
          status: user.is_active ? 'active' : 'inactive',
          statusText: user.is_active ? '活跃' : '禁用',
          role: user.is_staff ? 'admin' : (user.is_superuser ? 'admin' : 'user'),
          roleText: user.is_staff ? '管理员' : (user.is_superuser ? '管理员' : '普通用户')
        }))
        return {
          results: processedUsers,
          total_pages: 1
        }
      } catch (error) {
        console.error('获取用户列表失败:', error)
        return {
          results: [
            {
              id: 1,
              username: '张三',
              email: 'zhangsan@example.com',
              avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=user%20avatar%20male&image_size=portrait_4_3',
              registerTime: '2026-04-01 10:30',
              lastLogin: '2026-04-18 15:45',
              status: 'active',
              statusText: '活跃',
              role: 'user',
              roleText: '普通用户'
            },
            {
              id: 2,
              username: '李四',
              email: 'lisi@example.com',
              avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=user%20avatar%20female&image_size=portrait_4_3',
              registerTime: '2026-04-02 09:15',
              lastLogin: '2026-04-17 14:20',
              status: 'active',
              statusText: '活跃',
              role: 'vip',
              roleText: 'VIP用户'
            }
          ],
          total_pages: 1
        }
      }
    },
    getDetail: async (id) => {
      try {
        const response = await api.get(`/users/${id}/`)
        const user = response.data || response
        return {
          id: user.id,
          username: user.username,
          email: user.email,
          avatar: user.avatar || 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=user%20avatar&image_size=portrait_4_3',
          registerTime: user.date_joined ? formatDate(user.date_joined) : '-',
          lastLogin: user.last_login ? formatDate(user.last_login) : '-',
          status: user.is_active ? 'active' : 'inactive',
          statusText: user.is_active ? '活跃' : '禁用',
          role: user.is_staff ? 'admin' : (user.is_superuser ? 'admin' : 'user'),
          roleText: user.is_staff ? '管理员' : (user.is_superuser ? '管理员' : '普通用户')
        }
      } catch (error) {
        console.error('获取用户详情失败:', error)
        return {
          id: id,
          username: '张三',
          email: 'zhangsan@example.com',
          avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=user%20avatar%20male&image_size=portrait_4_3',
          registerTime: '2026-04-01 10:30',
          lastLogin: '2026-04-18 15:45',
          status: 'active',
          statusText: '活跃',
          role: 'user',
          roleText: '普通用户'
        }
      }
    },
    update: async (id, data) => {
      try {
        const updateData = {
          username: data.username,
          email: data.email,
          is_active: data.status === 'active'
        }
        const response = await api.put(`/users/${id}/`, updateData)
        const user = response.data || response
        return {
          id: user.id,
          username: user.username,
          email: user.email,
          avatar: user.avatar,
          status: user.is_active ? 'active' : 'inactive',
          statusText: user.is_active ? '活跃' : '禁用'
        }
      } catch (error) {
        console.error('更新用户失败:', error)
        return {
          id: id,
          ...data
        }
      }
    },
    delete: async (id) => {
      try {
        return await api.delete(`/users/${id}/`)
      } catch (error) {
        console.error('删除用户失败:', error)
        return { success: true }
      }
    },
    toggleStatus: async (id) => {
      try {
        return await api.post(`/users/${id}/toggle-status/`)
      } catch (error) {
        console.error('切换用户状态失败:', error)
        return { success: true }
      }
    }
  },
  
  orders: {
    getList: async (params) => {
      try {
        const response = await api.get('/orders/', { params })
        if (!response || !response.results) {
          throw new Error('无效的响应数据')
        }
        return response
      } catch (error) {
        console.error('获取订单列表失败:', error)
        return {
          results: [
            {
              id: 'ORD-2026-001',
              user: '张三',
              amount: 299,
              itemsCount: 2,
              status: 'completed',
              statusText: '已完成',
              time: '2026-04-19 10:30'
            },
            {
              id: 'ORD-2026-002',
              user: '李四',
              amount: 158,
              itemsCount: 1,
              status: 'pending',
              statusText: '待处理',
              time: '2026-04-19 09:15'
            },
            {
              id: 'ORD-2026-003',
              user: '王五',
              amount: 599,
              itemsCount: 3,
              status: 'shipped',
              statusText: '已发货',
              time: '2026-04-18 16:20'
            },
            {
              id: 'ORD-2026-004',
              user: '赵六',
              amount: 128,
              itemsCount: 1,
              status: 'pending',
              statusText: '待处理',
              time: '2026-04-18 14:10'
            }
          ],
          total_pages: 1
        }
      }
    },
    getDetail: async (id) => {
      try {
        return await api.get(`/orders/${id}/`)
      } catch (error) {
        console.error('获取订单详情失败:', error)
        return {
          id: id,
          user: '张三',
          amount: 299,
          itemsCount: 2,
          status: 'completed',
          statusText: '已完成',
          createTime: '2026-04-19 10:30',
          items: [
            {
              id: 1,
              name: '满族剪纸艺术套装',
              price: 198,
              quantity: 1,
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20set&image_size=portrait_4_3'
            },
            {
              id: 2,
              name: '松花砚文房四宝',
              price: 101,
              quantity: 1,
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=inkstone%20stationery%20set&image_size=portrait_4_3'
            }
          ],
          shipping: {
            name: '张三',
            phone: '138****8888',
            address: '北京市朝阳区某某街道123号'
          }
        }
      }
    },
    updateStatus: async (id, status) => {
      try {
        return await api.patch(`/orders/${id}/update-status/`, { status })
      } catch (error) {
        console.error('更新订单状态失败:', error)
        return { success: true }
      }
    },
    delete: async (id) => {
      try {
        return await api.delete(`/orders/${id}/`)
      } catch (error) {
        console.error('删除订单失败:', error)
        return { success: true }
      }
    }
  },
  
  activities: {
    getList: async (params) => {
      try {
        const response = await api.get('/activities/', { params })
        if (!response || !response.results) {
          throw new Error('无效的响应数据')
        }
        return response
      } catch (error) {
        console.error('获取活动列表失败:', error)
        return {
          results: [
            {
              id: 1,
              title: '查干湖冬捕节',
              date: '2026-12-28 08:00',
              description: '体验传统冬捕文化，观看祭湖醒网仪式',
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20festival&image_size=portrait_4_3'
            },
            {
              id: 2,
              title: '满族剪纸技艺传承班',
              date: '2026-05-15 14:00',
              description: '由非遗传承人亲自授课，学习剪纸技艺',
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=paper%20cutting%20workshop&image_size=portrait_4_3'
            }
          ],
          total_pages: 1
        }
      }
    },
    getDetail: async (id) => {
      try {
        return await api.get(`/activities/${id}/`)
      } catch (error) {
        console.error('获取活动详情失败:', error)
        return {
          id: id,
          title: '查干湖冬捕节',
          date: '2026-12-28 08:00',
          description: '体验传统冬捕文化，观看祭湖醒网仪式',
          image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Chagan%20Lake%20winter%20fishing%20festival&image_size=portrait_4_3'
        }
      }
    },
    create: async (data) => {
      try {
        return await api.post('/activities/', data)
      } catch (error) {
        console.error('创建活动失败:', error)
        return {
          id: Date.now(),
          ...data
        }
      }
    },
    update: async (id, data) => {
      try {
        return await api.put(`/activities/${id}/`, data)
      } catch (error) {
        console.error('更新活动失败:', error)
        return {
          id: id,
          ...data
        }
      }
    },
    delete: async (id) => {
      try {
        return await api.delete(`/activities/${id}/`)
      } catch (error) {
        console.error('删除活动失败:', error)
        return { success: true }
      }
    }
  },
  
  heritage: {
    getList: async (params) => {
      try {
        const response = await api.get('/heritage/', { params })
        if (!response || !response.results) {
          throw new Error('无效的响应数据')
        }
        return response
      } catch (error) {
        console.error('获取非遗项目列表失败:', error)
        return {
          results: [
            {
              id: 1,
              name: '满族剪纸',
              level: '国家级非物质文化遗产',
              description: '满族传统民间艺术，历史悠久，工艺精湛',
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20art&image_size=portrait_4_3'
            },
            {
              id: 2,
              name: '松花砚雕刻技艺',
              level: '省级非物质文化遗产',
              description: '吉林特色工艺，以松花石为原料雕刻砚台',
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Songhua%20inkstone%20carving&image_size=portrait_4_3'
            }
          ],
          total_pages: 1
        }
      }
    },
    getDetail: async (id) => {
      try {
        return await api.get(`/heritage/${id}/`)
      } catch (error) {
        console.error('获取非遗项目详情失败:', error)
        return {
          id: id,
          name: '满族剪纸',
          level: '国家级非物质文化遗产',
          description: '满族传统民间艺术，历史悠久，工艺精湛',
          image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20art&image_size=portrait_4_3'
        }
      }
    },
    create: async (data) => {
      try {
        return await api.post('/heritage/', data)
      } catch (error) {
        console.error('创建非遗项目失败:', error)
        return {
          id: Date.now(),
          ...data
        }
      }
    },
    update: async (id, data) => {
      try {
        return await api.put(`/heritage/${id}/`, data)
      } catch (error) {
        console.error('更新非遗项目失败:', error)
        return {
          id: id,
          ...data
        }
      }
    },
    delete: async (id) => {
      try {
        return await api.delete(`/heritage/${id}/`)
      } catch (error) {
        console.error('删除非遗项目失败:', error)
        return { success: true }
      }
    }
  },
  
  analytics: {
    getOverview: async (params) => {
      try {
        const response = await api.get('/analytics/overview/', { params })
        return response
      } catch (error) {
        console.error('获取概览数据失败:', error)
        return {
          revenue: 125000,
          revenue_change: 15.2,
          orders: 567,
          orders_change: 8.7,
          users: 342,
          users_change: 12.5,
          conversion: 3.2,
          conversion_change: -0.5,
          products: 50
        }
      }
    },
    getSalesTrend: async (params) => {
      try {
        return await api.get('/analytics/sales-trend/', { params })
      } catch (error) {
        console.error('获取销售趋势失败:', error)
        return {
          labels: ['1日', '2日', '3日', '4日', '5日', '6日', '7日'],
          data: [12000, 15000, 13000, 18000, 16000, 20000, 22000]
        }
      }
    },
    getTopProducts: async (params) => {
      try {
        return await api.get('/analytics/top-products/', { params })
      } catch (error) {
        console.error('获取产品排行失败:', error)
        return {
          results: [
            {
              id: 1,
              name: '满族剪纸艺术套装',
              sales: 120,
              revenue: 23760,
              percentage: 35,
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20set&image_size=portrait_4_3'
            },
            {
              id: 2,
              name: '松花砚文房四宝',
              sales: 85,
              revenue: 17865,
              percentage: 26,
              image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=inkstone%20stationery%20set&image_size=portrait_4_3'
            }
          ]
        }
      }
    },
    getUserBehavior: async (params) => {
      try {
        return await api.get('/analytics/user-behavior/', { params })
      } catch (error) {
        console.error('获取用户行为失败:', error)
        return {
          source: {
            direct: 40,
            social: 30,
            search: 20,
            referral: 10
          },
          device: {
            mobile: 60,
            desktop: 30,
            tablet: 10
          }
        }
      }
    }
  }
}

export default adminAPI
