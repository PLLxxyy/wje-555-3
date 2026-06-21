from datetime import timedelta

from django.utils import timezone

from apps.bill.models import Bill
from apps.common.constants import BillStatus, BillType, PaymentCycle


def mark_overdue_bills(queryset=None):
    queryset = queryset or Bill.objects.all()
    return queryset.filter(status=BillStatus.PENDING, dueDate__lt=timezone.localdate()).update(status=BillStatus.OVERDUE)


def generate_rent_bills(lease):
    months = {PaymentCycle.MONTHLY: 1, PaymentCycle.QUARTERLY: 3, PaymentCycle.YEARLY: 12}[lease.paymentCycle]
    Bill.objects.get_or_create(
        lease=lease,
        type=BillType.RENT,
        dueDate=lease.startDate + timedelta(days=30 * months),
        defaults={"title": f"{lease.property.title} 房租账单", "amount": lease.monthlyRent * months},
    )

