from rest_framework import serializers

from .models import Beacon
from locations.serializers import LocationSerializer


class BeaconPostPutSerializer(serializers.ModelSerializer):

    beacon_uuid = serializers.CharField(min_length=32, max_length=32)

    class Meta:
        model = Beacon
        fields = ('id', 'beacon_uuid', 'location')


class BeaconSerializer(serializers.ModelSerializer):

    beacon_uuid = serializers.CharField(min_length=32, max_length=32)
    location = LocationSerializer()

    class Meta:
        model = Beacon
        fields = ('id', 'beacon_uuid', 'location', 'created_at', 'updated_at')
