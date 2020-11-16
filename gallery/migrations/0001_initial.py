# Generated by Django 3.1.3 on 2020-11-09 15:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0002_auto_20201108_2100'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('summary', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Resumen')),
                ('photo_thumbnail', models.ImageField(blank=True, null=True, upload_to='articulo/miniatura', verbose_name='Foto de portada')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacción')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author', verbose_name='Autor')),
                ('category', models.ManyToManyField(to='category.Category', verbose_name='Categorías')),
            ],
            options={
                'verbose_name': 'Galería',
                'verbose_name_plural': 'Galerías',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galeria', verbose_name='Agregar fotografías')),
                ('summary', models.CharField(blank=True, max_length=500, null=True, verbose_name='Resumen')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.gallery')),
            ],
            options={
                'verbose_name': 'Imágen para la galería',
                'verbose_name_plural': 'Imágenes para la galería',
            },
        ),
    ]
