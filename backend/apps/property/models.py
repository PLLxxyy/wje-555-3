import uuid

from django.conf import settings
from django.db import models

from apps.common.constants import PropertyStatus, PropertyType


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=180)
    type = models.CharField(max_length=20, choices=PropertyType.choices)
    address = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.CharField(max_length=80)
    floor = models.IntegerField()
    totalFloors = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    deposit = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=PropertyStatus.choices, default=PropertyStatus.AVAILABLE)
    landlord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="properties")
    images = models.JSONField(default=list, blank=True)
    facilities = models.JSONField(default=list, blank=True)
    description = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-createdAt"]

    def __str__(self):
        return self.title

