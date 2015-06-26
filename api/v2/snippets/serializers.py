from rest_framework import serializers
from resources.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_api_example.custom  import utilities
from api.v2 import helpers

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
  
  # private variables
  _resource_name = "snippets"
  _related_models = [
    { 'name': 'user'}, 
    { 'name':'test', 'alternate' : 'owner'},
  ]

  # serialized values
  attribute = serializers.SerializerMethodField()
  relationships = serializers.SerializerMethodField()
  included = serializers.SerializerMethodField()
  links = serializers.SerializerMethodField()
  type = serializers.SerializerMethodField()
  
  class Meta:
    model = Snippet
    fields = (
      'id',
      'type',
      'attribute', 
      'relationships', 
      'links',
      'included', 
      # the below are the model parameters
      'code',
      'linenos',
      'language',
      'style'
    )
    extra_kwargs = {
      'code': {'write_only': True},
      'linenos': {'write_only': True},
      'language': {'write_only': True},
      'style': {'write_only': True},
    }

  def get_attribute(self, obj): 
    return {
      'code': obj.code, 
      'linenos': obj.linenos,
      'language': obj.language, 
      'style': obj.style
    }

  def get_type(self, obj):
    return self._resource_name

  def get_links(self,obj):
    return { "self" : utilities.get_path(self.context.get('request'), self._resource_name) + str(obj.id)}

  def get_relationships(self, obj): 
    response_obj = []
    request = self.context['request']
    url = (utilities.get_url(request)) + str(obj.id)
    query = request.QUERY_PARAMS['relationships'] if 'relationships' in request.QUERY_PARAMS else None
      
    if query:
      queries = query.split(',')
      for model in self._related_models:
        print model['name']
        if model['name'] in queries:
          alternative_name = model['alternate'] if 'alternate' in model else None
          response_obj.append(helpers.create_relationship_obj(url, obj, model['name'], obj.user, alternative_name ))
        
    return response_obj

  def get_included(self,obj):
    
    response_obj = []
    request = self.context['request']
    url = utilities.get_domain(request)
    query = request.QUERY_PARAMS['included'] if 'included' in request.QUERY_PARAMS else None

    if query:
      queries = query.split(',')
      if 'user' in queries:
        response_obj.append({
          "type": "user",
          "id": obj.user.id,
          "attributes": {
            "username": obj.user.username,
          },
          "links": {
            "self": url + "/users/" + str(obj.user.id)
          }
        })
      if 'test' in queries:
        response_obj.append({
          "type": "somethingelse",
          "id": 2,
          "attributes": {
            "username": obj.user.username,
          },
          "links": {
            "self": url + "/somethingelse/" + str(obj.user.id)
          }
        })
        
    return response_obj
    