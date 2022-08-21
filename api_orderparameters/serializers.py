from rest_framework import serializers

from api_orderconsiderations.serializers import OrderConsiderationPublicSerializer, OrderConsiderationSerializer
from .models import OrderParameter
from api_orderoffers.serializers import OrderOfferSerializer, OrderOfferPublicSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class OrderParametersPublicSerializer(serializers.Serializer):
    offerer = serializers.CharField(read_only=True)
    zone = serializers.CharField(read_only=True)
    zoneHash = serializers.CharField(read_only=True)
    startTime = serializers.CharField(read_only=True)
    endTime = serializers.CharField(read_only=True)
    orderType = serializers.IntegerField(read_only=True)
    offer = OrderOfferPublicSerializer(read_only=True)
    consideration = OrderConsiderationPublicSerializer(read_only=True)
    totalOriginalConsiderationItems = serializers.IntegerField(read_only=True)
    salt = serializers.CharField(read_only=True)
    conduitKey = serializers.CharField(read_only=True)
    counter = serializers.IntegerField(read_only=True)


class OrderParametersSerializer(WritableNestedModelSerializer):
    offer = OrderOfferSerializer(many=True)
    consideration = OrderConsiderationSerializer(many=True)

    class Meta:
        model = OrderParameter
        fields = [
            "offerer",
            "zone",
            "zoneHash",
            "startTime",
            "endTime",
            "orderType",
            "offer",
            "consideration",
            "totalOriginalConsiderationItems",
            "salt",
            "conduitKey",
            "counter"
        ]
