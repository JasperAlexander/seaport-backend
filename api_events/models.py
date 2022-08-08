from django.db import models


class Event(models.Model):
    type = models.CharField(max_length=50)
    created_timestamp = models.DateTimeField()
