from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
  url(r'^', include('api.urls', namespace="api")),
  url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
  url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
)
