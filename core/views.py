from django.views.generic import TemplateView, ListView
from django.db.models import Q
from itertools import chain
from operator import attrgetter

from article.models import *
from gallery.models import *
from foro.models import *
from category.models import *
from agenda.models import *
from ultimate.models import *


class IndexView(TemplateView):
    template_name = 'core/index.html'

    
    def get_template_names(self):
        if self.request.GET.get("buscar"):
            return ['core/search.html']
        else:
            return ['core/index.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_articles = Article.objects.all()
        all_galleries = Gallery.objects.all()
        all_forums = Forum.objects.all()

        consulta = self.request.GET.get("buscar")

        if consulta:
            all_articles = Article.objects.filter(
                Q(title__unaccent__icontains = consulta) |
                Q(descent__unaccent__icontains = consulta) |
                Q(summary__unaccent__icontains = consulta) |
                Q(content__unaccent__icontains = consulta)
            ).distinct()
            all_gallery = Gallery.objects.filter(
                Q(title__unaccent__icontains = consulta) |
                Q(descent__unaccent__icontains = consulta)
            ).distinct()
            all_forum = Forum.objects.filter(
                Q(title__unaccent__icontains = consulta) |
                Q(descent__unaccent__icontains = consulta)
            ).distinct()

            context['all_search'] = sorted(
                chain(all_articles, all_gallery, all_forum),
                key=attrgetter('created'),
                reverse=True
            )
            return context

        context['all_news'] = sorted(
            chain(all_articles, all_galleries, all_forums),
            key=attrgetter('date'),
            reverse=True
        )
        context['all_normalidad'] = Article.objects.filter(category__slug = "nueva-normalidad")
        context['all_debates'] = Article.objects.filter(category__slug = "debates")
        context['all_forum'] = all_forums
        context['all_gallery'] = all_galleries
        context['all_observatorio'] = Article.objects.filter(category__slug = "observatorio")
        context['all_opinion'] = Article.objects.filter(category__slug = "opinion")
        context['all_schedule'] = Schedule.objects.all()
        context['all_ultimate'] = Ultimate.objects.all()
        return context

class RazonesView(TemplateView):
    template_name = 'core/razones.html'


"""
class SearchView(ListView):
    template_name = 'core/search.html'
    paginate_by = 8

    def get_queryset(self):
        consulta = self.kwargs['buscar']

        all_articles = Article.objects.filter(
            Q(title__unaccent__icontains = consulta) |
            Q(descent__unaccent__icontains = consulta) |
            Q(summary__unaccent__icontains = consulta) |
            Q(content__unaccent__icontains = consulta)
        ).distinct()
        all_gallery = Gallery.objects.filter(
            Q(title__unaccent__icontains = consulta) |
            Q(descent__unaccent__icontains = consulta)
        ).distinct()
        all_forum = Forum.objects.filter(
            Q(title__unaccent__icontains = consulta) |
            Q(descent__unaccent__icontains = consulta)
        ).distinct()

        queryset = sorted(
            chain(all_articles, all_gallery, all_forum),
            key=attrgetter('created'),
            reverse=True
        )

        return queryset"""