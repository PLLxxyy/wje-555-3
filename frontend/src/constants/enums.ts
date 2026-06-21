export enum UserRole {
  LANDLORD = 'LANDLORD',
  TENANT = 'TENANT',
  ADMIN = 'ADMIN',
}

export enum PropertyType {
  WHOLE = 'WHOLE',
  SHARED = 'SHARED',
  COMMERCIAL = 'COMMERCIAL',
}

export enum LeaseStatus {
  PENDING = 'PENDING',
  ACTIVE = 'ACTIVE',
  EXPIRING_SOON = 'EXPIRING_SOON',
  EXPIRED = 'EXPIRED',
  TERMINATED = 'TERMINATED',
}

export enum BillType {
  RENT = 'RENT',
  UTILITY = 'UTILITY',
  MAINTENANCE = 'MAINTENANCE',
  PROPERTY = 'PROPERTY',
}

export enum BillStatus {
  PENDING = 'PENDING',
  PAID = 'PAID',
  OVERDUE = 'OVERDUE',
  WAIVED = 'WAIVED',
}

export enum RepairPriority {
  LOW = 'LOW',
  MEDIUM = 'MEDIUM',
  HIGH = 'HIGH',
  URGENT = 'URGENT',
}

export enum PropertyStatus {
  AVAILABLE = 'AVAILABLE',
  RENTED = 'RENTED',
  MAINTENANCE = 'MAINTENANCE',
}

export enum PaymentCycle {
  MONTHLY = 'MONTHLY',
  QUARTERLY = 'QUARTERLY',
  YEARLY = 'YEARLY',
}

export enum RepairStatus {
  PENDING = 'PENDING',
  ASSIGNED = 'ASSIGNED',
  IN_PROGRESS = 'IN_PROGRESS',
  COMPLETED = 'COMPLETED',
}

export const enumLabels: Record<string, string> = Object.fromEntries([
  [UserRole.LANDLORD, '房东'],
  [UserRole.TENANT, '租客'],
  [UserRole.ADMIN, '管理员'],
  [PropertyType.WHOLE, '整租'],
  [PropertyType.SHARED, '合租'],
  [PropertyType.COMMERCIAL, '商铺'],
  [PropertyStatus.AVAILABLE, '待租'],
  [PropertyStatus.RENTED, '已租'],
  [PropertyStatus.MAINTENANCE, '维护中'],
  [LeaseStatus.PENDING, '待签'],
  [LeaseStatus.ACTIVE, '生效'],
  [LeaseStatus.EXPIRING_SOON, '即将到期'],
  [LeaseStatus.EXPIRED, '已到期'],
  [LeaseStatus.TERMINATED, '已终止'],
  [BillType.RENT, '房租'],
  [BillType.UTILITY, '水电'],
  [BillType.MAINTENANCE, '维修'],
  [BillType.PROPERTY, '物业'],
  [BillStatus.PENDING, '待付'],
  [BillStatus.PAID, '已付'],
  [BillStatus.OVERDUE, '逾期'],
  [BillStatus.WAIVED, '已减免'],
  [RepairPriority.LOW, '低'],
  [RepairPriority.MEDIUM, '中'],
  [RepairPriority.HIGH, '高'],
  [RepairPriority.URGENT, '紧急'],
  [RepairStatus.PENDING, '待处理'],
  [RepairStatus.ASSIGNED, '已派单'],
  [RepairStatus.IN_PROGRESS, '维修中'],
  [RepairStatus.COMPLETED, '已完成'],
  [PaymentCycle.MONTHLY, '月付'],
  [PaymentCycle.QUARTERLY, '季付'],
  [PaymentCycle.YEARLY, '年付'],
])

export const propertyStatusLabels: Record<PropertyStatus, string> = {
  [PropertyStatus.AVAILABLE]: '待租',
  [PropertyStatus.RENTED]: '已租',
  [PropertyStatus.MAINTENANCE]: '维护中',
}

export const leaseStatusLabels: Record<LeaseStatus, string> = {
  [LeaseStatus.PENDING]: '待签',
  [LeaseStatus.ACTIVE]: '生效',
  [LeaseStatus.EXPIRING_SOON]: '即将到期',
  [LeaseStatus.EXPIRED]: '已到期',
  [LeaseStatus.TERMINATED]: '已终止',
}

export const billStatusLabels: Record<BillStatus, string> = {
  [BillStatus.PENDING]: '待付',
  [BillStatus.PAID]: '已付',
  [BillStatus.OVERDUE]: '逾期',
  [BillStatus.WAIVED]: '已减免',
}

export const repairStatusLabels: Record<RepairStatus, string> = {
  [RepairStatus.PENDING]: '待处理',
  [RepairStatus.ASSIGNED]: '已派单',
  [RepairStatus.IN_PROGRESS]: '维修中',
  [RepairStatus.COMPLETED]: '已完成',
}
