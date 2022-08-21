from rest_framework import generics
from .models import OrderParameter
from .serializers import OrderParametersSerializer


class GetOrderParametersView(generics.ListAPIView):
    queryset = OrderParameter.objects.all()
    serializer_class = OrderParametersSerializer


class GetOrderParameterView(generics.RetrieveAPIView):
    queryset = OrderParameter.objects.all()
    serializer_class = OrderParametersSerializer


class CreateOrderParameterView(generics.CreateAPIView):
    queryset = OrderParameter.objects.all()
    serializer_class = OrderParametersSerializer
