from django.contrib.admin.decorators import register
from gallery.models import ImageGallery
from django.contrib import admin
from .models import ImageGallery, VideoGallery, Gallery
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery

class ImageGalleryAdmin(admin.StackedInline):
    model = ImageGallery

class VideoGalleryAdmin(admin.StackedInline):
    model = VideoGallery

class GalleryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title', 'author','category_article','date')
    search_fields = ('title','summary','content','descent','author__first_name','category__name')
    prepopulated_fields = {"slug":("title",)}
    inlines = [ ImageGalleryAdmin, VideoGalleryAdmin ]
    resource_class = GalleryResource

    class Meta:
        model = Gallery

    def category_article(self, obj):
        return ",".join([c.name for c in obj.category.all()])
    category_article.short_description = "Categorías"

admin.site.register(Gallery, GalleryAdmin)