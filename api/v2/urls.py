from django.conf.urls import *
from snippets.views import SnippetViewSet
from users.views import UserViewSet
from garments.views import GarmentViewSet
from patterns.views import PatternViewSet
from test1.views import Test1ViewSet
from test2.views import Test2ViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetViewSet)
router.register(r'garments', GarmentViewSet)
router.register(r'patterns', PatternViewSet)
router.register(r'test1', Test1ViewSet)
router.register(r'test2', Test2ViewSet)

urlpatterns = router.urls

urlpatterns += patterns('',
  # default version needs to be always the most recent API urls 
  url(r'', include('api.v2.users.urls')),
  url(r'', include('api.v2.garments.urls')),
)