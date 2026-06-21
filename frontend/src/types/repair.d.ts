import type { RepairPriority, RepairStatus } from '@/constants/enums'

export interface RepairOrder {
  id: string
  propertyId: string
  propertyTitle: string
  tenantId: string
  title: string
  description: string
  images: string[]
  priority: RepairPriority
  status: RepairStatus
  assignedTo: string
  resolvedAt: string | null
  resolvedNote: string
}

