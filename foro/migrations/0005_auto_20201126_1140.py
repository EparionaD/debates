# Generated by Django 3.1.3 on 2020-11-26 16:40

from django.db import migrations
from django.contrib.postgres.operations import UnaccentExtension


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0004_auto_20201119_2011'),
    ]

    operations = [
        UnaccentExtension()
    ]