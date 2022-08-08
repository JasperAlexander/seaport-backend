from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer


class GetItemsView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class GetItemView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
