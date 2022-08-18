from rest_framework import generics
from .models import OrderParameters
from .serializers import OrderParametersPublicSerializer, OrderParametersSerializer


class GetOrderParametersView(generics.ListAPIView):
    queryset = OrderParameters.objects.all()
    serializer_class = OrderParametersPublicSerializer


class GetOrderParameterView(generics.RetrieveAPIView):
    queryset = OrderParameters.objects.all()
    serializer_class = OrderParametersPublicSerializer


class CreateOrderParametersView(generics.CreateAPIView):
    queryset = OrderParameters.objects.all()
    serializer_class = OrderParametersSerializer
