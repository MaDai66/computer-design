import api from './axios'

export const userAPI = {
  register: (userData) => api.post('/users/register/', userData),
  login: (credentials) => api.post('/users/login/', credentials),
  logout: () => api.post('/users/logout/'),
  getProfile: () => api.get('/users/profile/'),
  updateProfile: (userData) => api.put('/users/profile/', userData),
  getAllUsers: () => api.get('/users/'),
  getUserById: (id) => api.get(`/users/${id}/`),
  updateUser: (id, userData) => api.put(`/users/${id}/`, userData),
  deleteUser: (id) => api.delete(`/users/${id}/`),
  toggleUserStatus: (id) => api.post(`/users/${id}/toggle-status/`)
}
