from rest_framework import serializers

from api_users.serializers import UserPublicSerializer
from .models import Event
from api_assets.serializers import EventAssetSerializer
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
            "from_account",
            "to_account",
            "start_time",
            "end_time",
            "start_amount",
            "end_amount",
            "payment_token",
            "is_private",
            "created_timestamp"
        ]

    def create(self, validated_data):
        request = self.context['request']
        validated_data['from_account_id'] = request.data.get(
            'from_account')
        validated_data['to_account_id'] = request.data.get('to_account')
        validated_data['payment_token_id'] = request.data.get('payment_token')

        instance = super().create(validated_data)

        return instance
