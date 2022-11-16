from django.db import models
from tinymce import models as tinymce__models

class Retreat(models.Model):
    title = models.CharField( max_length=500)
    date_added = models.DateField(auto_now_add=True)
    body = tinymce__models.HTMLField(blank=False)
    img = models.ImageField(upload_to='retreat', null=True)
    included = tinymce__models.HTMLField(null=True)
    excluded = tinymce__models.HTMLField(null=True)
    know_before_you_go = tinymce__models.HTMLField(null=True)
    day_1 = models.TextField( max_length=500,null=True)
    day_2 = tinymce__models.HTMLField(null=True)
    day_3 = tinymce__models.HTMLField(null=True)
    day_4 = tinymce__models.HTMLField(null=True)
    day_5 = tinymce__models.HTMLField(null=True)
    day_6 = tinymce__models.HTMLField(null=True)
    day_7 = tinymce__models.HTMLField(null=True)
    day_8 = tinymce__models.HTMLField(null=True)
    day_9 = tinymce__models.HTMLField(null=True)
    day_10 = tinymce__models.HTMLField(null=True)
