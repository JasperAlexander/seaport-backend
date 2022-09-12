from rest_framework import generics
from .models import Token
from .serializers import TokenReadSerializer
from .pagination import TokensCursorPagination


class GetTokensView(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenReadSerializer
    pagination_class = TokensCursorPagination


class GetTokenView(generics.RetrieveAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenReadSerializer
    lookup_field = "address"
