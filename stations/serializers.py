from rest_framework import serializers
from .models import Metric
from .models import Device
from .models import Contributor
from .models import Station
from .models import Measure

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model= Metric
        fields = ('id','name','unit','description')
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Device
        fields = ('id','name','description','status')
class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contributor
        fields = ('id','name','email','site','logo','telefone')
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Station
        fields = ('id','name','description','location','latitude','status','contributors_id')
class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model= Measure
        fields = ('date','station_id','metric_id','device_id','measure')
