from django.shortcuts import render
from rest_framework import viewsets
from sensors.models import Sensor
from core.models import Device
from .serializers import SensorSerializer, DeviceSerializer

# Create your views here.


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
