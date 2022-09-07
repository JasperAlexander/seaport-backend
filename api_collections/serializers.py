from rest_framework import serializers
from .models import Collection
# from api_tokens.serializers import TokenSerializer


class CollectionPublicSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    created_timestamp = serializers.DateTimeField(read_only=True)
    banner_image_url = serializers.URLField(read_only=True)
    image_url = serializers.URLField(read_only=True)
    external_url = serializers.URLField(read_only=True)
    twitter_username = serializers.CharField(read_only=True)
    instagram_username = serializers.CharField(read_only=True)
    medium_username = serializers.CharField(read_only=True)
    is_nsfw = serializers.BooleanField(read_only=True)
    # payment_tokens = TokenSerializer(read_only=True)


class CollectionSerializer(serializers.ModelSerializer):
    # payment_tokens = TokenSerializer(read_only=True, many=True)

    class Meta:
        model = Collection
        fields = [
            "name",
            "description",
            "slug",
            "created_timestamp",
            "banner_image_url",
            "image_url",
            "external_url",
            "twitter_username",
            "instagram_username",
            "medium_username",
            "is_nsfw",
            # "payment_tokens"
        ]
