import uuid

from django.conf import settings
from django.db import models


class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=80)
    entityType = models.CharField(max_length=40)
    entityId = models.CharField(max_length=80)
    oldValue = models.JSONField(default=dict, blank=True)
    newValue = models.JSONField(default=dict, blank=True)
    ipAddress = models.GenericIPAddressField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-createdAt"]

    def __str__(self):
        return f"{self.action} {self.entityType}:{self.entityId}"

