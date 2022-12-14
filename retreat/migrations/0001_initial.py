# Generated by Django 4.1.3 on 2022-11-11 05:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Retreat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('body', tinymce.models.HTMLField()),
                ('img', models.ImageField(null=True, upload_to='retreat')),
            ],
        ),
    ]
