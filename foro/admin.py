from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ForumResource(resources.ModelResource):
    class Meta:
        model = Forum

class ForumAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title', 'author','category_article','date')
    search_fields = ('title','summary','content','descent','author__first_name','category__name')
    prepopulated_fields = {"slug":("title",)}
    resource_class = ForumResource

    def category_article(self, obj):
        return ",".join([c.name for c in obj.category.all()])
    category_article.short_description = "Categorías"

admin.site.register(Forum, ForumAdmin)