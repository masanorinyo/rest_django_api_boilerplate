from rest_framework import pagination
from rest_framework.response import Response


class PaginationSerializer(pagination.PageNumberPagination):
    
    
    def get_paginated_response(self, data):
        print 
        url = "http://" + self.request.META['HTTP_HOST'] + self.request.META['PATH_INFO']
        last_page = url + "?page=" + str(self.page.paginator.count / self.page_size)

        return Response({
            'self' : url,
            'last' : last_page,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
            'included' : ( data['included'] if 'included' in data else None )
        })