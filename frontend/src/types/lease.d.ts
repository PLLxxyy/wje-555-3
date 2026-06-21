import type { LeaseStatus, PaymentCycle } from '@/constants/enums'
import type { Bill } from './bill'

export interface Lease {
  id: string
  propertyId: string
  propertyTitle: string
  tenantId: string
  tenantName: string
  landlordId: string
  landlordName: string
  startDate: string
  endDate: string
  monthlyRent: string
  deposit: string
  paymentCycle: PaymentCycle
  status: LeaseStatus
  terminationReason: string
  landlordSigned: boolean
  tenantSigned: boolean
  bills?: Bill[]
}

