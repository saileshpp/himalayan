# Generated by Django 3.2.7 on 2022-10-07 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog__app', '0002_rename_job_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='link',
        ),
    ]