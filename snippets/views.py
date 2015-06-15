from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from snippets.models import Snippet
from django.contrib.auth.models import User 
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response

@api_view(('GET',))
def api_root(request, format=None):
  return Response({
      'users': reverse('user-list', request=request, format=format),
      'snippets': reverse('snippet-list', request=request, format=format)
  })


class SnippetHighlight(generics.GenericAPIView):
  """
  returns html template with content in it
  """
  queryset = Snippet.objects.all()
  renderer_classes = (renderers.StaticHTMLRenderer,)

  def get(self, request, *args, **kwargs):
      snippet = self.get_object()
      return Response(snippet.highlighted)




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

# The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrieve, update or delete a code snippet.
  """
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)