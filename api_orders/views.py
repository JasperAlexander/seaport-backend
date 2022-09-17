from rest_framework import generics, filters
from .models import Order
from .serializers import OrderReadSerializer, OrderWriteSerializer
from .pagination import OrdersCursorPagination
from django_filters.rest_framework import DjangoFilterBackend


class GetOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderReadSerializer
    pagination_class = OrdersCursorPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_fields = ["parameters__offer__token",
                        "parameters__offer__identifierOrCriteria"]
    search_fields = ["parameters__offer__token",
                     "parameters__offer__identifierOrCriteria"]
    # ordering_fields = ['end_time']
    ordering = ['-expiration_time']


class GetOrderView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer
