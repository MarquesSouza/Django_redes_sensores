from django.shortcuts import render
from rest_framework import viewsets
from .models import Metric
from .models import Device
from .models import Contributor
from .models import Station
from .models import Measure
from .serializers import MetricSerializer
from .serializers import DeviceSerializer
from .serializers import ContributorSerializer
from .serializers import StationSerializer
from .serializers import MeasureSerializer

class MetricView(viewsets.ModelViewSet):
   queryset = Metric.objects.all()
   serializer_class = MetricSerializer
class StationView(viewsets.ModelViewSet):
   queryset = Station.objects.all()
   serializer_class = StationSerializer
class DeviceView(viewsets.ModelViewSet):
   queryset = Device.objects.all()
   serializer_class = DeviceSerializer
class ContributorView(viewsets.ModelViewSet):
   queryset = Contributor.objects.all()
   serializer_class = ContributorSerializer
class MeasureView(viewsets.ModelViewSet):
   queryset = Measure.objects.all()
   serializer_class = MeasureSerializer


