from django.contrib import admin
from .models import Metric
from .models import Device
from .models import Contributor
from .models import Station
from .models import Measure


# Register your models here.
admin.site.register(Metric)
admin.site.register(Device)
admin.site.register(Contributor)
admin.site.register(Station)
admin.site.register(Measure)


