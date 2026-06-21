from django.utils import timezone
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.audit.mixins import AuditMixin
from apps.common.constants import RepairStatus, UserRole
from apps.repair.models import RepairOrder
from apps.repair.serializers import RepairOrderSerializer


class RepairOrderViewSet(AuditMixin, viewsets.ModelViewSet):
    queryset = RepairOrder.objects.select_related("property", "property__landlord", "tenant").all()
    serializer_class = RepairOrderSerializer
    audit_entity_type = "repair"

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.role == UserRole.LANDLORD:
            queryset = queryset.filter(property__landlord=user)
        elif user.role == UserRole.TENANT:
            queryset = queryset.filter(tenant=user)
        return queryset

    def get_permissions(self):
        return [permissions.IsAuthenticated()]

    @action(detail=True, methods=["patch"])
    def assign(self, request, pk=None):
        repair = self.get_object()
        repair.assignedTo = request.data.get("assignedTo", repair.assignedTo)
        repair.status = RepairStatus.ASSIGNED
        repair.save()
        self.record_audit(request, "repair.assign", repair, {}, {"assignedTo": repair.assignedTo})
        return Response(RepairOrderSerializer(repair).data)

    @action(detail=True, methods=["patch"])
    def progress(self, request, pk=None):
        repair = self.get_object()
        repair.status = RepairStatus.IN_PROGRESS
        repair.save(update_fields=["status", "updatedAt"])
        self.record_audit(request, "repair.progress", repair, {}, {"status": repair.status})
        return Response(RepairOrderSerializer(repair).data)

    @action(detail=True, methods=["patch"])
    def complete(self, request, pk=None):
        repair = self.get_object()
        repair.status = RepairStatus.COMPLETED
        repair.resolvedNote = request.data.get("resolvedNote", repair.resolvedNote)
        repair.resolvedAt = timezone.now()
        repair.save()
        self.record_audit(request, "repair.complete", repair, {}, {"status": repair.status})
        return Response(RepairOrderSerializer(repair).data)

