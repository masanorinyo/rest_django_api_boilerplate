from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name="snippet-detail", read_only=True)

    class Meta:
        model = User
        fields = ('id', 'snippets')