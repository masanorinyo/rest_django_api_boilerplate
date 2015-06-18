from django.conf.urls import *

urlpatterns = patterns('',
  # default version needs to be always the most recent API urls 
  url(r'', include('api.v2.urls', namespace='default')),
  url(r'^v1/', include('api.v1.urls', namespace='v1')),
  url(r'^v2/', include('api.v2.urls', namespace='v2')),
)