from rest_framework import generics
from .models import Offer
from .serializers import OfferPublicSerializer, OfferSerializer


class GetOrderOffersView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferPublicSerializer


class GetOrderOfferView(generics.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferPublicSerializer


class CreateOrderOffersView(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
