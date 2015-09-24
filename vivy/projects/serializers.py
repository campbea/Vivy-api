from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        read_only_fields = (
            'id',
            'added_at',
            'updated'
        )
