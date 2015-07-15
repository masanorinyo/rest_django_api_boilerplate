from .serializers import GarmentSerializer
from rest_framework import renderers
from rest_framework.response import Response
from resources.garment.models import Garment
from resources.pattern.models import Pattern
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from api.v2 import helpers
from rest_api_example.custom  import utilities

class GarmentViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = Garment.objects.all()
  serializer_class = GarmentSerializer

  # @detail_route(methods=['get'])
  # def relationships(self, request, **kwargs):
    
  #   # needs to use global variable to get domain 
  #   response_obj = {
  #     "garments": "http://api.rest_api_example.dev/users/1/relationships/garments/"
  #   }

  #   return Response(response_obj)

  # @detail_route(methods=['get'])
  # def snippet_relationships(self, request, **kwargs):
  #   user = self.get_object()
  #   queryset = Snippet.objects.filter(user=user.id);
  #   data = helpers.create_data( queryset , 'garments' )
  #   resource_name = "users"
  #   return Response({
  #     "links": {
  #       "self" : (utilities.get_path( resource_name )) + str(user.id) + "/relationships/garments/",
  #       "related" : (utilities.get_path( resource_name )) + str(user.id) + "/garments/",
  #     },
  #     "data":data,
  #   }) 
  
  # @detail_route(methods=['get'])
  # def snippet_included(self, request, **kwargs):
  #   user = self.get_object()
  #   queryset = Snippet.objects.filter(user=user.id);
  #   serializer= Garmentserializer(queryset, many=True ).data
  #   resource_name = "users"
  #   # removing empty arrays
  #   for result in serializer:
  #     utilities.remove_empty_keys(result) 
  #   return Response({
  #     "links" : {
  #       "self" : (utilities.get_path( resource_name )) + str(user.id) + "/garments/",
  #     },
  #     "data" : serializer,
  #   })

  # 