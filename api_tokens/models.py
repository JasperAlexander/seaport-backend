from django.db import models


class Token(models.Model):
    symbol = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    image_url = models.URLField(blank=True)
    name = models.CharField(max_length=50, blank=True)
    decimals = models.IntegerField()
    eth_price = models.IntegerField(blank=True)
    usd_price = models.FloatField(blank=True)
