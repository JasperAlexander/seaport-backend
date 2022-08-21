from rest_framework import serializers
from .models import OrderOffer


class OrderOfferPublicSerializer(serializers.Serializer):
    itemType = serializers.IntegerField(read_only=True)
    token = serializers.CharField(read_only=True)
    identifierOrCriteria = serializers.CharField(read_only=True)
    startAmount = serializers.IntegerField(read_only=True)
    endAmount = serializers.IntegerField(read_only=True)


class OrderOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderOffer
        fields = [
            "itemType",
            "token",
            "identifierOrCriteria",
            "startAmount",
            "endAmount"
        ]
