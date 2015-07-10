"""
This class allows to modify json reponse structure
"""

from rest_framework.renderers import JSONRenderer
from rest_api_example.custom  import utilities

class ApiRenderer(JSONRenderer):
  
  media_type ='application/vdn.bespoke.v2+json' # this represents the accepted content-type


  def render(self, data, accepted_media_type ='application/vdn.bespoke.v2+json', renderer_context=None):
    """
    'data' represents the data returned by requested API end point
    """
    if data: 

      # remove empty parameters
      utilities.remove_empty_keys(data)
      if 'results' in data:
        
        included_objs = []
        index = 0
        for result in data['results']:
          included_objs = result.pop('included')
          if not data['results'][index]['relationships']:
            utilities.remove_empty_keys(data['results'][index]) 
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
        if included_objs:
          # retrieve unique object from the included_objs list
          included_objs = sorted(included_objs,key=lambda x:(x["type"],x["id"]))
          seen_items = set()
          filtered_dictlist = (x for x in included_objs if (x["id"],x["type"]) not in seen_items and not seen_items.add((x["id"],x["type"])))
          included_objs = sorted(filtered_dictlist,key=lambda x:(x["type"],x["id"]))

          for obj in included_objs:
            utilities.remove_empty_keys(obj)

          response_data["included"] = included_objs        

      else:
        
        if "data" in data:
          response_data = data
        else:
          response_data = {}
          if "links" in data:
            response_data['links'] = data.pop('links')
          response_data['data'] = data
          

    
    else: 
      response_data = data        

    return super(ApiRenderer, self).render(response_data, accepted_media_type, renderer_context)
