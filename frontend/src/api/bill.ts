import { request } from './request'
import type { Paginated } from '@/types/api'
import type { Bill } from '@/types/bill'

export const billApi = {
  list: (params?: Record<string, unknown>) => request.get<unknown, Paginated<Bill>>('/bills/', { params }),
  create: (data: Record<string, unknown>) => request.post<unknown, Bill>('/bills/', data),
  pay: (id: string) => request.post<unknown, Bill>(`/bills/${id}/pay/`),
  urge: (id: string) => request.post<unknown, { message: string }>(`/bills/${id}/urge/`),
  waive: (id: string, data: Record<string, unknown>) => request.post<unknown, Bill>(`/bills/${id}/waive/`, data),
  stats: () => request.get<unknown, { pendingTotal: number; paidTotal: number; overdueTotal: number }>('/bills/stats/'),
}

