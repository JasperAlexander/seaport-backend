from django.db import models
# from api_tokens.models import Token


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=20000, blank=True)
    slug = models.CharField(max_length=50)
    created_timestamp = models.DateTimeField(auto_created=True)
    banner_image_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    external_url = models.URLField(blank=True)
    twitter_username = models.CharField(max_length=50, blank=True)
    instagram_username = models.CharField(max_length=50, blank=True)
    medium_username = models.CharField(max_length=50, blank=True)
    is_nsfw = models.BooleanField(default=False)
    # payment_tokens = models.ManyToManyField(Token, null=True)
