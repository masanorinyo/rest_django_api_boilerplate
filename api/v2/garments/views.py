from .serializers import GarmentSerializer
from rest_framework import renderers
from rest_framework.response import Response
from resources.garment.models import Garment
from resources.pattern.models import Pattern
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from api.v2.patterns.serializers import PatternSerializer

# [TODO] - make the utility and helper to class object
from api.v2 import helpers
from rest_api_example.custom  import utilities

# [TODO] - add comments 
class GarmentViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = Garment.objects.all()
  serializer_class = GarmentSerializer

  # [TODO] - make a utility class which makes the list of objects unique based on id and model_type 
  # adding included object
  def get_serializer_class(self):
    if self.action == 'list':
      included_objs = []
      
      current_page = self.request.QUERY_PARAMS['page'] if 'page' in self.request.QUERY_PARAMS else 1
      limit = 9
      offset = 0
      if current_page != 1:
        limit = 9 * current_page
        offset = 9 * (int(current_page) - 1)
      for garment in Garment.objects.all()[offset:limit]:
        included_objs.append(PatternSerializer(garment.pattern).data)
      GarmentSerializer.included=included_objs
    return GarmentSerializer
  
  # adding relationship controllers
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

  