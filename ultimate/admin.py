from django.contrib import admin
from .models import *

class UltimateAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title', 'author','date')
    search_fields = ('title','author__first_name')
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Ultimate, UltimateAdmin)