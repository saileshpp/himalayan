# Generated by Django 3.2.7 on 2022-10-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_about_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('position', models.EmailField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='ourteam')),
                ('info', models.TextField()),
            ],
        ),
    ]
