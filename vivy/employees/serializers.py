from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        read_only_fields = (
            'id',
            'added_at',
            'updated'
        )
