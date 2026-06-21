import { defineStore } from 'pinia'
import { authApi } from '@/api/auth'
import { storage } from '@/utils/storage'
import type { User } from '@/types/auth'

export const useAuthStore = defineStore('auth', {
  state: () => ({ user: null as User | null, token: storage.getToken() || '' }),
  getters: {
    isLoggedIn: (state) => Boolean(state.token),
    role: (state) => state.user?.role,
  },
  actions: {
    async login(username: string, password: string) {
      const data = await authApi.login({ username, password })
      this.token = data.token
      this.user = data.user
      storage.setToken(data.token)
    },
    async loadProfile() {
      if (!this.token) return
      this.user = await authApi.profile()
    },
    logout() {
      this.token = ''
      this.user = null
      storage.clearToken()
    },
  },
})

