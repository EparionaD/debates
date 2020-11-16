from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    slug = models.SlugField("Slug", max_length=250, unique=True)
    created = models.DateTimeField(verbose_name="Fecha de creacción", auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)