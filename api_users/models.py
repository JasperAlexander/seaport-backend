from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    profile_img_url = models.URLField(blank=True)
    config = models.CharField(max_length=100, blank=True, choices=(
        ('verified', 'Verified'), ('moderator', 'Moderator')))
    created_timestamp = models.DateTimeField(auto_now_add=True)
