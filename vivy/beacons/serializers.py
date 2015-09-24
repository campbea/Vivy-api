from rest_framework import serializers

from .models import Beacon


class BeaconPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beacon
        fields = ('id', 'beacon_id', 'location')


class BeaconSerializer(serializers.ModelSerializer):

    class meta:
        model = Beacon
        fields = ('id', 'beacon_id', 'location', 'created_at', 'updated')
