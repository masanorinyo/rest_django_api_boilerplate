from django.forms import widgets
from rest_framework import serializers
from resources.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
  # owner = serializers.StringRelatedField(source='owner.username')
  # highlight = serializers.StringRelatedField()

  class Meta:
    model = Snippet
    fields = ('title', 'code', 'linenos', 'language', 'style')
