# third party modules
from django.conf.urls import include, url
from django.contrib import admin

# url specification
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^',include('api.urls', namespace='api')),
]
