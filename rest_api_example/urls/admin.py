# third party modules
from django.conf.urls import include, url
from django.contrib import admin

# url specification
urlpatterns = [
    url(r'^', include(admin.site.urls)),
]
