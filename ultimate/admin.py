from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UltimateResource(resources.ModelResource):
    class Meta:
        model = Ultimate

class UltimateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title', 'author','date')
    search_fields = ('title','author__first_name')
    prepopulated_fields = {"slug":("title",)}
    resource_class = UltimateResource

admin.site.register(Ultimate, UltimateAdmin)