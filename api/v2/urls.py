from django.conf.urls import *
from snippets import views as SnippetView
from users import views as UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserView.UserViewSet)
router.register(r'snippets', SnippetView.SnippetViewSet)

urlpatterns = router.urls