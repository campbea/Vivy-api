from rest_framework import serializers

from .models import Location


class LocationPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'title', 'summary', 'impact', 'image_url')

    def validate_title(self, value):
        if Location.objects.filter(title=value).exists():
            raise serializers.ValidationError(
                'location with title "{}" already exists'.format(value))
        return value

    def validate_image_url(self, value):
        if Location.objects.filter(image_url=value).exists():
            raise serializers.ValidationError(
                'location with image_url "{}" already exists'.format(value))
        return value


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'title', 'summary', 'impact', 'image_url', 'created_at', 'updated_at')
