from django.shortcuts import render
from .models import *

def retreat(request):
    retreats = Retreat.objects.all
    return render(request, 'pages/retreat.html', {'retreats':retreats})