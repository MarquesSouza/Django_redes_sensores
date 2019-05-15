import ast
from datetime import datetime
from decimal import Decimal
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth, logout
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

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
def index(request):
   cursor = connection.cursor()
   data = {}
   campos={'date','measure','device_id_id','metric_id_id','station_id_id'}
   for campo in campos:
      query = "select "+campo+" from stations_measure limit 30"
      cursor.execute(query)
      result = cursor.fetchall()
      data[campo]= result
   return render(request,'index.html',data)