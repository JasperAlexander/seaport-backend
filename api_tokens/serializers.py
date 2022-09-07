from rest_framework import serializers
from .models import Token


class TokenPublicSerializer(serializers.Serializer):
    symbol = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    image_url = serializers.URLField(read_only=True)
    name = serializers.CharField(read_only=True)
    decimals = serializers.IntegerField(read_only=True)
    eth_price = serializers.IntegerField(read_only=True)
    usd_price = serializers.IntegerField(read_only=True)


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = [
            "symbol",
            "address",
            "image_url",
            "name",
            "decimals",
            "eth_price",
            "usd_price"
        ]
