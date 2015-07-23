from rest_framework import serializers
from resources.pattern.models import Pattern
from resources.garment.models import Garment
from rest_api_example.custom  import utilities
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

      panels = utilities.convert_to_list(obj.panels)
    
      return {
        'status' : obj.status,
        'subtype' : obj.subtype,
        'panels' : panels,
        'type' : obj.type,
        'version' : obj.version,
      }

    def get_relationships(self, obj): 
      response_obj = []
      return response_obj


    def get_included(self, obj):
      
      included_objs = []
      return included_objs
    