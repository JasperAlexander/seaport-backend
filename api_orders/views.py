from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer


class GetOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class GetOrderView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
