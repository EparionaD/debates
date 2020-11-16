from django.urls import path
from .views import *

app_name = 'gallery'

urlpatterns = [
    path('', GalleyView.as_view(), name="galleries"),
    path('<slug:slug>/', GalleryDetailView.as_view(), name="gallery-detail"),
]