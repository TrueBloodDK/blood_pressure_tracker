from django.urls import path
from .views import (
    PressureRecordCreateView,
    PressureRecordLatestView,
    PressureStatisticsView,
    login_view,
    logout_view,
    dashboard_view,
    statistics_view,
)

urlpatterns = [
    path('records/create/', PressureRecordCreateView.as_view(), name='record-create'),
    path('records/latest/', PressureRecordLatestView.as_view(), name='record-latest'),
    path('records/statistics/', PressureStatisticsView.as_view(), name='record-statistics'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('statistics/', statistics_view, name='statistics'),
]