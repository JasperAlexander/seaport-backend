from rest_framework import serializers
from .models import Order


class OrderPublicSerializer(serializers.Serializer):
    signature = serializers.CharField(read_only=True)
    numerator = serializers.IntegerField(read_only=True)
    denominator = serializers.IntegerField(read_only=True)
    extraData = serializers.CharField(read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "parameters",
            "signature",
            "numerator",
            "denominator",
            "extraData"
        ]
