from django.views.generic import TemplateView
from django.views.generic.detail import DetailView


from .models import *

class ForumView(TemplateView):
    template_name = 'foro/forums.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_forum = Forum.objects.all()
        context['all_articles'] = all_forum
        return context

class ForumDetailView(DetailView):
    model = Forum
    context_object_name = 'forum'
    template_name = 'foro/forum_detail.html'