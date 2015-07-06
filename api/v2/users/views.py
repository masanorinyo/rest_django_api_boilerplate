from django.contrib.auth.models import User 
from .serializers import UserSerializer
from rest_framework import renderers
from rest_framework.response import Response
from resources.snippets.models import Snippet
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from api.v2.snippets.serializers import SnippetSerializer
from api.v2 import helpers
from rest_api_example.custom  import utilities

class UserViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer

  @detail_route(methods=['get'])
  def relationships(self, request, **kwargs):
    
    # needs to use global variable to get domain 
    response_obj = {
      "snippets": "http://api.rest_api_example.dev/users/1/relationships/snippets/"
    }

    return Response(response_obj)

  @detail_route(methods=['get'])
  def snippet_relationships(self, request, **kwargs):
    user = self.get_object()
    queryset = Snippet.objects.filter(user=user.id);
    data = helpers.create_data( queryset , 'snippets' )
    resource_name = "users"
    return Response({
      "links": {
        "self" : (utilities.get_path( resource_name )) + str(user.id) + "/relationships/snippets/",
        "related" : (utilities.get_path( resource_name )) + str(user.id) + "/snippets/",
      },
      "data":data,
    }) 
  
  @detail_route(methods=['get'])
  def snippet_included(self, request, **kwargs):
    user = self.get_object()
    queryset = Snippet.objects.filter(user=user.id);
    serializer= SnippetSerializer(queryset, many=True ).data
    return Response(serializer)