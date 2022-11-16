from operator import mod
from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce__models


class Blog(models.Model):

    TAGS = (
        ('analyze', 'analyze'),
        ('audio', 'audio'),
        ('blog', 'blog'),
        ('creative', 'creative'),
        ('design', 'design'),
        ('expertize', 'expertize'),
        ('experiment', 'experiment'),
        ('express', 'express'),
        ('healthcare', 'healthcare'),
        ('muscle', 'muscle'),
        ('news', 'news'),
        ('power', 'power'),
        ('share', 'share'),
        ('slanting', 'slanting'),
        ('sustain', 'sustain'),
        ('video', 'video'),
        ('yoga', 'yoga'),
    )

    title = models.CharField(max_length=200, blank=False)
    body = tinymce__models.HTMLField(blank=False)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img', null=True)
    cat = models.CharField(max_length=100, choices=TAGS, default='blog')

    def __str__(self):
        return self.title


class Comment(models.Model):
    sn = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=500, null=False)
    date_added = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.TextField(max_length=20, null=False)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.author
