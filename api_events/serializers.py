from rest_framework import serializers
from api_tokens.serializers import TokenBundleSerializer

from api_users.serializers import UserBundleSerializer
from .models import Event
from api_assets.serializers import EventAssetSerializer
from api_tokens.models import Token
from api_users.models import User


class EventReadSerializer(serializers.ModelSerializer):
    asset = EventAssetSerializer(read_only=True)
    from_account = UserBundleSerializer(read_only=True)
    to_account = UserBundleSerializer(read_only=True)
    payment_token = TokenBundleSerializer(read_only=True)

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


class EventWriteSerializer(serializers.ModelSerializer):
    asset = EventAssetSerializer(read_only=True)
    from_account = serializers.SlugRelatedField(
        slug_field='address', queryset=User.objects.all())
    to_account = serializers.SlugRelatedField(
        slug_field='address', queryset=User.objects.all(), required=False)
    payment_token = serializers.SlugRelatedField(
        slug_field='address', queryset=Token.objects.all(), required=False)

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
