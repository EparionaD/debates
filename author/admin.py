from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','last_name1','email')

admin.site.register(Author, AuthorAdmin)
