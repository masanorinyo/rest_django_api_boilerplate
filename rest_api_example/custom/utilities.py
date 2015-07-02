# [TODO]
# make domain a global varialbe

def get_api_version(url):
  if "application/vdn.bespoke" in url:
    try: 
      return "v"+url.split('+')[0].split('v')[2]
    except IndexError: 
      return False
  else:
    return False

def get_domain(request):
  http_protocol = request.META['wsgi.url_scheme']
  domain = request.META['HTTP_HOST']
  return "http://api.rest_api_example.dev/"

def get_path(resource_name):
  # make the domain environment variable
  return "http://api.rest_api_example.dev/" + resource_name + '/'

def get_url(request):
  http_protocol = request.META['wsgi.url_scheme']
  domain = request.META['HTTP_HOST']
  path = request.META['PATH_INFO']
  return http_protocol + "://" + domain + path


def removekey(d, key):
  r = dict(d)
  del r[key] 
  return r

def remove_empty_keys(d):
  if isinstance(d,  list):
    for k in d:
      for v in k:
        if not k[v]:
          del  k[v]
  else:
    for k in d.keys():
        if not d[k]:
            del d[k]