from django.shortcuts import render
from matplotlib import image
from .models import Gallery


def getimages(request):
    images = Gallery.objects.all()
    images = images.order_by('-date_added')
    return render(request, 'pages/gallery.html', {'imgs': images})
