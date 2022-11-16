from email.policy import default
from django.db import models
from tinymce import models as tinymce__models


class Product(models.Model):

    title = models.CharField(max_length=100)
    highlight = models.TextField(max_length=500)
    body = tinymce__models.HTMLField(blank=False)
    date_added = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='img', null=True)
    price = models.IntegerField(default=1, blank=False)
    discounted_price = models.IntegerField(null=True, blank=True)
    # picture = models.ForeignKey(
    #     Pictures, default=1, on_delete=models.CASCADE, null=True)


class Review(models.Model):
    sn = models.AutoField(primary_key=True)
    review = models.TextField(max_length=500)
    date_added = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    email = models.EmailField(max_length=254)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.rating}'


class Order(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField(max_length=500)
    message = models.TextField()
    location = models.CharField(max_length=200, default="")
    date_added = models.DateField(auto_now_add=True)
