# Generated by Django 3.2.7 on 2022-11-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
