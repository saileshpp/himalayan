# Generated by Django 3.2.7 on 2022-11-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
