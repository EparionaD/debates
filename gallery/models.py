from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from author.models import Author
from category.models import Category

class Gallery(models.Model):
    title = models.CharField("Título", max_length=250)
    slug = models.SlugField("Slug", max_length=250, unique=True)
    descent = models.TextField("Bajada", max_length=500, null=True, blank=True)
    photo_main = models.ImageField("Foto para miniatura", null=True, blank=True, upload_to="galeria")
    author = models.ForeignKey(Author, verbose_name= "Autor", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name= "Categorías")
    date = models.DateTimeField("Fecha de publicación", default=timezone.now)
    created = models.DateTimeField("Fecha de creacción", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField("Fecha de edición", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Galería"
        verbose_name_plural = "Galerías"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)

class ImageGallery(models.Model):
    gallery = models.ForeignKey(Gallery, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField("Agregar fotografías", upload_to="galeria/imagen", null=True, blank=True)
    summary = models.CharField("Descripción", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Imágen para la galería"
        verbose_name_plural = "Imágenes para la galería"

class VideoGallery(models.Model):
    video = models.ForeignKey(Gallery, null=True, blank=True, on_delete=models.CASCADE)
    url = models.URLField("Url del video", max_length=150, null=True, blank=True)
    image = models.ImageField("Agregar fotografías", upload_to="galeria/video", null=True, blank=True)
    summary = models.CharField("Descripción", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Url del video para la galería"
        verbose_name_plural = "Urls de los videos para la galería"