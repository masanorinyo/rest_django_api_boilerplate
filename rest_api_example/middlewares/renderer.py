from rest_framework.renderers import JSONRenderer

class ApiV1Renderer(JSONRenderer):
  media_type ='application/vdn.bespoke.v1+json'
  # def render(self, data, accepted_media_type ='application/vdn.bespoke.v1+json', renderer_context=None):

  #    #determine the resource name for this request - default to objects if not defined
  #   resource = getattr(renderer_context.get('view').get_serializer().Meta, 'resource_name', 'objects')

  #   #check if the results have been paginated
  #   if data.get('paginated_results'):
  #       #add the resource key and copy the results
  #       response_data['meta'] = data.get('meta')
  #       response_data[resource] = data.get('paginated_results')
  #   else:
  #       response_data[resource] = data

  #   #call super to render the response
  #   response = super(ApiV1Renderer, self).render(response_data, accepted_media_type, renderer_context)

  #   return response

class ApiV2Renderer(JSONRenderer):
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

    return super(ApiV2Renderer, self).render(data, accepted_media_type, renderer_context)