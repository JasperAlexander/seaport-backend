from django.db import models


class Item(models.Model):
    type = models.IntegerField()
    token = models.CharField(max_length=50)
    identifierOrCriteria = models.CharField(max_length=50)
    startAmount = models.IntegerField()
    endAmount = models.IntegerField()
    recipient = models.CharField(max_length=50)
