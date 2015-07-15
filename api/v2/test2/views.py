from resources.test2.models import Test2
from .serializers import Test2Serializer
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets

class Test2ViewSet(viewsets.ModelViewSet):
    queryset = Test2.objects.all()
    serializer_class = Test2Serializer

