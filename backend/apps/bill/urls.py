from rest_framework.routers import DefaultRouter

from apps.bill.views import BillViewSet

router = DefaultRouter()
router.register("", BillViewSet, basename="bill")
urlpatterns = router.urls

