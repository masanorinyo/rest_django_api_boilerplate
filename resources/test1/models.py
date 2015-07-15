from django.db import models
from resources.test2.models import Test2

class Test1(models.Model):
  version = models.CharField(max_length=256)
  test2 = models.ForeignKey(Test2, related_name='test1')
