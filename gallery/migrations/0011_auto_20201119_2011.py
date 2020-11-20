# Generated by Django 3.1.3 on 2020-11-20 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_auto_20201112_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo_main',
            field=models.ImageField(blank=True, null=True, upload_to='galeria', verbose_name='Foto para miniatura'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='galeria/imagen', verbose_name='Agregar fotografías'),
        ),
        migrations.AlterField(
            model_name='videogallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='galeria/video', verbose_name='Agregar fotografías'),
        ),
    ]
