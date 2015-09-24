from rest_framework import serializers

from .models import Location


class LocationPostSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=128)
    summary = serializers.CharField()
    impact = serializers.CharField()
    image_url = serializers.URLField(max_length=256)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'title', 'summary', 'image_url', 'added_at', 'updated')
