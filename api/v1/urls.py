# third party modules
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter

# # custom modules 
from .users import views as UserView
from .snippets import views as SnippetView

router_v1 = DefaultRouter()
router_v1.register(r'users', UserView.UserViewSet)
router_v1.register(r'snippets', SnippetView.SnippetViewSet)

# url specification
urlpatterns = router_v1.urls