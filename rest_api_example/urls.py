# third party modules
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

# # custom modules 
from resources import views as ApiView
from resources.users import views as UserView
from resources.snippets import views as SnippetView

# router = DefaultRouter()
# router.register(r'users', UserView.UserViewSet)
# router.register(r'snippets', SnippetView.SnippetList.as_view())
# router.register(r'snippets', SnippetView.SnippetDetail.as_view())

# url specification
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', ApiView.api_root),
    url(r'^snippets/$', SnippetView.SnippetList.as_view(), name="snippet-list"),
    url(r'^snippets/$', SnippetView.SnippetDetail.as_view(), name="snippet-detail"),
]
