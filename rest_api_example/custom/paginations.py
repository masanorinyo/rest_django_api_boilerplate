from rest_framework import pagination
from rest_framework.response import Response


class PaginationSerializer(pagination.PageNumberPagination):
        
    def get_paginated_response(self, data):
        http_protocol = self.request.META['wsgi.url_scheme']
        domain = self.request.META['HTTP_HOST']
        path = self.request.META['PATH_INFO']
        url = http_protocol + "://" + domain + path
        current_page = self.request.build_absolute_uri() 
        last_page = current_page + "?page=" + str(self.page.paginator.count / self.page_size + 1 ) # 1 stands for one page

        return Response({
            'self' : current_page,
            'last' : last_page,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })