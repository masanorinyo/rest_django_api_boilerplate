from rest_framework import serializers
from resources.garment.models import Garment
from rest_api_example.custom  import utilities
from api.v2 import helpers


class GarmentSerializer(serializers.ModelSerializer):
    

    # private variables
    _resource_name = "garments"

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
      return []

    def get_included(self,obj):
      return []