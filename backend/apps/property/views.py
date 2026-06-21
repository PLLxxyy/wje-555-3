from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.constants import UserRole
from apps.common.permissions import IsLandlord
from apps.property.filters import apply_property_filters
from apps.property.models import Property
from apps.property.serializers import PropertyDetailSerializer, PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.select_related("landlord").all()
    serializer_class = PropertySerializer

    def get_serializer_class(self):
        return PropertyDetailSerializer if self.action == "retrieve" else PropertySerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy", "status"]:
            return [permissions.IsAuthenticated(), IsLandlord()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queryset = apply_property_filters(super().get_queryset(), self.request.query_params)
        user = self.request.user
        if self.action in ["update", "partial_update", "destroy", "status"] and user.is_authenticated and user.role != UserRole.ADMIN:
            queryset = queryset.filter(landlord=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)

    @action(detail=True, methods=["patch"])
    def status(self, request, pk=None):
        prop = self.get_object()
        prop.status = request.data.get("status", prop.status)
        prop.save(update_fields=["status", "updatedAt"])
        return Response(PropertySerializer(prop).data)

