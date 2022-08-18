from rest_framework import generics
from .models import Consideration
from .serializers import ConsiderationPublicSerializer, ConsiderationSerializer


class GetOrderConsiderationsView(generics.ListAPIView):
    queryset = Consideration.objects.all()
    serializer_class = ConsiderationPublicSerializer


class GetOrderConsiderationView(generics.RetrieveAPIView):
    queryset = Consideration.objects.all()
    serializer_class = ConsiderationPublicSerializer


class CreateOrderConsiderationsView(generics.CreateAPIView):
    queryset = Consideration.objects.all()
    serializer_class = ConsiderationSerializer
