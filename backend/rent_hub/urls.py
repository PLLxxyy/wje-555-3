from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    return Response({"status": "ok", "service": "renthub"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health),
    path("api/auth/", include("apps.auth.urls")),
    path("api/properties/", include("apps.property.urls")),
    path("api/leases/", include("apps.lease.urls")),
    path("api/bills/", include("apps.bill.urls")),
    path("api/repairs/", include("apps.repair.urls")),
    path("api/audit-logs/", include("apps.audit.urls")),
]

