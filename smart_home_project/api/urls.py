from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..api.views import SensorViewSet, DeviceViewSet


router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls))
]

