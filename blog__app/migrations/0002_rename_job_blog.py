# Generated by Django 3.2.7 on 2022-10-07 03:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog__app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Blog',
        ),
    ]
