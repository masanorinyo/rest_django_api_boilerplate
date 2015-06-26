from django.forms import widgets
from rest_framework import serializers
from resources.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework.reverse import reverse
from rest_api_example.custom  import utilities
from api.v2 import factory

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
  attribute = serializers.SerializerMethodField()
  relationships = serializers.SerializerMethodField()
  included = serializers.SerializerMethodField()
  links = serializers.SerializerMethodField()
  type = serializers.SerializerMethodField()
  
  
  class Meta:
    model = Snippet
    fields = ('id','type','attribute', 'relationships', 'links','included', 'code','linenos','language','style')
    extra_kwargs = {
      'code': {'write_only': True},
      'linenos': {'write_only': True},
      'language': {'write_only': True},
      'style': {'write_only': True},
    }

  def get_type(self, obj):
    return 'snippets'

  def get_links(self,obj):
    return { "self" : utilities.get_path(self.context.get('request'), 'snippets') + str(obj.id)}

  def get_attribute(self, obj): 
    return {
      'code': obj.code, 
      'linenos': obj.linenos,
      'language': obj.language, 
      'style': obj.style
    }

  def get_relationships(self, obj): 
    response_obj = []
    request = self.context['request']
    url = (utilities.get_url(request)) + str(obj.id)
    query = request.QUERY_PARAMS['relationships'] if 'relationships' in request.QUERY_PARAMS else None
      
    if query:
      queries = query.split('.')
      if 'user' in queries:
        response_obj.append(factory.create_relationship_obj(url, obj, 'user', obj.owner, 'owner'))
      if 'test' in queries:
        response_obj.append(factory.create_relationship_obj(url, obj, 'test', obj.owner))
        
    return response_obj

  def get_included(self,obj):
    
    response_obj = []
    request = self.context['request']
    url = utilities.get_domain(request)
    query = request.QUERY_PARAMS['included'] if 'included' in request.QUERY_PARAMS else None

    if query:
      queries = query.split('.')
      if 'user' in queries:
        response_obj.append({
          "type": "user",
          "id": obj.owner.id,
          "attributes": {
            "username": obj.owner.username,
          },
          "links": {
            "self": url + "/users/" + str(obj.owner.id)
          }
        })
      if 'test' in queries:
        response_obj.append({
          "type": "somethingelse",
          "id": 2,
          "attributes": {
            "username": obj.owner.username,
          },
          "links": {
            "self": url + "/somethingelse/" + str(obj.owner.id)
          }
        })
        
    return response_obj
    