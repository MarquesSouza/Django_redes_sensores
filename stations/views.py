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
   data={}
   menu = {'Pagina Inicial': '/','Mapas': 'maps','Graficos': 'graphics'}
   data['menuactive']='/'
   data['menu'] = menu
   return render(request,'index.html',data)
def maps(request):
   data = {}
   data['menuactive'] = 'maps'
   menu = {'Pagina Inicial': '/', 'Mapas': 'maps', 'Graficos': 'graphics'}
   data['menu'] = menu
   return render(request, 'maps.html', data)
def graphics(request):
   cursor = connection.cursor()
   menu = {'Pagina Inicial': '/', 'Mapas': 'maps', 'Graficos': 'graphics'}
   data={}
   data['menuactive'] = 'graphics'
   data['menu'] = menu
   where={"","","metric_id=3 and device_id=2 and station_id=1","metric_id=4 and device_id=3 and station_id=1","metric_id=5 and device_id=4 and station_id=1","metric_id=6 and device_id=5 and station_id=1"}
   query = "SELECT DISTINCT measure,strftime('%d/%m-%H:%M',date) as date from stations_measure where metric_id=1 and device_id=1 and station_id=1 order by date limit 30 "
   cursor.execute(query)
   result = cursor.fetchall()
   tempdat={}
   tempval={}
   count = 0
   for  measure,date in result :
      tempdat[count] = date
      tempval[count] = measure
      count=count+1
   data['tempdat'] = tempdat
   data['tempval'] = tempval

   query = "SELECT DISTINCT measure,strftime('%d/%m-%H:%M',date) as date from stations_measure where metric_id=2 and device_id=1 and station_id=1 order by date limit 30 "
   cursor.execute(query)
   result = cursor.fetchall()
   umidat = {}
   umival = {}
   count = 0
   for measure, date in result:
      umidat[count] = date
      umival[count] = measure
      count = count + 1

   data['umidat'] = umidat
   data['umival'] = umival

   query = "SELECT DISTINCT measure,strftime('%d/%m-%H:%M',date) as date from stations_measure where metric_id=3 and device_id=2 and station_id=1 order by date limit 30 "
   cursor.execute(query)
   result = cursor.fetchall()
   uvmdat = {}
   uvmval = {}
   count = 0
   for measure, date in result:
      uvmdat[count] = date
      uvmval[count] = measure
      count = count + 1

   data['uvmdat']=uvmdat
   data['uvmval']=uvmval

   query = "SELECT DISTINCT measure,strftime('%d/%m-%H:%M',date) as date from stations_measure where metric_id=4 and device_id=3 and station_id=1 order by date limit 30 "
   cursor.execute(query)
   result = cursor.fetchall()
   pludat = {}
   pluval = {}
   count = 0
   for measure, date in result:
      pludat[count] = date
      pluval[count] = measure
      count = count + 1

   data['pludat']=pludat
   data['pluval']=pluval

   query = "SELECT DISTINCT measure,strftime('%d/%m-%H:%M',date) as date from stations_measure where metric_id=5 and device_id=4 and station_id=1 order by date limit 30 "
   cursor.execute(query)
   result = cursor.fetchall()
   co2dat = {}
   co2val = {}
   count = 0
   for measure, date in result:
      co2dat[count] = date
      co2val[count] = measure
      count = count + 1

   data['co2dat']=co2dat
   data['co2val']=co2val

   query = "SELECT DISTINCT measure,strftime('%d/%m-%H:%M',date) as date from stations_measure where metric_id=6 and device_id=5 and station_id=1 order by date limit 30 "
   cursor.execute(query)
   result = cursor.fetchall()
   toxdat = {}
   toxval = {}
   count = 0
   for measure, date in result:
      toxdat[count] = date
      toxval[count] = measure
      count = count + 1

   data['toxdat']=toxdat
   data['toxval']=toxval
   return render(request,'graphics.html',data)