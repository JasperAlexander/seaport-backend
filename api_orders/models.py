from django.db import models
from api_items.models import Item


class OrderParameteters(models.Model):
    offerer = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    offer: models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    consideration: models.ForeignKey(
        Item, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=50)
    zoneHash = models.CharField(max_length=50)
    salt = models.CharField(max_length=50)
    conduitKey = models.CharField(max_length=50)  # part of item?
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    # zonehash, salt, conduitKey, counter, extraCheap, signer, timeflag, criteriaresolvers


class Order(models.Model):
    parameters = models.ForeignKey(
        OrderParameteters, null=True, on_delete=models.SET_NULL)
    signature = models.CharField(max_length=50)
    numerator = models.IntegerField()
    denominator = models.IntegerField()
    extraData = models.CharField(max_length=50)
