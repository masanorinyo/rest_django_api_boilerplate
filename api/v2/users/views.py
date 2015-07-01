from django.contrib.auth.models import User 
from .serializers import UserSerializer
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route

class UserViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def perform_create(self, serializer):
      serializer.save(user=self.request.user)