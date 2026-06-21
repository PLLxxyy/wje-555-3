from rest_framework import serializers

from apps.audit.models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):
    actorName = serializers.CharField(source="actor.username", read_only=True)

    class Meta:
        model = AuditLog
        fields = ["id", "actor", "actorName", "action", "entityType", "entityId", "oldValue", "newValue", "ipAddress", "createdAt"]

