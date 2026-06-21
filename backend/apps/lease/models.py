import uuid

from django.conf import settings
from django.db import models

from apps.common.constants import LeaseStatus, PaymentCycle


class Lease(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey("property.Property", on_delete=models.CASCADE, related_name="leases")
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tenant_leases")
    landlord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="landlord_leases")
    startDate = models.DateField()
    endDate = models.DateField()
    monthlyRent = models.DecimalField(max_digits=12, decimal_places=2)
    deposit = models.DecimalField(max_digits=12, decimal_places=2)
    paymentCycle = models.CharField(max_length=20, choices=PaymentCycle.choices, default=PaymentCycle.MONTHLY)
    status = models.CharField(max_length=20, choices=LeaseStatus.choices, default=LeaseStatus.PENDING)
    terminationReason = models.CharField(max_length=255, blank=True)
    landlordSigned = models.BooleanField(default=False)
    tenantSigned = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-createdAt"]

    def __str__(self):
        return f"{self.property.title} - {self.tenant.username}"

