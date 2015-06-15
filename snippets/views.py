from snippets.models import Snippet
from django.contrib.auth.models import User 
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class SnippetList(generics.ListCreateAPIView):
  """
  List all code snippets, or create a new snippet.
  """
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer 
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrieve, update or delete a code snippet.
  """
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


def perform_create(self, serializer):
  """
  perform_create() method on our snippet views, that allows us to modify 
  how the instance save is managed, and handle any information that is 
  implicit in the incoming request or requested URL.
  """
  serializer.save(owner=self.request.user)

