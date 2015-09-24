
from django.db import models


class Location(models.Model):

    title = models.CharField(max_length=128, unique=True)
    summary = models.TextField(blank=True)
    impact = models.TextField(blank=True)
    image_url = models.URLField(max_length=256, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
