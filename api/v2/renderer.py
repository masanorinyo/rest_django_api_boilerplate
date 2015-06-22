from rest_framework.renderers import JSONRenderer

class ApiRenderer(JSONRenderer):
  
  """
  This class allows to modify json reponse structure
  """

  media_type ='application/vdn.bespoke.v2+json' # this represents the accepted content-type


  def render(self, data, accepted_media_type ='application/vdn.bespoke.v2+json', renderer_context=None):
    """
    'data' represents the data returned by requested API end point
    """

    if 'results' in data:
      response_data = {
        "links" : {
          "self" : ( data['self'] if 'self' in data else None ),
          "next" : ( data['next'] if 'next' in data else None ),
          "previous" : ( data['previous'] if 'previous' in data else None ),
          "last" : ( data['last'] if 'last' in data else None ),
        },
        "data" : data['results'],
        "included" : ( data['included'] if 'included' in data['results'] else None )
      }
    else:
      response_data = data

    return super(ApiRenderer, self).render(response_data, accepted_media_type, renderer_context)