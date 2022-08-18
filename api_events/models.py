from django.db import models
from api_assets.models import Asset
from api_users.models import User
from api_tokens.models import Token


class Event(models.Model):
    type = models.CharField(max_length=50, choices=(
        ('created', 'Created'),
        ('succesfull', 'Succesfull'),
        ('cancelled', 'Cancelled'),
        ('bid_entered', 'Bid entered'),
        ('bid_withdrawn', 'Bid withdrawn'),
        ('transfer', 'Transfer'),
        ('offer_entered', 'Offer entered'),
        ('approve', 'Approve')
    ))
    asset = models.ForeignKey(Asset, null=True, on_delete=models.SET_NULL)
    created_timestamp = models.DateTimeField(auto_created=True)
    from_account = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="from_account")
    to_account = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL, related_name="to_account")
    is_private = models.BooleanField(default=False)
    payment_token = models.ForeignKey(
        Token, null=True, on_delete=models.SET_NULL)
    quantity = models.FloatField()
    total_price = models.FloatField()
