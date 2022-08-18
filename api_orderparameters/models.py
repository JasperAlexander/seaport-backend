from django.db import models
from api_orderoffers.models import Offer
from api_orderconsiderations.models import Consideration


class OrderParameters(models.Model):
    offerer = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    zoneHash = models.CharField(max_length=200)
    startTime = models.CharField(max_length=200)
    endTime = models.CharField(max_length=200)
    orderType = models.IntegerField()
    offer: models.ManyToManyField(
        Offer, null=True, related_name='offer')
    consideration: models.ManyToManyField(
        Consideration, null=True, related_name='consideration')
    totalOriginalConsiderationItems = models.IntegerField()
    salt = models.CharField(max_length=200)
    conduitKey = models.CharField(max_length=200)
    counter = models.IntegerField()
