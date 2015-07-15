from .serializers import PatternSerializer
from resources.pattern.models import Pattern
from rest_framework import viewsets

class PatternViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list` and `detail` actions.
  """
  queryset = Pattern.objects.all()
  serializer_class = PatternSerializer
