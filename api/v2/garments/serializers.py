from rest_framework import serializers
from resources.garment.models import Garment
from resources.pattern.models import Pattern
from rest_api_example.custom  import utilities
from api.v2.patterns.serializers import PatternSerializer
from api.v2 import helpers
test = []
class GarmentSerializer(serializers.ModelSerializer):
    

    # private variables
    _resource_name = "garments"
    _related_models = [{'name':'patterns'}]
    # serialized values
    attribute = serializers.SerializerMethodField()
    relationships = serializers.SerializerMethodField()
    included = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()
    model_type = serializers.SerializerMethodField()
  

    class Meta:
        model = Garment
        fields = (
          'id',
          'model_type',
          'attribute',
          'links',
          'relationships',
          'included',

          # the below is the model parameters
          'pattern',
          'created',
          'product',
          'status',
          'color',
          'season',
          'brand',
          'size',
          'name',
          'gender',
          'type',
          'version',
          'hasMesh',
          'hasTexture',
        )
        extra_kwargs = {
          'pattern': {'write_only': True},
          'product': {'write_only': True},
          'status': {'write_only': True},
          'color': {'write_only': True},
          'season': {'write_only': True},
          'brand': {'write_only': True},
          'size': {'write_only': True},
          'name': {'write_only': True},
          'gender': {'write_only': True},
          'type': {'write_only': True},
          'hasMesh': {'write_only': True},
          'version': {'write_only': True},
          'hasTexture': {'write_only': True},
        }    

    def get_model_type(self, obj):
      return self._resource_name

    def get_links(self,obj):
      return { "self" : utilities.get_path( self._resource_name ) + str(obj.id)}

    def get_attribute(self, obj): 
      
      s3key = obj.brand + "/" + obj.type + "/" + obj.gender + "/" + obj.season + "/" + str(obj.id)

      return {
        'pattern_id' : obj.pattern.id,
        'product': obj.product,
        'status': obj.status,
        'color': obj.color,
        'season': obj.season,
        'brand': obj.brand,
        'size': obj.size,
        'name': obj.name,
        's3key': s3key,
        'gender': obj.gender,
        'type': obj.type,
        'hasMesh': obj.hasMesh,
        'version': obj.version,
        'hasTexture': obj.hasTexture,
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
          data = helpers.create_data( obj.pattern , type_name )
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
              
              queryset = Pattern.objects.all()
              included_objs += PatternSerializer(queryset, many=True ).data
            else:
              included_objs.append({
                "id": None, 
                "model_type": key,
                "error": "There is no such related model"
              })

      return included_objs
    