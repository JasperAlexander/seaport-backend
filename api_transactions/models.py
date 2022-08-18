from django.db import models
# from api_users.models import User


class Transaction(models.Model):
    block_hash = models.CharField(max_length=50)
    block_number = models.CharField(max_length=50)
    hash = models.CharField(max_length=50)
    index = models.CharField(max_length=50)
    # from_account = models.ForeignKey(
    #     User, null=True, on_delete=models.SET_NULL, related_name="from_account")
    # to_account = models.ForeignKey(
    #     User, null=True, on_delete=models.SET_NULL, related_name="to_account")
    created_timestamp = models.DateTimeField()
