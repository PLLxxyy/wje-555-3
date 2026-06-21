import uuid

from django.db import models

from apps.common.constants import BillStatus, BillType


class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lease = models.ForeignKey("lease.Lease", on_delete=models.CASCADE, related_name="bills")
    type = models.CharField(max_length=20, choices=BillType.choices)
    title = models.CharField(max_length=180)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    dueDate = models.DateField()
    paidDate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=BillStatus.choices, default=BillStatus.PENDING)
    remark = models.CharField(max_length=255, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-createdAt"]

    def __str__(self):
        return self.title

