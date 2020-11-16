from django.views.generic import TemplateView

from .models import *

class GalleyView(TemplateView):
    template_name = 'gallery/galleries.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_gallery = Gallery.objects.all()
        context['all_gallery'] = all_gallery
        return context

class GalleryDetailView(TemplateView):
    template_name = 'gallery/gallery_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_gallery = Gallery.objects.get(slug=kwargs['slug'])
        all_img = ImageGallery.objects.filter(gallery=all_gallery)
        all_videos = VideoGallery.objects.filter(video=all_gallery)
        context['detalle'] = all_gallery
        context['detalle_img'] = all_img
        context['detalle_video'] = all_videos
        return context