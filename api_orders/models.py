from django.db import models
from api_orderparameters.models import OrderParameters


class Order(models.Model):
    parameters = models.ForeignKey(
        OrderParameters, null=True, on_delete=models.SET_NULL)
    signature = models.CharField(max_length=200)
