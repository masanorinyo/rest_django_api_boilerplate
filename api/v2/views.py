from django.contrib.auth.models import User 
from .serializers import UserSerializer
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RootList(APIView):
  """
  List all snippets, or create a new snippet.
  """
  def get(self, request, format=None):
      snippets = Snippet.objects.all()
      serializer = SnippetSerializer(snippets, many=True)
      return Response(serializer.data)