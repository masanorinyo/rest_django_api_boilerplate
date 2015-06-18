from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
  url(r'^', include('api.urls', namespace="api")),
)
