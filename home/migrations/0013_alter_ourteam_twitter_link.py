# Generated by Django 3.2.7 on 2022-10-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_ourteam_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='twitter_link',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
