import uuid

from django.conf import settings
from django.db import models

from apps.common.constants import RepairPriority, RepairStatus


class RepairOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey("property.Property", on_delete=models.CASCADE, related_name="repairs")
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="repairs")
    title = models.CharField(max_length=180)
    description = models.TextField()
    images = models.JSONField(default=list, blank=True)
    priority = models.CharField(max_length=20, choices=RepairPriority.choices, default=RepairPriority.MEDIUM)
    status = models.CharField(max_length=20, choices=RepairStatus.choices, default=RepairStatus.PENDING)
    assignedTo = models.CharField(max_length=120, blank=True)
    resolvedAt = models.DateTimeField(null=True, blank=True)
    resolvedNote = models.CharField(max_length=255, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-createdAt"]

    def __str__(self):
        return self.title

