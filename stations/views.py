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
   query = "SELECT measure,strftime('%Y %m %d %H %M %S',date) as date from stations_measure where metric_id=5 order by date desc"
   cursor.execute(query)
   result = cursor.fetchall()
   da={}
   me={}
   count=0
   for  measure,date in result :
      da[count] = date
      me[count] = measure
      count=count+1
   data['date']=da
   data['measure']=me
   data['count']= count
   return render(request,'index.html',data)