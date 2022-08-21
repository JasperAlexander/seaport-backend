from django.db import models
from api_orderconsiderations.models import OrderConsideration
from api_orderoffers.models import OrderOffer


class OrderParameter(models.Model):
    offerer = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    zoneHash = models.CharField(max_length=200)
    startTime = models.CharField(max_length=200)
    endTime = models.CharField(max_length=200)
    orderType = models.IntegerField()
    offer = models.ManyToManyField(OrderOffer, null=True)
    consideration = models.ManyToManyField(OrderConsideration, null=True)
    totalOriginalConsiderationItems = models.IntegerField()
    salt = models.CharField(max_length=200)
    conduitKey = models.CharField(max_length=200)
    counter = models.IntegerField()
