from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class UsersCursorPagination(CursorPagination):
    ordering = "username"
    page_size = 6

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'users': data
        })
