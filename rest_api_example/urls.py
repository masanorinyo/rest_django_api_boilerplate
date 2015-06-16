from django.conf.urls import include, url
from django.contrib import admin
from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
