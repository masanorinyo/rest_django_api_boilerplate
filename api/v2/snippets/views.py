from resources.snippets.models import Snippet
from .serializers import SnippetSerializer
from rest_framework import viewsets


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer 

    # The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
    def perform_create(self, serializer):
      serializer.save(user=self.request.user)