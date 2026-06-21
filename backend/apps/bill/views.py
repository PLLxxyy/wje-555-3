from django.db.models import Sum
from django.utils import timezone
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.audit.mixins import AuditMixin
from apps.bill.models import Bill
from apps.bill.serializers import BillSerializer
from apps.bill.services import mark_overdue_bills
from apps.common.constants import BillStatus, UserRole
from apps.common.permissions import IsLandlord
from apps.lease.models import Lease


class BillViewSet(AuditMixin, viewsets.ModelViewSet):
    queryset = Bill.objects.select_related("lease", "lease__property", "lease__tenant", "lease__landlord").all()
    serializer_class = BillSerializer
    audit_entity_type = "bill"

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated(), IsLandlord()]
        return [permissions.IsAuthenticated()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["lease_model"] = Lease
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        mark_overdue_bills(queryset)
        user = self.request.user
        if user.role == UserRole.LANDLORD:
            queryset = queryset.filter(lease__landlord=user)
        elif user.role == UserRole.TENANT:
            queryset = queryset.filter(lease__tenant=user)
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @action(detail=True, methods=["post"])
    def pay(self, request, pk=None):
        bill = self.get_object()
        bill.status = BillStatus.PAID
        bill.paidDate = timezone.localdate()
        bill.save(update_fields=["status", "paidDate"])
        self.record_audit(request, "bill.pay", bill, {}, {"status": bill.status})
        return Response(BillSerializer(bill).data)

    @action(detail=True, methods=["post"])
    def urge(self, request, pk=None):
        bill = self.get_object()
        self.record_audit(request, "bill.urge", bill, {}, {"message": "已发送催缴提醒"})
        return Response({"message": "已发送催缴提醒", "billId": str(bill.id)})

    @action(detail=True, methods=["post"])
    def waive(self, request, pk=None):
        bill = self.get_object()
        old_amount = str(bill.amount)
        if request.data.get("amount"):
            bill.amount = request.data["amount"]
        else:
            bill.status = BillStatus.WAIVED
        bill.remark = request.data.get("remark", bill.remark)
        bill.save()
        self.record_audit(request, "bill.waive", bill, {"amount": old_amount}, {"amount": str(bill.amount), "status": bill.status})
        return Response(BillSerializer(bill).data)

    @action(detail=False, methods=["get"])
    def stats(self, request):
        queryset = self.get_queryset()
        return Response({
            "pendingTotal": queryset.filter(status=BillStatus.PENDING).aggregate(total=Sum("amount"))["total"] or 0,
            "paidTotal": queryset.filter(status=BillStatus.PAID).aggregate(total=Sum("amount"))["total"] or 0,
            "overdueTotal": queryset.filter(status=BillStatus.OVERDUE).aggregate(total=Sum("amount"))["total"] or 0,
        })

