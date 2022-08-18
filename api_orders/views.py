from rest_framework import generics
from .models import Order
from .serializers import OrderReadSerializer, OrderSerializer


class GetOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderReadSerializer


class GetOrderView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderReadSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
