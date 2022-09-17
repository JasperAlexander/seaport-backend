from django.db import models
from api_contracts.models import Contract
from api_collections.models import Collection
from api_users.models import User
from api_tokens.models import Token


class Asset(models.Model):
    token_id = models.CharField(max_length=256)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    image_url = models.URLField(blank=True)
    external_link = models.URLField(blank=True)
    asset_contract = models.ForeignKey(
        Contract, null=True, on_delete=models.SET_NULL, related_name="asset_contract")
    collection = models.ForeignKey(
        Collection, null=True, on_delete=models.SET_NULL, related_name="collection")
    owner = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="owner")
    creator = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="creator")
    transfer_fee = models.IntegerField(default=0)
    transfer_fee_payment_token = models.ForeignKey(
        Token, null=True, blank=True, on_delete=models.SET_NULL, related_name="transfer_fee_payment_token")
    is_nsfw = models.BooleanField(default=False)
