# Generated by Django 3.1.3 on 2020-11-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='descent',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Bajada'),
        ),
    ]