from rest_framework import serializers
from .models import OrderParameters
from api_orderoffers.serializers import OfferPublicSerializer, OfferSerializer
from api_orderconsiderations.serializers import ConsiderationPublicSerializer, ConsiderationSerializer
from api_orderoffers.models import Offer
from api_orderconsiderations.models import Consideration
from drf_writable_nested.serializers import WritableNestedModelSerializer


class OrderParametersPublicSerializer(serializers.ModelSerializer):
    offerer = serializers.CharField(read_only=True)
    zone = serializers.CharField(read_only=True)
    zoneHash = serializers.CharField(read_only=True)
    startTime = serializers.CharField(read_only=True)
    endTime = serializers.CharField(read_only=True)
    orderType = serializers.IntegerField(read_only=True)
    # offer: OfferPublicSerializer(read_only=True)
    # consideration: ConsiderationPublicSerializer(read_only=True)
    totalOriginalConsiderationItems = serializers.IntegerField(read_only=True)
    salt = serializers.CharField(read_only=True)
    conduitKey = serializers.CharField(read_only=True)
    counter = serializers.IntegerField(read_only=True)


class OrderParametersSerializer(WritableNestedModelSerializer):
    # offer = OfferSerializer(many=True)
    # consideration = ConsiderationSerializer(many=True)

    class Meta:
        model = OrderParameters
        fields = [
            "offerer",
            "zone",
            "zoneHash",
            "startTime",
            "endTime",
            "orderType",
            # "offer",
            # "consideration",
            "totalOriginalConsiderationItems",
            "salt",
            "conduitKey",
            "counter"
        ]

    def create(self, validated_data):
        offer_data = validated_data.pop('offer')
        consideration_data = validated_data.pop('consideration')
        orderparameters = OrderParameters.objects.create(**validated_data)
        for offers in offer_data:
            Offer.objects.create(**offer_data)
        for considerations in consideration_data:
            Consideration.objects.create(**consideration_data)
    # #     # Offer.objects.create(orderparameters=orderparameters, **offer_data)
    # #     # Consideration.objects.create(
    # #     #     orderparameters=orderparameters, **consideration_data)
        return orderparameters
