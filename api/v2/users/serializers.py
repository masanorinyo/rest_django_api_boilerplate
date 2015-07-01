from rest_framework import serializers
from django.contrib.auth.models import User
from resources.snippets.models import Snippet
from rest_api_example.custom  import utilities
from api.v2 import helpers
from api.v2.snippets.serializers import SnippetSerializer


class UserSerializer(serializers.ModelSerializer):
    

    # private variables
    _resource_name = "users"
    _related_models = [
      { 'name': 'snippets'},
    ]

    # serialized values
    attribute = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    relationships = serializers.SerializerMethodField()
    included = serializers.SerializerMethodField()

    class Meta:
        model = User
        depth = 1
        fields = (
          'id',
          'type',
          'attribute',
          'links',
          'relationships',
          'included',

          # the below is the model parameters
          'username',
        )
        extra_kwargs = {
          'username': {'write_only': True}
        }    

    def get_type(self, obj):
      return self._resource_name

    def get_links(self,obj):
      return { "self" : utilities.get_path(self._resource_name) + str(obj.id)}

    def get_attribute(self, obj): 
      return {
        'username' : obj.username
      }


    # [TODO]
    # use more helper method to make relationship and included
    def get_relationships(self, obj): 
      response_obj = []
      if self.context:
        request = self.context['request']
        url = (utilities.get_url(request)) + str(obj.id)
        query = request.QUERY_PARAMS['relationships'] if 'relationships' in request.QUERY_PARAMS else None
          
        if query:
          queries = query.split(',')
          for model in self._related_models:
            if model['name'] in queries:
              alternative_name = model['alternate'] if 'alternate' in model else None

              response_obj.append(helpers.create_relationship_obj(url, obj, model['name'], obj.snippets.all(), alternative_name ))
          
      return response_obj


    def get_included(self, obj):
      
      included_objs = []
      if self.context:
        request = self.context['request']
        url = (utilities.get_url(request)) + str(obj.id)
        query = request.QUERY_PARAMS['included'] if 'included' in request.QUERY_PARAMS else None
        
        if query: 
          queries = query.split(',')
          for model in self._related_models:
            queryset = Snippet.objects.all()
            if 'snippets' in queries:
              included_objs += SnippetSerializer(queryset, many=True ).data
              # included_objs += SnippetSerializer(queryset, many=True ).data


      return included_objs