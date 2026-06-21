from rest_framework import serializers

from apps.property.models import Property
from apps.repair.models import RepairOrder


class RepairOrderSerializer(serializers.ModelSerializer):
    propertyId = serializers.UUIDField(source="property.id", read_only=True)
    property_id = serializers.UUIDField(write_only=True, required=False)
    tenantId = serializers.UUIDField(source="tenant.id", read_only=True)
    propertyTitle = serializers.CharField(source="property.title", read_only=True)

    class Meta:
        model = RepairOrder
        fields = [
            "id", "propertyId", "property_id", "propertyTitle", "tenantId", "title", "description",
            "images", "priority", "status", "assignedTo", "resolvedAt", "resolvedNote", "createdAt", "updatedAt",
        ]
        read_only_fields = ["id", "propertyId", "tenantId", "status", "resolvedAt", "createdAt", "updatedAt"]

    def create(self, validated_data):
        property_id = validated_data.pop("property_id")
        prop = Property.objects.get(id=property_id)
        return RepairOrder.objects.create(property=prop, tenant=self.context["request"].user, **validated_data)

