from rest_framework import serializers
from rest_api_example.custom  import utilities
from resources.test1.models  import Test1
from resources.test2.models  import Test2
from api.v2 import helpers

class Test1Serializer(serializers.ModelSerializer):
  
  # private variables
  _resource_name = "test1"
  _related_models = [{'name':'test2'}]

  # serialized values
  attribute = serializers.SerializerMethodField()
  links = serializers.SerializerMethodField()
  model_type = serializers.SerializerMethodField()
  relationships = serializers.SerializerMethodField()
  included = serializers.SerializerMethodField()
  
  class Meta:
    model = Test1
    fields = (
      'id',
      'model_type',
      'attribute', 
      'links',
      'relationships', 
      'included', 
      # the below are the model parameters
      'test2',
      'version'
    )
    extra_kwargs = {
      'test2': {'write_only': True},
      'version': {'write_only': True},
    }

  def get_attribute(self, obj): 
    return {
      'version': obj.version, 
    }

  def get_model_type(self, obj):
    return self._resource_name

  def get_links(self,obj):
    return { "self" : utilities.get_path( self._resource_name ) + str(obj.id)}

  def get_relationships(self, obj): 
    return []


  def get_included(self, obj):
    return []