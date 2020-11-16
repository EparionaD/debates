from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path('', ArticleView.as_view(), name="articles"),
    path('<slug:slug>/', CategoryView.as_view(), name="articles-category"),
    path('detalle/<slug:slug>/', ArticleDetailView.as_view(), name="article-detail"),
]