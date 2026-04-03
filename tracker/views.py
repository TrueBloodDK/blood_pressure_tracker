from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from .models import PressureRecord
from .serializers import PressureRecordSerializer


class PressureRecordCreateView(generics.CreateAPIView):
    """Создание новой записи давления"""
    serializer_class = PressureRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PressureRecordLatestView(APIView):
    """Получение последней записи давления"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        record = PressureRecord.objects.filter(user=request.user).first()

        if not record:
            return Response(
                {'detail': 'Записей не найдено.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PressureRecordSerializer(record)
        return Response(serializer.data)


class PressureStatisticsView(APIView):
    """Статистика давления за сутки или месяц"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        period = request.query_params.get('period')  

        if period == 'day':
            since = timezone.now() - timedelta(days=1)
        elif period == 'month':
            since = timezone.now() - timedelta(days=30)
        else:
            return Response(
                {'detail': 'Укажите period: day или month.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        records = PressureRecord.objects.filter(
            user=request.user,
            created_at__gte=since
        )

        if not records.exists():
            return Response(
                {'detail': f'Записей за указанный период нет.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Считаем статистику
        systolic_values = list(records.values_list('systolic', flat=True))
        diastolic_values = list(records.values_list('diastolic', flat=True))
        pulse_values = list(records.values_list('pulse', flat=True))

        stats = {
            'period': period,
            'records_count': records.count(),
            'systolic': {
                'avg': round(sum(systolic_values) / len(systolic_values), 1),
                'min': min(systolic_values),
                'max': max(systolic_values),
            },
            'diastolic': {
                'avg': round(sum(diastolic_values) / len(diastolic_values), 1),
                'min': min(diastolic_values),
                'max': max(diastolic_values),
            },
            'pulse': {
                'avg': round(sum(pulse_values) / len(pulse_values), 1),
                'min': min(pulse_values),
                'max': max(pulse_values),
            },
        }

        return Response(stats)