from datetime import timedelta

from django.utils import timezone

from apps.common.constants import LeaseStatus


def refresh_lease_status(lease):
    today = timezone.localdate()
    if lease.status in [LeaseStatus.TERMINATED, LeaseStatus.PENDING]:
        return lease
    if lease.endDate < today:
        lease.status = LeaseStatus.EXPIRED
    elif lease.endDate <= today + timedelta(days=30):
        lease.status = LeaseStatus.EXPIRING_SOON
    lease.save(update_fields=["status", "updatedAt"])
    return lease

