from django.conf.urls import include, url
from api.v1.users import views as UserView
from api.v1.snippets import views as SnippetView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserView.UserViewSet)
router.register(r'snippets', SnippetView.SnippetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]