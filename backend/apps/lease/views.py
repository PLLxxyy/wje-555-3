from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.audit.mixins import AuditMixin
from apps.common.constants import LeaseStatus, UserRole
from apps.common.permissions import IsLandlord
from apps.lease.models import Lease
from apps.lease.serializers import LeaseDetailSerializer, LeaseSerializer
from apps.lease.services import refresh_lease_status
from apps.property.models import Property


class LeaseViewSet(AuditMixin, viewsets.ModelViewSet):
    queryset = Lease.objects.select_related("property", "tenant", "landlord").prefetch_related("bills").all()
    serializer_class = LeaseSerializer
    audit_entity_type = "lease"

    def get_permissions(self):
        if self.action in ["create", "renew"]:
            return [permissions.IsAuthenticated(), IsLandlord()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        return LeaseDetailSerializer if self.action == "retrieve" else LeaseSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["property_model"] = Property
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.role == UserRole.LANDLORD:
            queryset = queryset.filter(landlord=user)
        elif user.role == UserRole.TENANT:
            queryset = queryset.filter(tenant=user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        lease = refresh_lease_status(self.get_object())
        return Response(self.get_serializer(lease).data)

    @action(detail=True, methods=["post"])
    def sign(self, request, pk=None):
        lease = self.get_object()
        if request.user == lease.landlord:
            lease.landlordSigned = True
        if request.user == lease.tenant:
            lease.tenantSigned = True
        if lease.landlordSigned and lease.tenantSigned:
            lease.status = LeaseStatus.ACTIVE
        lease.save()
        self.record_audit(request, "lease.sign", lease, {}, {"status": lease.status})
        return Response(LeaseSerializer(lease).data)

    @action(detail=True, methods=["post"])
    def renew(self, request, pk=None):
        old = self.get_object()
        old.status = LeaseStatus.TERMINATED
        old.terminationReason = "续签生成新租约"
        old.save()
        serializer = LeaseSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        new_lease = serializer.save()
        self.record_audit(request, "lease.renew", new_lease, {"oldLease": str(old.id)}, {"newLease": str(new_lease.id)})
        return Response(LeaseSerializer(new_lease).data, status=201)

    @action(detail=True, methods=["post"])
    def terminate(self, request, pk=None):
        lease = self.get_object()
        lease.status = LeaseStatus.TERMINATED
        lease.terminationReason = request.data.get("terminationReason", "提前终止")
        lease.save()
        self.record_audit(request, "lease.terminate", lease, {}, {"reason": lease.terminationReason})
        return Response(LeaseSerializer(lease).data)

