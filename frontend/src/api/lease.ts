import { request } from './request'
import type { Paginated } from '@/types/api'
import type { Lease } from '@/types/lease'

export const leaseApi = {
  list: () => request.get<unknown, Paginated<Lease>>('/leases/'),
  detail: (id: string) => request.get<unknown, Lease>(`/leases/${id}/`),
  create: (data: Record<string, unknown>) => request.post<unknown, Lease>('/leases/', data),
  sign: (id: string) => request.post<unknown, Lease>(`/leases/${id}/sign/`),
  renew: (id: string, data: Record<string, unknown>) => request.post<unknown, Lease>(`/leases/${id}/renew/`, data),
  terminate: (id: string, terminationReason: string) => request.post<unknown, Lease>(`/leases/${id}/terminate/`, { terminationReason }),
}

