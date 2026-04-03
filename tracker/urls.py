from django.urls import path
from .views import (
    PressureRecordCreateView,
    PressureRecordLatestView,
    PressureStatisticsView,
)

urlpatterns = [
    path('records/create/', PressureRecordCreateView.as_view(), name='record-create'),
    path('records/latest/', PressureRecordLatestView.as_view(), name='record-latest'),
    path('records/statistics/', PressureStatisticsView.as_view(), name='record-statistics'),
]