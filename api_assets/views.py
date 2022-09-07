from rest_framework import generics, filters
from .models import Asset
from .serializers import AssetSerializer, AssetPublicSerializer
from .mixins import MultipleFieldLookupMixin
from .pagination import AssetsCursorPagination
from django_filters.rest_framework import DjangoFilterBackend


class GetAssetsView(generics.ListAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetPublicSerializer
    pagination_class = AssetsCursorPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]  # , filters.OrderingFilter]
    filterset_fields = ["asset_contract__address",
                        "owner__username", "owner__address"]
    search_fields = ["name", "collection__name"]
    # ordering_fields = [""]


class GetAssetView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    lookup_fields = ["asset_contract__address", "token_id"]


class CreateAssetView(generics.CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class DestroyAssetView(MultipleFieldLookupMixin, generics.DestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    lookup_fields = ["asset_contract__address", "token_id"]


class UpdateAssetView(MultipleFieldLookupMixin, generics.UpdateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    lookup_fields = ["asset_contract__address", "token_id"]
