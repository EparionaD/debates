from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path('', ArticleView.as_view(), name="articles"),
    path('todos/', AllArticlesView.as_view(), name="todos"),
    path('<slug:slug>/', CategoryView.as_view(), name="articles-category"),
    path('categoria/<slug:slug>/', AllCategoryView.as_view(), name="todos-category"),
    path('detalle/<slug:slug>/', ArticleDetailView.as_view(), name="article-detail"),
]