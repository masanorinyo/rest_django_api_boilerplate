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
      included_objs = []
      for result in data['results']:
        included_objs.append(result.pop('included',0))
        
      # make the dictionary unique 
      included_objs = {v['id']:v for v in included_objs}.values()
      response_data = {
        "links" : {
          "self" : ( data['self'] if 'self' in data else None ),
          "next" : ( data['next'] if 'next' in data else None ),
          "previous" : ( data['previous'] if 'previous' in data else None ),
          "last" : ( data['last'] if 'last' in data else None ),
        },
        "data" : data['results'],
        "included" : included_objs
      }

    else:
      response_data = data

    return super(ApiRenderer, self).render(response_data, accepted_media_type, renderer_context)

  def get_included_objs(objs):

    return objs