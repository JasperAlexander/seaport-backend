from rest_framework import generics
from .models import OrderConsideration
from .serializers import OrderConsiderationSerializer, OrderConsiderationPublicSerializer


class GetOrderConsiderationsView(generics.ListAPIView):
    queryset = OrderConsideration.objects.all()
    serializer_class = OrderConsiderationPublicSerializer


class GetOrderConsiderationView(generics.RetrieveAPIView):
    queryset = OrderConsideration.objects.all()
    serializer_class = OrderConsiderationPublicSerializer


class CreateOrderConsiderationView(generics.CreateAPIView):
    queryset = OrderConsideration.objects.all()
    serializer_class = OrderConsiderationSerializer
