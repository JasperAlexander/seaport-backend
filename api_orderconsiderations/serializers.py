from rest_framework import serializers

from api_orderparameters.models import OrderParameters
from .models import Consideration


class ConsiderationPublicSerializer(serializers.Serializer):
    itemType = serializers.IntegerField(read_only=True)
    token = serializers.CharField(read_only=True)
    identifierOrCriteria = serializers.CharField(read_only=True)
    startAmount = serializers.IntegerField(read_only=True)
    endAmount = serializers.IntegerField(read_only=True)
    recipient = serializers.CharField(read_only=True)


class ConsiderationSerializer(serializers.ModelSerializer):
    itemType = serializers.IntegerField()
    token = serializers.CharField()
    identifierOrCriteria = serializers.CharField()
    startAmount = serializers.IntegerField()
    endAmount = serializers.IntegerField()
    recipient = serializers.CharField()

    class Meta:
        model = Consideration
        fields = [
            "itemType",
            "token",
            "identifierOrCriteria",
            "startAmount",
            "endAmount",
            "recipient"
        ]

    # def create(self, validated_data):
    #     consideration_data = validated_data.pop('consideration')
    #     consideration = Consideration.objects.create(**consideration_data)
    #     return consideration
