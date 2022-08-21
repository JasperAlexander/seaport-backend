from rest_framework import generics
from .models import OrderOffer
from .serializers import OrderOfferSerializer, OrderOfferPublicSerializer


class GetOrderOffersView(generics.ListAPIView):
    queryset = OrderOffer.objects.all()
    serializer_class = OrderOfferPublicSerializer


class GetOrderOfferView(generics.RetrieveAPIView):
    queryset = OrderOffer.objects.all()
    serializer_class = OrderOfferPublicSerializer


class CreateOrderOfferView(generics.CreateAPIView):
    queryset = OrderOffer.objects.all()
    serializer_class = OrderOfferSerializer
