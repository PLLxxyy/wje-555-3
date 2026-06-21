from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.bill.models import Bill
from apps.common.constants import BillStatus, BillType, LeaseStatus, PaymentCycle, PropertyStatus, PropertyType, RepairPriority
from apps.lease.models import Lease
from apps.property.models import Property
from apps.repair.models import RepairOrder


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        landlord, _ = User.objects.get_or_create(username="landlord", defaults={"role": "LANDLORD", "nickname": "陆房东", "phone": "13800000001"})
        tenant, _ = User.objects.get_or_create(username="tenant", defaults={"role": "TENANT", "nickname": "唐租客", "phone": "13800000002"})
        admin, _ = User.objects.get_or_create(username="admin", defaults={"role": "ADMIN", "nickname": "平台管理员", "is_staff": True, "is_superuser": True})
        for user in [landlord, tenant, admin]:
            user.set_password("renthub123")
            user.save()

        prop, _ = Property.objects.get_or_create(
            title="滨江花园 2室1厅 南向",
            landlord=landlord,
            defaults={
                "type": PropertyType.WHOLE,
                "address": "杭州市滨江区春晓路 88 号",
                "area": Decimal("86.50"),
                "rooms": "2室1厅1卫",
                "floor": 12,
                "totalFloors": 28,
                "price": Decimal("5200.00"),
                "deposit": Decimal("5200.00"),
                "status": PropertyStatus.RENTED,
                "images": ["https://images.unsplash.com/photo-1505693416388-ac5ce068fe85"],
                "facilities": ["空调", "洗衣机", "冰箱", "宽带", "热水器"],
                "description": "近地铁、采光好、可拎包入住。",
                "latitude": Decimal("30.208400"),
                "longitude": Decimal("120.212000"),
            },
        )
        lease, _ = Lease.objects.get_or_create(
            property=prop,
            tenant=tenant,
            landlord=landlord,
            defaults={
                "startDate": date.today() - timedelta(days=20),
                "endDate": date.today() + timedelta(days=340),
                "monthlyRent": prop.price,
                "deposit": prop.deposit,
                "paymentCycle": PaymentCycle.MONTHLY,
                "status": LeaseStatus.ACTIVE,
                "landlordSigned": True,
                "tenantSigned": True,
            },
        )
        Bill.objects.get_or_create(lease=lease, type=BillType.RENT, title="本月房租", defaults={"amount": prop.price, "dueDate": date.today() + timedelta(days=5), "status": BillStatus.PENDING})
        Bill.objects.get_or_create(lease=lease, type=BillType.UTILITY, title="水电费", defaults={"amount": Decimal("286.50"), "dueDate": date.today() - timedelta(days=3), "status": BillStatus.OVERDUE})
        RepairOrder.objects.get_or_create(property=prop, tenant=tenant, title="厨房水龙头漏水", defaults={"description": "水龙头关闭后仍持续滴水。", "priority": RepairPriority.HIGH})
        self.stdout.write(self.style.SUCCESS("Demo data ready: landlord/tenant/admin password renthub123"))

