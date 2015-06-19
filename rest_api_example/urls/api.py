from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
  url(r'^', include('api.urls', namespace="api")),
  url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
)
