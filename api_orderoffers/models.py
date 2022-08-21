from django.db import models


class OrderOffer(models.Model):
    itemType = models.IntegerField(choices=((0, 'Native'), (1, 'ERC20'), (2, 'ERC721'), (
        3, 'ERC1155'), (4, 'ERC721 with criteria'), (5, 'ERC1155 with criteria')))
    token = models.CharField(max_length=200)
    identifierOrCriteria = models.CharField(max_length=200)
    startAmount = models.IntegerField()
    endAmount = models.IntegerField()
