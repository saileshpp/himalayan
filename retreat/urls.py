from django.urls import path
from retreat import views

urlpatterns = [
    path('', views.retreat, name='retreat'),
]
