from rest_framework.routers import DefaultRouter

from apps.repair.views import RepairOrderViewSet

router = DefaultRouter()
router.register("", RepairOrderViewSet, basename="repair")
urlpatterns = router.urls

