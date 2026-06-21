from rest_framework import permissions, viewsets

from apps.audit.models import AuditLog
from apps.audit.serializers import AuditLogSerializer
from apps.common.constants import UserRole


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.select_related("actor").all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        entity_type = self.request.query_params.get("entity_type")
        entity_id = self.request.query_params.get("entity_id")
        if entity_type:
            queryset = queryset.filter(entityType=entity_type)
        if entity_id:
            queryset = queryset.filter(entityId=entity_id)
        if user.role == UserRole.ADMIN:
            return queryset
        return queryset.filter(actor=user)

