import axios from 'axios'
import { ElMessage } from 'element-plus'
import { storage } from '@/utils/storage'

export const request = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/api',
  timeout: 10000,
})

request.interceptors.request.use((config) => {
  const token = storage.getToken()
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

request.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const status = error.response?.status
    const message = error.response?.data?.message || error.response?.data?.detail || '请求失败'
    if (status === 401) {
      storage.clearToken()
      location.href = '/login'
    }
    ElMessage.error(message)
    return Promise.reject(error)
  },
)

