from django.db import models


class Contract(models.Model):
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=20000)
