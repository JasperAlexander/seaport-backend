from rest_framework import serializers
from .models import OrderConsideration


class OrderConsiderationPublicSerializer(serializers.Serializer):
    itemType = serializers.IntegerField(read_only=True)
    token = serializers.CharField(read_only=True)
    identifierOrCriteria = serializers.CharField(read_only=True)
    startAmount = serializers.IntegerField(read_only=True)
    endAmount = serializers.IntegerField(read_only=True)
    recipient = serializers.CharField(read_only=True)


class OrderConsiderationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderConsideration
        fields = [
            "itemType",
            "token",
            "identifierOrCriteria",
            "startAmount",
            "endAmount",
            "recipient"
        ]
