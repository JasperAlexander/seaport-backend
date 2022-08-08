from rest_framework import serializers
from .models import Item


class ItemPublicSerializer(serializers.Serializer):
    type = serializers.IntegerField(read_only=True)
    token = serializers.CharField(read_only=True)
    identifierOrCriteria = serializers.CharField(read_only=True)
    startAmount = serializers.IntegerField(read_only=True)
    endAmount = serializers.IntegerField(read_only=True)
    recipient = serializers.CharField(read_only=True)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "type",
            "token",
            "identifierOrCriteria",
            "startAmount",
            "endAmount",
            "recipient"
        ]
