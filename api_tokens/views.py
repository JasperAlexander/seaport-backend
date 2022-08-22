from rest_framework import generics
from .models import Token
from .serializers import TokenSerializer
from .pagination import TokensCursorPagination


class GetTokensView(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    pagination_class = TokensCursorPagination


class GetTokenView(generics.RetrieveAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    lookup_field = "address"
