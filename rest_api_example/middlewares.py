from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
import urlparse
import logging
logger = logging.getLogger(__name__)

api_urls = ['tasks']  # the URLs you want to serve on your api subdomain

class SubdomainMiddleware:
    def process_request(self, request):
        """
        Checks subdomain against requested URL.

        Raises 404 or returns None
        """
        path = request.get_full_path()  # i.e. /tasks/
        root_url = path.split('/')[1]  # i.e. tasks
        domain_parts = request.get_host().split('.')

        if (len(domain_parts) > 2):
            subdomain = domain_parts[0]
            if (subdomain.lower() == 'www'):
                subdomain = None
            domain = '.'.join(domain_parts[1:])
        else:
            subdomain = None
            domain = request.get_host()

        request.subdomain = subdomain  # i.e. 'api'
        request.domain = domain  # i.e. 'example.com'

        # Loosen restrictions when developing locally or running test suite
        if not request.domain in ['localhost:8000', 'testserver']:
            return  # allow request

        if request.subdomain == "api" and root_url not in api_urls:
            raise Http404()  # API subdomain, don't want to serve regular URLs
        elif not subdomain and root_url in api_urls:
            raise Http404()  # No subdomain or www, don't want to serve API URLs
        else:  
            raise Http404()  # Unexpected subdomain
        return  # allow request  


class VersionSwitch(object):

    def process_request(self, request):
        r = resolve(request.path_info)
        version = request.META.get('HTTP_X_VERSION', False)
        logger.info("version information is :",version)
        # if r.namespace.startswith('api:') and version:
        #     old_version = r.namespace.split(':')[-1]
        #     request.path_info = reverse('{}:{}'.format(r.namespace.replace(old_version, version), r.url_name), args=r.args, kwargs=r.kwargs)


class GetSubdomainMiddleware:

    def process_request(self, request):
        bits = urlparse.urlsplit(request.META['HTTP_HOST'])[0].split('.')
        if not( len(bits) == 3):
            pass#Todo Raise an exception etc
        request.subdomain = bits[0]
