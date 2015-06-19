from rest_framework.renderers import JSONRenderer

class ApiRenderer(JSONRenderer):
  media_type ='application/vdn.bespoke.v2+json'
  def render(self, data, accepted_media_type ='application/vdn.bespoke.v2+json', renderer_context=None):

    included = ""

    data = {
      "links" : {
        "self" : ( data['url'] if hasattr(data, 'url') else None),
        "next" : ( data['next'] if hasattr(data, 'next') else None),
        "last" : ( data['last'] if hasattr(data, 'last') else None),
      },
      "data" : ( data['results'] if hasattr(data, 'results') else None),
      "included" : data
    }

    return super(ApiRenderer, self).render(data, accepted_media_type, renderer_context)