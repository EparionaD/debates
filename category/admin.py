from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Category, CategoryAdmin)
