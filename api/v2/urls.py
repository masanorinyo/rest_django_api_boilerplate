from django.conf.urls import *
from users.views import UserViewSet
from snippets.views import SnippetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'snippets', SnippetViewSet)

urlpatterns = router.urls

urlpatterns += [
  url(r'^users/(?P<pk>[0-9]+)/relationships/$', UserViewSet.as_view({'get':'relationships'}), name="relationships"),
  url(r'^users/(?P<pk>[0-9]+)/relationships/snippets/$', UserViewSet.as_view({'get':'snippet_relationships'}), name="snippet_relationships"),
  # url(r'^users/(?P<pk>[0-9]+)/relationships/snippets/$', UserViewSet.as_view({'get':'relationships'}), name="user-relationships"),
]