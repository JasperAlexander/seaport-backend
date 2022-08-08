from rest_framework import serializers
from .models import Asset
from api_contracts.serializers import ContractPublicSerializer
from api_collections.serializers import CollectionPublicSerializer
from api_users.serializers import UserPublicSerializer


class AssetSerializer(serializers.ModelSerializer):
    asset_contract = ContractPublicSerializer(read_only=True)
    collection = CollectionPublicSerializer(read_only=True)
    owner = UserPublicSerializer(read_only=True)
    creator = UserPublicSerializer(read_only=True)

    class Meta:
        model = Asset
        fields = [
            "id",
            "token_id",
            "name",
            "description",
            "image_url",
            "external_link",
            "asset_contract",
            "collection",
            "owner",
            "creator",
            "last_sale",
            "transfer_fee",
            "transfer_fee_payment_token",
            "orders",
            "is_nsfw"
        ]
