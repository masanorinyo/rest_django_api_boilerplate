from django.db import models

class Pattern(models.Model):
  status = models.CharField(max_length=256, null=True)
  subtype = models.CharField(max_length=256)
  panels = models.TextField(null=True)
  type = models.CharField(max_length=256)
  version = models.CharField(max_length=256, null=True)
  created = models.DateTimeField(auto_now_add=True, null=True)