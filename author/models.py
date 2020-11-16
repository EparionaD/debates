from django.db import models

class Author(models.Model):
    first_name = models.CharField("Primer nombre", max_length=255, null=False, blank=False)
    second_name = models.CharField("Segundo nombre", default="", max_length=255, null=False, blank=False)
    last_name = models.CharField("Apellido paterno", default="", max_length=255, null=False, blank=False)
    last_name1 = models.CharField("Apellido materno", default="", max_length=255, null=False, blank=False)
    email =  models.EmailField("Correo electrónico", max_length=254, null=False, blank=False)
    created = models.DateTimeField(verbose_name="Fecha de creacción", auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['-created']

    def __str__(self):
        return self.first_name