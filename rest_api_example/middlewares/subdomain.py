from django.core.urlresolvers import set_urlconf

class SubdomainMiddleware:
    def process_request(self, request):
        """
        Checks subdomain against requested URL.
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

        request.subdomain = subdomain  
        
        # no re-setting urlconf when developing locally or running test suite, meaning the default urlconf in settings.py will be used
        if not request.domain in ['testserver']:

            if request.subdomain == "api":
                set_urlconf("rest_api_example.urls.api")
                request.urlconf = "rest_api_example.urls.api"
            elif request.subdomain == "admin":
                set_urlconf("rest_api_example.urls.admin")
                request.urlconf = "rest_api_example.urls.admin"
            else:
                set_urlconf("rest_api_example.urls.default")
                request.urlconf = "rest_api_example.urls.default"