from rest_framework.routers import DefaultRouter

from apps.lease.views import LeaseViewSet

router = DefaultRouter()
router.register("", LeaseViewSet, basename="lease")
urlpatterns = router.urls

