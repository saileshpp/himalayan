from email.policy import default
from django.db import models
from tinymce import models as tinymce__models

LANGUAGE__CHOICE = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
]
LEVEL__CHOICES = [
    ('Beginner', 'Beginner'),
    ('Experienced-Beginner', 'Experienced-Beginner'),
    ('Experienced', 'Experienced'),
    ('Intermediate', 'Intermediate'),
    ('Intermediate-Advanced', 'Intermediate-Advanced'),
    ('Advanced', 'Advanced'),
]
STYLE__CHOICES = [
    ('Ashtanga Vinyasa-style', 'Ashtanga Vinyasa-style'),
]


# class Pictures(models.Model):
#     picture = models.ImageField(upload_to='courses/')


class Courses(models.Model):

    title = models.TextField(max_length=100)
    body = tinymce__models.HTMLField(blank=False)
    date_added = models.DateField()
    img = models.ImageField(upload_to='img', null=True)
    duration = models.DurationField()
    language = models.CharField(
        max_length=100, choices=LANGUAGE__CHOICE, default='ENG')
    level = models.CharField(
        max_length=100, choices=LEVEL__CHOICES, default='BEG')
    style = models.CharField(
        max_length=100, choices=STYLE__CHOICES, default='AVS')
    price = models.IntegerField(default=1, blank=False)
    discounted_price = models.IntegerField(null=True, blank=True)
    # picture = models.ForeignKey(
    #     Pictures, default=1, on_delete=models.CASCADE, null=True)
