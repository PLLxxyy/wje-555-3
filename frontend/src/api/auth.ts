import { request } from './request'
import type { User } from '@/types/auth'

export const authApi = {
  register: (data: Record<string, unknown>) => request.post<unknown, { user: User }>('/auth/register', data),
  login: (data: { username: string; password: string }) => request.post<unknown, { token: string; user: User }>('/auth/login', data),
  profile: () => request.get<unknown, User>('/auth/profile'),
  updateProfile: (data: Partial<User>) => request.put<unknown, User>('/auth/profile', data),
}

