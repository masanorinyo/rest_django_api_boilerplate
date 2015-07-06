from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from rest_api_example.custom  import utilities
import urlparse
import logging
logger = logging.getLogger(__name__)


class VersionSwitchMiddleware(object):

    def process_request(self, request):
        r = resolve(request.path_info)
        if 'HTTP_ACCEPT' in request.META:
          version = utilities.get_api_version(request.META['HTTP_ACCEPT'])
        else: 
          # when being accessed by testserver
          # get version info from path info
          # [TEMP_FIX][TODO] : testserver needs to run on proxy server so that it can make a HTTP request, which can be stored in request object
          version = request.META['PATH_INFO'].split('/')[1]
        old_version = r.namespace.split(':')[-1]
        if r.namespace.startswith('api:') and version:
            request.path_info = reverse('{}:{}'.format(r.namespace.replace(old_version, version), r.url_name), args=r.args, kwargs=r.kwargs)