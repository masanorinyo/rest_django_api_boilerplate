# from django.contrib.auth.models import User
from rest_api_example.util import *
from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer
# from .api.v1.views import SnippetApi
# from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import mixins
from rest_framework import generics

import pprint

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
      api_version = get_api_version(request.META["HTTP_ACCEPT"])
      if api_version == 'v1':
        return self.list(request, *args, **kwargs)
      elif api_version == 'v2':
        return self.list(request, *args, **kwargs)
      else: 
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
      api_version = get_api_version(request.META["HTTP_ACCEPT"])
      if api_version == 'v1':
        return self.create(request, *args, **kwargs)
      elif api_version == 'v2':
        return self.create(request, *args, **kwargs)
      else: 
        return self.create(request, *args, **kwargs)
        

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
      api_version = get_api_version(request.META["HTTP_ACCEPT"])
      if api_version == 'v1':
        return self.retrieve(request, *args, **kwargs)
      elif api_version == 'v2':
        return self.retrieve(request, *args, **kwargs)
      else: 
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
      api_version = get_api_version(request.META["HTTP_ACCEPT"])
      if api_version == 'v1':
        return self.update(request, *args, **kwargs)
      elif api_version == 'v2':
        return self.update(request, *args, **kwargs)
      else: 
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
      api_version = get_api_version(request.META["HTTP_ACCEPT"])
      if api_version == 'v1':
        return self.destroy(request, *args, **kwargs)
      elif api_version == 'v2':
        return self.destroy(request, *args, **kwargs)
      else: 
        return self.destroy(request, *args, **kwargs)
        
