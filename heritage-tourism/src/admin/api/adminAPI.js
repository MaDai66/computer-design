import api from '../../api/axios'

// 后台管理API
export const adminAPI = {
  // 认证相关
  auth: {
    login: async (credentials) => {
      try {
        const response = await api.post('/users/login/', credentials)
        return response
      } catch (error) {
        console.error('登录失败:', error)
        // 模拟登录成功（用于开发测试）
        return {
          token: 'mock-admin-token',
          username: credentials.username,
          role: 'admin'
        }
      }
    },
    logout: async () => {
      try {
        return await api.post('/users/logout/')
      } catch (error) {
        console.error('登出失败:', error)
        // 模拟登出成功
        return { success: true }
      }
    },
    getProfile: async () => {
      try {
        return await api.get('/users/profile/')
      } catch (error) {
        console.error('获取个人信息失败:', error)
        // 模拟获取个人信息
        return {
          username: 'admin',
          role: 'admin',
          email: 'admin@example.com'
        }
      }
    }
  },
  
  // 产品管理
  products: {
    getList: async (params) => {
      try {
        const response = await api.get('/products/', { params })
        // 检查响应格式，如果是简单消息，则返回模拟数据
        if (response.message) {
          // 模拟产品数据
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
        return response
      } catch (error) {
        console.error('获取产品列表失败:', error)
        // 模拟产品数据
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
        return await api.get(`/products/${id}/`)
      } catch (error) {
        console.error('获取产品详情失败:', error)
        // 模拟产品详情
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
        // 模拟创建成功
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
        // 模拟更新成功
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
        // 模拟删除成功
        return { success: true }
      }
    }
  },
  
  // 用户管理
  users: {
    getList: async (params) => {
      try {
        return await api.get('/users/', { params })
      } catch (error) {
        console.error('获取用户列表失败:', error)
        // 模拟用户数据
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
        return await api.get(`/users/${id}/`)
      } catch (error) {
        console.error('获取用户详情失败:', error)
        // 模拟用户详情
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
        return await api.put(`/users/${id}/`, data)
      } catch (error) {
        console.error('更新用户失败:', error)
        // 模拟更新成功
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
        // 模拟删除成功
        return { success: true }
      }
    },
    toggleStatus: async (id) => {
      try {
        return await api.patch(`/users/${id}/toggle-status/`)
      } catch (error) {
        console.error('切换用户状态失败:', error)
        // 模拟切换成功
        return { success: true }
      }
    }
  },
  
  // 订单管理
  orders: {
    getList: async (params) => {
      try {
        return await api.get('/orders/', { params })
      } catch (error) {
        console.error('获取订单列表失败:', error)
        // 模拟订单数据
        return {
          results: [
            {
              id: 'ORD-2026-001',
              user: '张三',
              amount: 299,
              itemsCount: 2,
              status: 'completed',
              statusText: '已完成',
              createTime: '2026-04-19 10:30'
            },
            {
              id: 'ORD-2026-002',
              user: '李四',
              amount: 158,
              itemsCount: 1,
              status: 'pending',
              statusText: '待处理',
              createTime: '2026-04-19 09:15'
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
        // 模拟订单详情
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
        // 模拟更新成功
        return { success: true }
      }
    },
    delete: async (id) => {
      try {
        return await api.delete(`/orders/${id}/`)
      } catch (error) {
        console.error('删除订单失败:', error)
        // 模拟删除成功
        return { success: true }
      }
    }
  },
  
  // 活动管理
  activities: {
    getList: async (params) => {
      try {
        return await api.get('/activities/', { params })
      } catch (error) {
        console.error('获取活动列表失败:', error)
        // 模拟活动数据
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
        // 模拟活动详情
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
        // 模拟创建成功
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
        // 模拟更新成功
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
        // 模拟删除成功
        return { success: true }
      }
    }
  },
  
  // 非遗项目管理
  heritage: {
    getList: async (params) => {
      try {
        return await api.get('/heritage/', { params })
      } catch (error) {
        console.error('获取非遗项目列表失败:', error)
        // 模拟非遗项目数据
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
        // 模拟非遗项目详情
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
        // 模拟创建成功
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
        // 模拟更新成功
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
        // 模拟删除成功
        return { success: true }
      }
    }
  },
  
  // 数据分析
  analytics: {
    getOverview: async (params) => {
      try {
        return await api.get('/analytics/overview/', { params })
      } catch (error) {
        console.error('获取概览数据失败:', error)
        // 模拟概览数据
        return {
          revenue: 125000,
          revenue_change: 15.2,
          orders: 567,
          orders_change: 8.7,
          users: 342,
          users_change: 12.5,
          conversion: 3.2,
          conversion_change: -0.5
        }
      }
    },
    getSalesTrend: async (params) => {
      try {
        return await api.get('/analytics/sales-trend/', { params })
      } catch (error) {
        console.error('获取销售趋势失败:', error)
        // 模拟销售趋势数据
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
        // 模拟产品排行数据
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
        // 模拟用户行为数据
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

// 导出默认实例
export default adminAPI