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
   where={"metric_id=1 and device_id=1 and station_id=1","metric_id=2 and device_id=1 and station_id=1","metric_id=3 and device_id=2 and station_id=1","metric_id=4 and device_id=3 and station_id=1","metric_id=5 and device_id=4 and station_id=1","metric_id=6 and device_id=5 and station_id=1"}
   contr=0
   for select in where:
      query = "SELECT measure,strftime('%Y %m %d %H %M %S',date) as date from stations_measure where "+select+" order by date desc limit 30 "
      cursor.execute(query)
      result = cursor.fetchall()
      da={}
      va={}
      count = 0
      for  measure,date in result :
         da[count] = date
         va[count] = measure
         count=count+1
         contr=contr+1
      if contr<=30:
         data['tempdat'] = da
         data['tempval'] = va
      if contr > 30 & contr <= 60:
         data['umidat'] = da
         data['umival'] = va
      if contr>60&contr<=90:
         data['uvmdat']=da
         data['uvmval']=va
      if contr>90&contr<=120:
         data['pludat']=da
         data['pluval']=va
      if contr>120&contr<=150:
         data['co2dat']=da
         data['co2val']=va
      if contr>150&contr<=180:
         data['toxdat']=da
         data['toxval']=va
   #return HttpResponse()
   return render(request,'index.html',data)