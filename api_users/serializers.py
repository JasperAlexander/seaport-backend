from rest_framework import serializers
from .models import User


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    profile_img_url = serializers.URLField(read_only=True)
    config = serializers.CharField(read_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "address",
            "profile_img_url",
            "config"
        ]