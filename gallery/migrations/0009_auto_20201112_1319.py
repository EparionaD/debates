# Generated by Django 3.1.3 on 2020-11-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20201111_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogallery',
            name='summary',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='summary',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción'),
        ),
    ]