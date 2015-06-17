from django.forms import widgets
from rest_framework import serializers
from resources.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

  class Meta:
    model = Snippet
    fields = ('url', 'highlight', 'owner', 'code', 'linenos', 'style')
