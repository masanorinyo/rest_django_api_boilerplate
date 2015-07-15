from rest_framework import serializers
from resources.pattern.models import Pattern
from resources.garment.models import Garment
from rest_api_example.custom  import utilities
from api.v2.garments.serializers import GarmentSerializer
from api.v2 import helpers


class PatternSerializer(serializers.ModelSerializer):
    

    # private variables
    _resource_name = "patterns"
    _related_models = [{'name':'garment'}]

    # serialized values
    attribute = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()
    model_type = serializers.SerializerMethodField()
    relationships = serializers.SerializerMethodField()
    included = serializers.SerializerMethodField()

    class Meta:
        model = Pattern
        fields = (
          'id',
          'model_type',
          'attribute',
          'links',
          'relationships',
          'included',

          # the below is the model parameters
          'status',
          'subtype',
          'panels',
          'type',
          'version',
        )
        extra_kwargs = {
          'status': {'write_only': True},
          'subtype': {'write_only': True},
          'panels': {'write_only': True},
          'type': {'write_only': True},
          'version': {'write_only': True},
        }    

    def get_model_type(self, obj):
      return self._resource_name

    def get_links(self,obj):
      return { "self" : utilities.get_path( self._resource_name ) + str(obj.id)}

    def get_attribute(self, obj): 
      return {
        'status' : obj.status,
        'subtype' : obj.subtype,
        'panels' : obj.panels,
        'type' : obj.type,
        'version' : obj.version,
      }

    def get_relationships(self, obj): 
      # print Garment.objects.all()
      response_obj = []
      if self.context:
        request = self.context['request']
        url = (utilities.get_path(self._resource_name)) + str(obj.id)
        query = request.QUERY_PARAMS['relationships'] if 'relationships' in request.QUERY_PARAMS else None
        for model in self._related_models:  
          type_name = model['alternate'] if 'alternate' in model else model['name']
          data = helpers.create_data( Garment.objects.filter(pattern=obj.id) , type_name )
          response_obj.append(helpers.create_relationship_obj(url, obj, model['name'], data ))
          
      return response_obj


    def get_included(self, obj):
      
      included_objs = []
      if self.context:
        request = self.context['request']
        url = (utilities.get_path(self._resource_name)) + str(obj.id)
        query = request.QUERY_PARAMS['included'] if 'included' in request.QUERY_PARAMS else None
        
        if query: 
          queries = query.split(',')
          for key in queries:
            if 'pattern' == key or 'patterns' == key:
              queryset = Garment.objects.all()
              included_objs += GarmentSerializer(queryset, many=True ).data
            else:
              included_objs.append({
                "id": None, 
                "model_type": key,
                "error": "There is no such related model"
              })

      return included_objs
    