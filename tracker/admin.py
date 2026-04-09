from django.contrib import admin
from .models import PressureRecord


@admin.register(PressureRecord)
class PressureRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'systolic', 'diastolic', 'pulse', 'created_at']
    list_filter = ['user', 'created_at']
    search_fields = ['user__username']
    ordering = ['-created_at']