# Generated by Django 3.2.7 on 2022-10-07 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('link', models.TextField(max_length=500)),
                ('img', models.ImageField(null=True, upload_to='img')),
                ('cat', models.CharField(choices=[('analyze', 'analyze'), ('audio', 'audio'), ('blog', 'blog'), ('creative', 'creative'), ('design', 'design'), ('expertize', 'expertize'), ('experiment', 'experiment'), ('express', 'express'), ('healthcare', 'healthcare'), ('muscle', 'muscle'), ('news', 'news'), ('power', 'power'), ('share', 'share'), ('slanting', 'slanting'), ('sustain', 'sustain'), ('video', 'video'), ('yoga', 'yoga')], default='blog', max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
