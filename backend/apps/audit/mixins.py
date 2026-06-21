from apps.audit.models import AuditLog


class AuditMixin:
    audit_entity_type = "entity"

    def record_audit(self, request, action, target, old_value=None, new_value=None):
        AuditLog.objects.create(
            actor=request.user if request.user.is_authenticated else None,
            action=action,
            entityType=self.audit_entity_type,
            entityId=str(target.id),
            oldValue=old_value or {},
            newValue=new_value or {},
            ipAddress=request.META.get("REMOTE_ADDR"),
        )

    def perform_create(self, serializer):
        instance = serializer.save()
        self.record_audit(self.request, f"{self.audit_entity_type}.create", instance, {}, {"id": str(instance.id)})

    def perform_update(self, serializer):
        instance = serializer.save()
        self.record_audit(self.request, f"{self.audit_entity_type}.update", instance, {}, {"id": str(instance.id)})

