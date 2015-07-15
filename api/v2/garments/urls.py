from django.conf.urls import *
from .views import GarmentViewSet
from rest_framework.routers import DefaultRouter


# [TODO] - needs to move these to user api directory
urlpatterns = [
  url(r'^garments/(?P<pk>[0-9]+)/relationships/$', GarmentViewSet.as_view({'get':'relationships'}), name="relationships"),
  url(r'^garments/(?P<pk>[0-9]+)/relationships/patterns/$', GarmentViewSet.as_view({'get':'pattern_relationships'}), name="pattern_relationships"),
  url(r'^garments/(?P<pk>[0-9]+)/patterns/$', GarmentViewSet.as_view({'get':'pattern_included'}), name="pattern_included"),
]