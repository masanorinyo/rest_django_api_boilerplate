from django.db import models

class Test2(models.Model):
  version = models.CharField(max_length=256)
