# Generated by Django 3.2.7 on 2022-10-15 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]