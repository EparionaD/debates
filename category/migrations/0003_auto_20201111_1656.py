# Generated by Django 3.1.3 on 2020-11-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=250, verbose_name='Slug'),
        ),
    ]