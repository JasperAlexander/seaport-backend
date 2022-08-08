from rest_framework import serializers
from .models import Event


class EventPublicSerializer(serializers.Serializer):
    type = serializers.CharField(read_only=True)
    created_timestamp = serializers.DateTimeField(read_only=True)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "type",
            "created_timestamp"
        ]
