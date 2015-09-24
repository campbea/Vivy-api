from django.db import models

from locations.models import Location

# BEACON_ID_LENGTH = 15  # ask Kyle


class Beacon(models.Model):

    beacon_uuid = models.CharField(max_length=32, unique=True)
    location = models.OneToOneField(Location)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
