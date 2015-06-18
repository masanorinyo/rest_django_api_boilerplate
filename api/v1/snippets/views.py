from django.contrib.auth.models import User 
from resources.snippets.models import Snippet
from resources.snippets.permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
import logging
logger = logging.getLogger(__name__)


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer 
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #   snippet = self.get_object()
    #   return Response(snippet.highlighted)

    # The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
    # def perform_create(self, serializer):
    #   serializer.save(owner=self.request.user)