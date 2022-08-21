from django.db import models
from api_orderparameters.models import OrderParameter


class Order(models.Model):
    parameters = models.ForeignKey(
        OrderParameter, null=True, on_delete=models.SET_NULL)
    signature = models.CharField(max_length=200)
