from rest_framework import generics, filters
from .models import Order
from .serializers import OrderSerializer
from .pagination import OrdersCursorPagination
from django_filters.rest_framework import DjangoFilterBackend


class GetOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrdersCursorPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]  # , filters.OrderingFilter]
    filterset_fields = ["parameters__offer__token",
                        "parameters__offer__identifierOrCriteria"]
    search_fields = ["parameters__offer__token",
                     "parameters__offer__identifierOrCriteria"]


class GetOrderView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
