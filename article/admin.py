from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title', 'author','category_article','date')
    search_fields = ('title','summary','content','descent','author__first_name','category__name')
    prepopulated_fields = {"slug":("title",)}

    def category_article(self, obj):
        return ",".join([c.name for c in obj.category.all()])
    category_article.short_description = "Categorías"

admin.site.register(Article, ArticleAdmin)