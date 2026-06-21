from rest_framework import serializers

from apps.property.models import Property


class PropertySerializer(serializers.ModelSerializer):
    landlordId = serializers.UUIDField(source="landlord.id", read_only=True)
    landlordName = serializers.CharField(source="landlord.nickname", read_only=True)

    class Meta:
        model = Property
        fields = [
            "id", "title", "type", "address", "area", "rooms", "floor", "totalFloors",
            "price", "deposit", "status", "landlordId", "landlordName", "images",
            "facilities", "description", "latitude", "longitude", "createdAt", "updatedAt",
        ]
        read_only_fields = ["id", "landlordId", "landlordName", "createdAt", "updatedAt"]


class PropertyDetailSerializer(PropertySerializer):
    pass

