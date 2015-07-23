from .serializers import PatternSerializer
from resources.pattern.models import Pattern
from rest_framework import viewsets
import json

class PatternViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = Pattern.objects.all()
  serializer_class = PatternSerializer

  def perform_create(self, serializer):
    try: 
      panels = json.loads(self.request.data['panels'])

    except ValueError: 
      panels = json.dumps(self.request.data['panels'])

    serializer.save(panels=panels) 
