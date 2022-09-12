from rest_framework import serializers
from .models import Asset
from api_contracts.serializers import ContractPublicSerializer, EventContractPublicSerializer
from api_collections.serializers import CollectionPublicSerializer
from api_users.serializers import UserBundleSerializer
# from api_tokens.serializers import TokenBundleSerializer


class EventAssetSerializer(serializers.Serializer):
    token_id = serializers.CharField(read_only=True)
    asset_contract = EventContractPublicSerializer(read_only=True)
    listing_date = serializers.CharField(read_only=True)


class AssetPublicSerializer(serializers.Serializer):
    token_id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    image_url = serializers.URLField(read_only=True)
    external_link = serializers.URLField(read_only=True)
    asset_contract = ContractPublicSerializer(read_only=True)
    collection = CollectionPublicSerializer(read_only=True)
    owner = UserBundleSerializer(read_only=True)
    creator = UserBundleSerializer(read_only=True)
    transfer_fee = serializers.IntegerField(read_only=True)
    # transfer_fee_payment_token = TokenBundleSerializer(read_only=True)
    is_nsfw = serializers.BooleanField(read_only=True)


class AssetSerializer(serializers.ModelSerializer):
    asset_contract = ContractPublicSerializer(read_only=True)
    collection = CollectionPublicSerializer(read_only=True)
    owner = UserBundleSerializer(read_only=True)
    creator = UserBundleSerializer(read_only=True)
    # transfer_fee_payment_token = TokenBundleSerializer(read_only=True)

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
            "transfer_fee",
            # "transfer_fee_payment_token",
            "is_nsfw"
        ]

    def create(self, validated_data):
        request = self.context['request']
        validated_data['asset_contract_id'] = request.data.get(
            'asset_contract')
        validated_data['collection_id'] = request.data.get('collection')
        validated_data['owner_id'] = request.data.get('owner')
        validated_data['creator_address'] = request.data.get('creator')

        instance = super().create(validated_data)

        return instance
