from django.conf.urls import *
from .views import UserViewSet
from rest_framework.routers import DefaultRouter


# [TODO] - needs to move these to user api directory
urlpatterns = [
  url(r'^users/(?P<pk>[0-9]+)/relationships/$', UserViewSet.as_view({'get':'relationships'}), name="relationships"),
  url(r'^users/(?P<pk>[0-9]+)/relationships/snippets/$', UserViewSet.as_view({'get':'snippet_relationships'}), name="snippet_relationships"),
  url(r'^users/(?P<pk>[0-9]+)/snippets/$', UserViewSet.as_view({'get':'snippet_included'}), name="snippet_included"),
]