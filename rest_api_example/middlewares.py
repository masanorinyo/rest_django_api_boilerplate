from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from rest_api_example.util import get_api_version
import urlparse
import logging
logger = logging.getLogger(__name__)


class VersionSwitch(object):

    def process_request(self, request):
        r = resolve(request.path_info)
        version = get_api_version(request.META['HTTP_ACCEPT'])
        if r.namespace.startswith('api:') and version:
            old_version = r.namespace.split(':')[-1]
            request.path_info = reverse('{}:{}'.format(r.namespace.replace(old_version, version), r.url_name), args=r.args, kwargs=r.kwargs)


