from django.db import models


class UserRole(models.TextChoices):
    LANDLORD = "LANDLORD", "房东"
    TENANT = "TENANT", "租客"
    ADMIN = "ADMIN", "管理员"


class PropertyType(models.TextChoices):
    WHOLE = "WHOLE", "整租"
    SHARED = "SHARED", "合租"
    COMMERCIAL = "COMMERCIAL", "商铺"


class LeaseStatus(models.TextChoices):
    PENDING = "PENDING", "待签"
    ACTIVE = "ACTIVE", "生效"
    EXPIRING_SOON = "EXPIRING_SOON", "即将到期"
    EXPIRED = "EXPIRED", "已到期"
    TERMINATED = "TERMINATED", "已终止"


class BillType(models.TextChoices):
    RENT = "RENT", "房租"
    UTILITY = "UTILITY", "水电"
    MAINTENANCE = "MAINTENANCE", "维修"
    PROPERTY = "PROPERTY", "物业"
    PENALTY = "PENALTY", "违约金"


class BillStatus(models.TextChoices):
    PENDING = "PENDING", "待付"
    PAID = "PAID", "已付"
    OVERDUE = "OVERDUE", "逾期"
    WAIVED = "WAIVED", "已减免"


class RepairPriority(models.TextChoices):
    LOW = "LOW", "低"
    MEDIUM = "MEDIUM", "中"
    HIGH = "HIGH", "高"
    URGENT = "URGENT", "紧急"


class PropertyStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", "待租"
    RENTED = "RENTED", "已租"
    MAINTENANCE = "MAINTENANCE", "维护中"


class PaymentCycle(models.TextChoices):
    MONTHLY = "MONTHLY", "月付"
    QUARTERLY = "QUARTERLY", "季付"
    YEARLY = "YEARLY", "年付"


class RepairStatus(models.TextChoices):
    PENDING = "PENDING", "待处理"
    ASSIGNED = "ASSIGNED", "已派单"
    IN_PROGRESS = "IN_PROGRESS", "维修中"
    COMPLETED = "COMPLETED", "已完成"

