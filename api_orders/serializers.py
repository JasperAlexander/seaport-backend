from rest_framework import serializers
from .models import Order
from api_orderparameters.serializers import OrderParametersSerializer, OrderParametersPublicSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class OrderPublicSerializer(serializers.Serializer):
    parameters = OrderParametersPublicSerializer(read_only=True)
    signature = serializers.CharField(read_only=True)


class OrderSerializer(WritableNestedModelSerializer):
    parameters = OrderParametersSerializer()

    class Meta:
        model = Order
        fields = [
            "parameters",
            "signature"
        ]
