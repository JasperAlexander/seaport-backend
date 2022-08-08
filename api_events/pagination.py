from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class EventsCursorPagination(CursorPagination):
    ordering = "pk"
    page_size = 6

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'events': data
        })
