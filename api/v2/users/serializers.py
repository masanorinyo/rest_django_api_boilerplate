from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # owner = serializers.StringRelatedField(source='owner.username')
    # highlight = serializers.StringRelatedField()
    # customField = serializers.ModelSerializer(source='get_absolute_url')

    # def get_type(self, model):
    #   return model.type == "snippet"

    class Meta:
        model = User
        fields = ( 'id', 'username', 'snippets')