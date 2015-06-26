from rest_framework.renderers import JSONRenderer
from rest_api_example.custom  import utilities

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
      index = 0
      for result in data['results']:
        included_objs.append(result.pop('included',0))
        if not data['results'][index]['relationships']:
          data['results'][index] = utilities.removekey(data['results'][index],'relationships') 
        index += 1
        
      
      response_data = {
        "data" : data['results'],
        "links" : {
          "self" : ( data['self'] if 'self' in data else None ),
          "next" : ( data['next'] if 'next' in data else None ),
          "previous" : ( data['previous'] if 'previous' in data else None ),
          "last" : ( data['last'] if 'last' in data else None ),
        },
      }


      # make the dictionary unique 
      if included_objs[0]:
        # make included_objs lists flat
        included_objs = [item for sublist in included_objs for item in sublist]
        # retrieve unique object from the included_objs list
        included_objs = {v['id'] and v['type']:v  for v in included_objs}.values()
        response_data["included"] = included_objs
      

    else:

      if 'included' in data:
        data = utilities.removekey(data,'included') 
      if 'relationships' in data:
        data = utilities.removekey(data,'relationships') 

      response_data = data

    return super(ApiRenderer, self).render(response_data, accepted_media_type, renderer_context)
