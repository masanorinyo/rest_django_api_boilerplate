from rest_framework import serializers
from rest_api_example.custom  import utilities
from resources.test2.models  import Test2
from resources.test1.models  import Test1
from api.v2 import helpers
from api.v2.test1.serializers import Test1Serializer

class Test2Serializer(serializers.ModelSerializer):
  
  # private variables
  _resource_name = "test2"
  _related_models = [{'name':'test1'}]


  # serialized values
  attribute = serializers.SerializerMethodField()
  links = serializers.SerializerMethodField()
  model_type = serializers.SerializerMethodField()
  relationships = serializers.SerializerMethodField()
  included = serializers.SerializerMethodField()
  
  class Meta:
    model = Test2
    fields = (
      'id',
      'model_type',
      'attribute', 
      'links',
      'relationships', 
      'included', 
      # the below are the model parameters
      'version'
    )
    extra_kwargs = {
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
      
      response_obj = []
      if self.context:
        request = self.context['request']
        url = (utilities.get_path(self._resource_name)) + str(obj.id)
        query = request.QUERY_PARAMS['relationships'] if 'relationships' in request.QUERY_PARAMS else None
        for model in self._related_models:  
          type_name = model['alternate'] if 'alternate' in model else model['name']
          data = helpers.create_data( Test1.objects.filter(test2=obj.id) , type_name )
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
            if 'test1' == key:
              queryset = Test1.objects.all()
              included_objs += Test1Serializer(queryset, many=True ).data
            else:
              included_objs.append({
                "id": None, 
                "model_type": key,
                "error": "There is no such related model"
              })

      return included_objs    