from django.urls import path
from .views import *

app_name = 'schedule'

urlpatterns = [
    path('', ScheduleView.as_view(), name="schedule_all"),
    path('<slug:slug>/', ScheduleDetailView.as_view(), name="schedule-detail"),
]