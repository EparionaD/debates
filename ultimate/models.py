from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from author.models import Author

class Ultimate(models.Model):
    title = models.CharField("Título", max_length=250)
    slug = models.SlugField("Slug", max_length=250, unique=True)
    photo_main = models.ImageField("Foto para miniatura", null=True, blank=True, upload_to="ultimas")
    url = models.URLField("Ingresa el Url", max_length=200)
    author = models.ForeignKey(Author, verbose_name= "Autor", on_delete=models.CASCADE)
    date = models.DateTimeField("Fecha de publicación", default=timezone.now)
    created = models.DateTimeField("Fecha de creacción", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Fecha de edición", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Última noticia"
        verbose_name_plural = "Últimas noticias"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Ultimate, self).save(*args, **kwargs)