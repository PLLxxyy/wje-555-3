from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.common.constants import LeaseStatus, PropertyStatus, UserRole
from apps.lease.models import Lease

User = get_user_model()


class LeaseSerializer(serializers.ModelSerializer):
    propertyTitle = serializers.CharField(source="property.title", read_only=True)
    tenantName = serializers.CharField(source="tenant.nickname", read_only=True)
    landlordName = serializers.CharField(source="landlord.nickname", read_only=True)
    propertyId = serializers.UUIDField(source="property.id", read_only=True)
    tenantId = serializers.UUIDField(source="tenant.id", read_only=True)
    landlordId = serializers.UUIDField(source="landlord.id", read_only=True)
    tenantUserId = serializers.UUIDField(write_only=True)
    property_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Lease
        fields = [
            "id", "propertyId", "property_id", "propertyTitle", "tenantId", "tenantUserId",
            "tenantName", "landlordId", "landlordName", "startDate", "endDate", "monthlyRent",
            "deposit", "paymentCycle", "status", "terminationReason", "landlordSigned",
            "tenantSigned", "createdAt", "updatedAt",
        ]
        read_only_fields = ["id", "status", "createdAt", "updatedAt"]

    def create(self, validated_data):
        property_id = validated_data.pop("property_id")
        tenant_id = validated_data.pop("tenantUserId")
        prop = self.context["property_model"].objects.get(id=property_id, landlord=self.context["request"].user)
        active_exists = prop.leases.filter(status__in=[LeaseStatus.ACTIVE, LeaseStatus.EXPIRING_SOON]).exists()
        if active_exists:
            raise serializers.ValidationError("该房源已有生效租约")
        tenant = User.objects.get(id=tenant_id, role=UserRole.TENANT)
        lease = Lease.objects.create(property=prop, tenant=tenant, landlord=self.context["request"].user, **validated_data)
        prop.status = PropertyStatus.RENTED
        prop.save(update_fields=["status", "updatedAt"])
        return lease


class LeaseDetailSerializer(LeaseSerializer):
    bills = serializers.SerializerMethodField()

    class Meta(LeaseSerializer.Meta):
        fields = LeaseSerializer.Meta.fields + ["bills"]

    def get_bills(self, obj):
        from apps.bill.serializers import BillSerializer

        return BillSerializer(obj.bills.all(), many=True).data

