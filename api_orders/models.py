from django.db import models
from api_orderparameters.models import OrderParameter


class Order(models.Model):
    listing_time = models.CharField(max_length=100)
    expiration_time = models.CharField(max_length=100)
    cancelled = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)
    parameters = models.ForeignKey(
        OrderParameter, null=True, on_delete=models.SET_NULL)
    signature = models.CharField(max_length=200)
