# Generated by Django 3.2.7 on 2022-10-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
            ],
        ),
    ]
