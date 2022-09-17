from rest_framework import generics, filters
from .models import Event
from .serializers import EventReadSerializer, EventWriteSerializer
from .pagination import EventsCursorPagination
from django_filters.rest_framework import DjangoFilterBackend


class GetEventsView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventReadSerializer
    pagination_class = EventsCursorPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]
    #    filters.OrderingFilter]
    filterset_fields = ["asset__asset_contract__address", "asset__token_id"]
    search_fields = ["asset__asset_contract__address", "asset__token_id"]


class GetEventView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventReadSerializer


class CreateEventView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventWriteSerializer
