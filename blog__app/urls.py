from django.urls import path
from blog__app import views

urlpatterns = [
    path('<int:id>', views.blogview, name='blog'),
    path('blogs', views.bloglisting, name='bloglisting'),
]
