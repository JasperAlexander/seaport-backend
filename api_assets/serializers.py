from rest_framework import serializers
from .models import Asset
from api_contracts.serializers import ContractPublicSerializer, EventContractPublicSerializer
from api_collections.serializers import CollectionPublicSerializer
from api_users.serializers import UserBundleSerializer
from api_tokens.serializers import TokenBundleSerializer
from api_contracts.models import Contract
from api_tokens.models import Token
from api_users.models import User
from api_collections.models import Collection


class EventAssetSerializer(serializers.Serializer):
    token_id = serializers.CharField(read_only=True)
    asset_contract = EventContractPublicSerializer(read_only=True)


class AssetBundleSerializer(serializers.Serializer):
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
    transfer_fee_payment_token = TokenBundleSerializer(read_only=True)
    is_nsfw = serializers.BooleanField(read_only=True)


class AssetReadSerializer(serializers.ModelSerializer):
    asset_contract = ContractPublicSerializer(read_only=True)
    collection = CollectionPublicSerializer(read_only=True)
    owner = UserBundleSerializer(read_only=True)
    creator = UserBundleSerializer(read_only=True)
    transfer_fee_payment_token = TokenBundleSerializer(read_only=True)

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
            "transfer_fee_payment_token",
            "is_nsfw"
        ]


class AssetWriteSerializer(serializers.ModelSerializer):
    asset_contract = serializers.SlugRelatedField(
        slug_field='address', queryset=Contract.objects.all())
    collection = serializers.SlugRelatedField(
        slug_field='slug', queryset=Collection.objects.all())
    owner = serializers.SlugRelatedField(
        slug_field='address', queryset=User.objects.all())
    creator = serializers.SlugRelatedField(
        slug_field='address', queryset=User.objects.all())
    transfer_fee_payment_token = serializers.SlugRelatedField(
        slug_field='address', queryset=Token.objects.all())

    class Meta:
        model = Asset
        fields = [
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
            "transfer_fee_payment_token",
            "is_nsfw"
        ]
