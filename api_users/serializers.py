from rest_framework import serializers
from .models import User


class UserBundleSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    profile_img_url = serializers.URLField(read_only=True)
    config = serializers.CharField(read_only=True)
    created_timestamp = serializers.DateTimeField(read_only=True)


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "address",
            "profile_img_url",
            "config",
            "created_timestamp"
        ]


class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "address",
            "profile_img_url",
            "config",
            "created_timestamp"
        ]
