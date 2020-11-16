from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from author.models import Author
from category.models import Category

class Article(models.Model):
    title = models.CharField("Título", max_length=250)
    slug = models.SlugField("Slug", max_length=250, unique=True)
    descent = models.TextField("Bajada", max_length=500, null=True, blank=True)
    summary = RichTextField("Resumen", null=True, blank=True)
    content = RichTextUploadingField("Contenido",null=True, blank=True)
    photo_main = models.ImageField("Foto de portada", null=True, blank=True, upload_to="articulo")
    source = models.CharField("Fuente", max_length=250)
    author = models.ForeignKey(Author, verbose_name= "Autor", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name= "Categorías")
    date = models.DateTimeField("Fecha de publicación", default=timezone.now)
    created = models.DateTimeField("Fecha de creacción", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Fecha de edición", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)