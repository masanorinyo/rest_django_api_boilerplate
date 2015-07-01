from rest_framework import serializers
from resources.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_api_example.custom  import utilities
from api.v2 import helpers

class SnippetSerializer(serializers.ModelSerializer):
  
  # private variables
  _resource_name = "snippets"

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
      'style',
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
    return { "self" : utilities.get_path(self._resource_name) + str(obj.id)}

  def get_relationships(self, obj): 
    return []

  def get_included(self,obj):
    return []
    