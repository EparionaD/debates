from django.urls import path
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', ForumView.as_view(), name="forums"),
    path('<slug:slug>/', ForumDetailView.as_view(), name="forum-detail"),
]