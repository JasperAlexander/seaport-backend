from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Collection
from .serializers import CollectionSerializer
from .pagination import CollectionsCursorPagination


class GetCollectionsView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = CollectionsCursorPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["slug"]

    # def get_queryset(self):
    #     slug = self.request.query_params.get('slug')
    #     queryset = Collection.objects.all()
    #     if slug is not None:
    #         queryset = Collection.objects.filter(slug=slug)
    #     return queryset


class GetCollectionView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = "slug"
