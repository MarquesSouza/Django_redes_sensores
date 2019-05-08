from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api/station', views.StationView)
router.register('api/metric', views.MetricView)
router.register('api/device', views.DeviceView)
router.register('api/contributor', views.ContributorView)
router.register('api/measure', views.MeasureView)
urlpatterns = [
    path('',include(router.urls))
]
