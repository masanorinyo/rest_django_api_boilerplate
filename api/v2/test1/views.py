from resources.test1.models import Test1
from resources.test2.models import Test2
from .serializers import Test1Serializer
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets

class Test1ViewSet(viewsets.ModelViewSet):
  queryset = Test1.objects.all()
  serializer_class = Test1Serializer

  