from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from author.models import Author
from category.models import Category

class Schedule(models.Model):
    title = models.CharField("Título", max_length=250)
    slug = models.SlugField("Slug", max_length=250, unique=True)
    descent = models.TextField("Bajada", max_length=500, null=True, blank=True)
    photo_main = models.ImageField("Foto para miniatura", null=True, blank=True, upload_to="agenda")
    author = models.ForeignKey(Author, verbose_name= "Autor", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name= "Categorías")
    date = models.DateTimeField("Fecha de publicación", default=timezone.now)
    created = models.DateTimeField("Fecha de creacción", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Fecha de edición", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Schedule, self).save(*args, **kwargs)