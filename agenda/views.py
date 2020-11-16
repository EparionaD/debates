from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import *

class ScheduleView(TemplateView):
    template_name = 'agenda/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_schedule = Schedule.objects.all()
        context['all_schedule'] = all_schedule
        return context

class ScheduleDetailView(DetailView):
    model = Schedule
    context_object_name = 'schedule'
    template_name = 'agenda/schedule_detail.html'