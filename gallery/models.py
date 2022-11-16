from django.db import models


class Gallery(models.Model):
    img = models.ImageField(upload_to='gallery/')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.date_added