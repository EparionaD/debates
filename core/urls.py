from django.urls import path
from core.views import IndexView, RazonesView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('nuestras-razones/', RazonesView.as_view(), name="razones"),
    #path('busqueda/', SearchView.as_view(), name="razones"),
]