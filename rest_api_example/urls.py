# third party modules
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', UserView.UserViewSet)
# router.register(r'snippets', SnippetView.SnippetList.as_view())
# router.register(r'snippets', SnippetView.SnippetDetail.as_view())

# url specification
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('api.urls', namespace="api")),
]
