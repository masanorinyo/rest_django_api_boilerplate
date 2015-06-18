from rest_framework.renderers import JSONRenderer

class ApiV1(JSONRenderer):
  media_type = 'application/vdn.bespoke.v1+json' 

class ApiV2(JSONRenderer):
  media_type = 'application/vdn.bespoke.v2+json' 