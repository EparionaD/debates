from django.views.generic import TemplateView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_articles = Article.objects.all()
        all_galleries = Gallery.objects.all()
        all_forums = Forum.objects.all()
        context['all_news'] = sorted(
            chain(all_articles, all_galleries, all_forums),
            key=attrgetter('created'),
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