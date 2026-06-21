import type { BillStatus, BillType } from '@/constants/enums'

export interface Bill {
  id: string
  leaseId: string
  propertyTitle: string
  type: BillType
  title: string
  amount: string
  dueDate: string
  paidDate: string | null
  status: BillStatus
  remark: string
  createdAt: string
}

