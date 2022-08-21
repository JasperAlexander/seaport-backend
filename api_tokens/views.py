from rest_framework import generics
from .models import Token
from .serializers import TokenSerializer


class GetTokensView(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class GetTokenView(generics.RetrieveAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    lookup_field = "address"
