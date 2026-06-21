import { request } from './request'
import type { Paginated } from '@/types/api'
import type { Property } from '@/types/property'

export const propertyApi = {
  list: (params?: Record<string, unknown>) => request.get<unknown, Paginated<Property>>('/properties/', { params }),
  detail: (id: string) => request.get<unknown, Property>(`/properties/${id}/`),
  create: (data: Record<string, unknown>) => request.post<unknown, Property>('/properties/', data),
  update: (id: string, data: Record<string, unknown>) => request.put<unknown, Property>(`/properties/${id}/`, data),
  setStatus: (id: string, status: string) => request.patch<unknown, Property>(`/properties/${id}/status/`, { status }),
  remove: (id: string) => request.delete(`/properties/${id}/`),
}
