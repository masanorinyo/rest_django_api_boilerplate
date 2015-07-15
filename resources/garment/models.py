from django.db import models
from resources.pattern.models import Pattern

class Garment(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  product = models.CharField(max_length=256)
  status = models.CharField(max_length=256)
  color = models.CharField(max_length=256)
  season = models.CharField(max_length=256)
  brand = models.CharField(max_length=256)
  size = models.CharField(max_length=256)
  name = models.CharField(max_length=256)
  gender = models.CharField(max_length=256)
  type = models.CharField(max_length=256)
  version = models.CharField(max_length=256)
  hasMesh = models.BooleanField(default=False)
  hasTexture = models.BooleanField(default=False)
  pattern = models.ForeignKey(Pattern, related_name='garment')