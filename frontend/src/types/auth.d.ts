import type { UserRole } from '@/constants/enums'

export interface User {
  id: string
  username: string
  role: UserRole
  nickname: string
  phone: string
  email: string
  avatar: string
  idCardNo: string
  createdAt: string
}

