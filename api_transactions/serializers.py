from rest_framework import serializers
from .models import Transaction
# from api_users.serializers import UserBundleSerializer


class TransactionPublicSerializer(serializers.Serializer):
    block_hash = serializers.CharField(read_only=True)
    block_number = serializers.CharField(read_only=True)
    hash = serializers.CharField(read_only=True)
    index = serializers.CharField(read_only=True)
    created_timestamp = serializers.DateTimeField(read_only=True)


class TransactionSerializer(serializers.ModelSerializer):
    # from_account = UserBundleSerializer(read_only=True)
    # to_account = UserBundleSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "block_hash",
            "block_number",
            "hash",
            "index",
            # "from_account",
            # "to_account",
            "created_timestamp"
        ]
