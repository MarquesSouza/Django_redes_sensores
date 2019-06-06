from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('station', views.StationView)
router.register('metric', views.MetricView)
router.register('device', views.DeviceView)
router.register('contributor', views.ContributorView)
router.register('measure', views.MeasureView)
urlpatterns = [
    path('api/',include(router.urls)),
    path('', views.index),
    path('graphics', views.graphics),
    path('maps', views.maps),

]
