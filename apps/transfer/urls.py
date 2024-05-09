from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.transfer.views import HistoryTransferAPIViewSet

router = DefaultRouter()
router.register('history_transfer', HistoryTransferAPIViewSet, basename='api_history_transfer')

urlpatterns = router.urls