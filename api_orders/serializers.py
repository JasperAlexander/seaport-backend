from rest_framework import serializers
from .models import Order
from api_orderparameters.serializers import OrderParametersSerializer, OrderParametersPublicSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class OrderBundleSerializer(serializers.Serializer):
    listing_time = serializers.CharField(read_only=True)
    expiration_time = serializers.CharField(read_only=True)
    cancelled = serializers.BooleanField(read_only=True)
    finalized = serializers.BooleanField(read_only=True)
    parameters = OrderParametersPublicSerializer(read_only=True)
    signature = serializers.CharField(read_only=True)


class OrderReadSerializer(serializers.ModelSerializer):
    parameters = OrderParametersSerializer()

    class Meta:
        model = Order
        fields = [
            "id",
            "listing_time",
            "expiration_time",
            "cancelled",
            "finalized",
            "parameters",
            "signature"
        ]


class OrderWriteSerializer(WritableNestedModelSerializer):
    parameters = OrderParametersSerializer()

    class Meta:
        model = Order
        fields = [
            "listing_time",
            "expiration_time",
            "cancelled",
            "finalized",
            "parameters",
            "signature"
        ]
