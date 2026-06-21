from rest_framework import serializers

from apps.bill.models import Bill


class BillSerializer(serializers.ModelSerializer):
    leaseId = serializers.UUIDField(source="lease.id", read_only=True)
    lease_id = serializers.UUIDField(write_only=True, required=False)
    propertyTitle = serializers.CharField(source="lease.property.title", read_only=True)

    class Meta:
        model = Bill
        fields = [
            "id", "leaseId", "lease_id", "propertyTitle", "type", "title", "amount",
            "dueDate", "paidDate", "status", "remark", "createdAt",
        ]
        read_only_fields = ["id", "leaseId", "propertyTitle", "paidDate", "status", "createdAt"]

    def create(self, validated_data):
        lease_id = validated_data.pop("lease_id")
        lease = self.context["lease_model"].objects.get(id=lease_id, landlord=self.context["request"].user)
        return Bill.objects.create(lease=lease, **validated_data)

