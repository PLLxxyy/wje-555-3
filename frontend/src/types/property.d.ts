import type { PropertyStatus, PropertyType } from '@/constants/enums'

export interface Property {
  id: string
  title: string
  type: PropertyType
  address: string
  area: string
  rooms: string
  floor: number
  totalFloors: number
  price: string
  deposit: string
  status: PropertyStatus
  landlordId: string
  landlordName: string
  images: string[]
  facilities: string[]
  description: string
  latitude: string
  longitude: string
  createdAt: string
  updatedAt: string
}

