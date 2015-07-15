from django.db import models

class Pattern(models.Model):
  status = models.CharField(max_length=256)
  subtype = models.CharField(max_length=256)
  panels = models.CharField(max_length=256)
  type = models.CharField(max_length=256)
  version = models.CharField(max_length=256)
  created = models.DateTimeField(auto_now_add=True)