from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from itertools import chain
from operator import attrgetter

from article.models import *
from gallery.models import *
from foro.models import *


class ArticleView(TemplateView):
    template_name = 'article/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_articles = Article.objects.all()
        all_gallery = Gallery.objects.all()
        all_forum = Forum.objects.all()
        context['all_articles'] = sorted(
            chain(all_articles, all_gallery, all_forum),
            key=attrgetter('created'),
            reverse=True
        )

        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'detalle'
    template_name = 'article/article_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_articles = Article.objects.all()
        all_galleries = Gallery.objects.all()
        all_forum = Forum.objects.all()
        context['all_news'] = sorted(
            chain(all_articles, all_galleries, all_forum),
            key=attrgetter('created'),
            reverse=True
        )
        return context

class CategoryView(TemplateView):
    template_name = 'article/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_articles = Article.objects.filter(category__slug=kwargs['slug'])
        all_galleries = Gallery.objects.filter(category__slug=kwargs['slug'])
        all_forum = Forum.objects.filter(category__slug=kwargs['slug'])
        context['all_articles'] = sorted(
            chain(all_articles, all_galleries, all_forum),
            key=attrgetter('created'),
            reverse=True
        )
        return context

class AllArticlesView(ListView):
    #model =  Article
    template_name = 'article/all_article.html'
    context_object_name = 'all'
    
    all_articles = Article.objects.all()
    all_gallery = Gallery.objects.all()
    all_forum = Forum.objects.all()
    paginate_by = 6

    queryset = sorted(
            chain(all_articles, all_gallery, all_forum),
            key=attrgetter('created'),
            reverse=True
        )[10:]

class AllCategoryView(ListView):
    template_name = 'article/all_article.html'
    context_object_name = 'all'
    paginate_by = 6

    def get_queryset(self):
        cat = self.kwargs['slug']

        all_articles = Article.objects.filter(category__slug=cat)
        all_galleries = Gallery.objects.filter(category__slug=cat)
        all_forum = Forum.objects.filter(category__slug=cat)
    
        queryset = sorted(
            chain(all_articles, all_galleries, all_forum),
            key=attrgetter('created'),
            reverse=True
        )
        return queryset