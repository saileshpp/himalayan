from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('singingbowl/', views.singingbowl, name='singingbowl'),
    # path('contact/message', views.contactmessage, name='contactmessage'),
    # path('jobview/<int:id>', views.jobview, name='jobview'),
]
