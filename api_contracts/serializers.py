from rest_framework import serializers
from .models import Contract


class ContractPublicSerializer(serializers.Serializer):
    address = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    schema_name = serializers.CharField(read_only=True)


class EventContractPublicSerializer(serializers.Serializer):
    address = serializers.CharField(read_only=True)


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "address",
            "name",
            "description",
            "schema_name"
        ]
