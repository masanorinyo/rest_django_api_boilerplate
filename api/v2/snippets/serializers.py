from django.forms import widgets
from rest_framework import serializers
from resources.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
  attribute = serializers.SerializerMethodField()
  relationships = serializers.SerializerMethodField()
  included = serializers.SerializerMethodField()
  type = serializers.SerializerMethodField()
  
  class Meta:
    model = Snippet
    fields = ('id','type','attribute', 'relationships', 'included')

  def get_type(self, obj):
    return 'snippets'
  
  def get_attribute(self, obj): 
    return {
      'code': obj.code, 
      'linenos': obj.linenos,
      'language': obj.language, 
      'style': obj.style
    }

  def get_relationships(self, obj): 
    return {
      'owner': {
        "links" :{
          "self" : "test",
          "related" : "test"
        },
        "data" : {
          "type" : 'user',
          "id" : obj.owner.id,
        }
      }
    }

  def get_included(self,obj):
    return {
      "type": "user",
      "id": obj.owner.id,
      "attributes": {
        "username": obj.owner.username,
      },
      "links": {
        "self": "test"
      }
    }