from django.conf.urls import *
from snippets.views import SnippetViewSet
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetViewSet)

urlpatterns = router.urls

urlpatterns += patterns('',
  # default version needs to be always the most recent API urls 
  url(r'', include('api.v2.users.urls')),
)