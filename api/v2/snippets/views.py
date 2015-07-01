from resources.snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer 

    def perform_create(self, serializer):
      serializer.save(user=self.request.user) 