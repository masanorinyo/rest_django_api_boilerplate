from .serializers import GarmentSerializer
from rest_framework import renderers
from rest_framework.response import Response
from resources.garment.models import Garment
from resources.pattern.models import Pattern
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from api.v2 import helpers
from api.v2.patterns.serializers import PatternSerializer
from rest_api_example.custom  import utilities

class GarmentViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = Garment.objects.all()
  serializer_class = GarmentSerializer

  @detail_route(methods=['get'])
  def relationships(self, request, **kwargs):
    
    # needs to use global variable to get domain 
    response_obj = {
      "garments": "http://api.rest_api_example.dev/garments/1/relationships/patterns/"
    }

    return Response(response_obj)

  @detail_route(methods=['get'])
  def pattern_relationships(self, request, **kwargs):
    garment = self.get_object()
    queryset = Pattern.objects.filter(garment=garment.id);
    data = helpers.create_data( queryset , 'garments' )
    resource_name = "garments"
    return Response({
      "links": {
        "self" : (utilities.get_path( resource_name )) + str(garment.id) + "/relationships/patterns/",
        "related" : (utilities.get_path( resource_name )) + str(garment.id) + "/patterns/",
      },
      "data":data,
    }) 
  
  @detail_route(methods=['get'])
  def pattern_included(self, request, **kwargs):
    garment = self.get_object()
    queryset = Pattern.objects.filter(garment=garment.id);
    serializer= PatternSerializer(queryset, many=True ).data
    resource_name = "garments"
    # removing empty arrays
    for result in serializer:
      utilities.remove_empty_keys(result) 
    return Response({
      "links" : {
        "self" : (utilities.get_path( resource_name )) + str(garment.id) + "/patterns/",
      },
      "data" : serializer,
    })

  