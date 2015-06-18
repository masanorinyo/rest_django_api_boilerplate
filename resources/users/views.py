# import logging
# logger = logging.getLogger(__name__)


# class ApiViewSet(viewsets.ReadOnlyModelViewSet):
#   """
#   This viewset automatically provides `list` and `detail` actions.
#   """
#   if self.request.version == 'v1':
#     from resources.users.api.v1 import UserViewSet
#   elif self.request.version == 'v2':
#     from resources.users.api.v2 import UserViewSet
#   else: 
#     from resources.users.api.v1 import UserViewSet
from django.contrib.auth.models import User 
from .serializers import UserSerializer
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route

class UserViewSet(viewsets.ReadOnlyModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer