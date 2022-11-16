from django.urls import path
from courses import views

urlpatterns = [
    path('<int:id>', views.viewCourse, name='viewcourse'),
    # path('jobview/<int:id>', views.jobview, name='jobview'),
]
