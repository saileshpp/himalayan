# Generated by Django 3.2.7 on 2022-11-01 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20221101_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='highlight',
            field=models.TextField(max_length=500),
        ),
    ]