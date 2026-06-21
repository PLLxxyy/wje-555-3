import { request } from './request'
import type { Paginated } from '@/types/api'
import type { RepairOrder } from '@/types/repair'

export const repairApi = {
  list: () => request.get<unknown, Paginated<RepairOrder>>('/repairs/'),
  create: (data: Record<string, unknown>) => request.post<unknown, RepairOrder>('/repairs/', data),
  assign: (id: string, assignedTo: string) => request.patch<unknown, RepairOrder>(`/repairs/${id}/assign/`, { assignedTo }),
  progress: (id: string) => request.patch<unknown, RepairOrder>(`/repairs/${id}/progress/`),
  complete: (id: string, resolvedNote: string) => request.patch<unknown, RepairOrder>(`/repairs/${id}/complete/`, { resolvedNote }),
}

