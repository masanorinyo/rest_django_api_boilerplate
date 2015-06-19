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
        else:
            subdomain = None

        request.subdomain = subdomain  
        
        if request.subdomain == "api":
            set_urlconf("rest_api_example.urls.api")
            request.urlconf = "rest_api_example.urls.api"
        elif request.subdomain == "admin":
            set_urlconf("rest_api_example.urls.admin")
            request.urlconf = "rest_api_example.urls.admin"
        else:
            set_urlconf("rest_api_example.urls.default")
            request.urlconf = "rest_api_example.urls.default"