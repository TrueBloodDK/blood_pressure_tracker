from rest_framework import serializers
from .models import PressureRecord


class PressureRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressureRecord
        fields = ['id', 'systolic', 'diastolic', 'pulse', 'created_at']
        read_only_fields = ['created_at']  