from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.getimages, name='gallery'),
    # path('jobview/<int:id>', views.jobview, name='jobview'),
]
