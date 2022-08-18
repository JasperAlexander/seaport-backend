from rest_framework import serializers
from .models import Event
from api_assets.serializers import EventAssetSerializer
from api_users.serializers import UserPublicSerializer
from api_tokens.serializers import TokenPublicSerializer


class EventPublicSerializer(serializers.Serializer):
    type = serializers.CharField(read_only=True)
    created_timestamp = serializers.DateTimeField(read_only=True)


class EventSerializer(serializers.ModelSerializer):
    asset = EventAssetSerializer(read_only=True)
    from_account = UserPublicSerializer(read_only=True)
    to_account = UserPublicSerializer(read_only=True)
    payment_token = TokenPublicSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "type",
            "asset",
            "created_timestamp",
            "from_account",
            "to_account",
            "is_private",
            "payment_token",
            "quantity",
            "total_price"
        ]
