from email.policy import default
from pyexpat import model
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import URLField
from numpy import True_


class ContactMessage(models.Model):
    name = models.TextField(max_length=25)
    email = models.EmailField(max_length=224)
    message = models.TextField()

    # def __str__(self) -> str:
    #      return f'{self.name[:20]} {self.email}'


class HomeSlider(models.Model):
    image = models.ImageField(upload_to='img', null=True)
    # imagename = models.TextField(max_length=100)
    date_added = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.date_added


class About(models.Model):
    title = models.TextField(max_length=25)
    message = models.TextField()
    img = models.ImageField(upload_to='img', null=True)


class OurTeam(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ourteam', null=True)
    info = models.TextField()
    facebook_link = models.URLField(default="", null=True, blank=True)
    instagram_link = models.URLField(default="", null=True, blank=True)
    twitter_link = models.URLField(default="", null=True, blank=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials', null=True)
    spoken_words = models.TextField()


class OurStatus(models.Model):
    name = models.CharField(max_length=200)
    status = models.IntegerField()
