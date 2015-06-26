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
  return http_protocol + "://" + domain

def get_path(request, resource_name):
  http_protocol = request.META['wsgi.url_scheme']
  domain = request.META['HTTP_HOST']
  return http_protocol + "://" + domain + '/' + resource_name + '/'

def get_url(request):
  http_protocol = request.META['wsgi.url_scheme']
  domain = request.META['HTTP_HOST']
  path = request.META['PATH_INFO']
  return http_protocol + "://" + domain + path


def removekey(d, key):
  r = dict(d)
  del r[key]
  return r