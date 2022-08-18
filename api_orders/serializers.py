from rest_framework import serializers
from .models import Order
from api_orderparameters.serializers import OrderParametersPublicSerializer, OrderParametersSerializer
from api_orderparameters.models import OrderParameters
from drf_writable_nested.serializers import WritableNestedModelSerializer


class OrderReadSerializer(serializers.Serializer):
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

    # def create(self, validated_data):
    #     parameters_data = validated_data.pop('parameters')
    #     order = Order.objects.create(**validated_data)
    #     OrderParameters.objects.create(**parameters_data)
    #     return order
