from rest_framework.permissions import BasePermission

from apps.common.constants import UserRole


class IsLandlord(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == UserRole.LANDLORD)


class IsTenant(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == UserRole.TENANT)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == UserRole.ADMIN)


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRole.ADMIN:
            return True
        for attr in ("landlord", "tenant", "user"):
            if hasattr(obj, attr) and getattr(obj, attr) == request.user:
                return True
        if hasattr(obj, "lease"):
            return obj.lease.landlord == request.user or obj.lease.tenant == request.user
        return False

