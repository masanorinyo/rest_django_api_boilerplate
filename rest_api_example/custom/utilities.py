from django.conf import settings
import string, random

def get_api_version(url):
  if "application/vdn.bespoke" in url:
    try: 
      return "v"+url.split('+')[0].split('v')[2]
    except IndexError: 
      return False
  else:
    return False

def get_domain(request):
  if 'wsgi.url_scheme' in request.META:
    http_protocol = request.META['wsgi.url_scheme']
  else:
    http_protocol = "http"
  return http_protocol + "://" + settings.APP_DOMAIN + "/"

def get_path(resource_name):
  http_protocol = "http"
  return http_protocol +"://" + settings.APP_DOMAIN + "/" + resource_name + '/'

def get_url(request):
  if 'wsgi.url_scheme' in request.META:
    http_protocol = request.META['wsgi.url_scheme']
  else:
    http_protocol = "http"
  path = request.META['PATH_INFO']
  return http_protocol + "://" + settings.APP_DOMAIN + path


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

def generate_random_strings(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))