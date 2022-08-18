from rest_framework import serializers
from .models import Offer


class OfferPublicSerializer(serializers.Serializer):
    itemType = serializers.IntegerField(read_only=True)
    token = serializers.CharField(read_only=True)
    identifierOrCriteria = serializers.CharField(read_only=True)
    startAmount = serializers.IntegerField(read_only=True)
    endAmount = serializers.IntegerField(read_only=True)


class OfferSerializer(serializers.ModelSerializer):
    itemType = serializers.IntegerField()
    token = serializers.CharField()
    identifierOrCriteria = serializers.CharField()
    startAmount = serializers.IntegerField()
    endAmount = serializers.IntegerField()

    class Meta:
        model = Offer
        fields = [
            "itemType",
            "token",
            "identifierOrCriteria",
            "startAmount",
            "endAmount"
        ]

    # def create(self, validated_data):
    #     offer_data = validated_data.pop('offer')
    #     offer = Offer.objects.create(**offer_data)
    #     return offer
