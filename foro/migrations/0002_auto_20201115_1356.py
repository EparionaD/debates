# Generated by Django 3.1.3 on 2020-11-15 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forum',
            options={'ordering': ['-created'], 'verbose_name': 'Foro', 'verbose_name_plural': 'Foros'},
        ),
    ]
