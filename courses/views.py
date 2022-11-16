from django.shortcuts import render
from .models import Courses


def viewCourse(request, id):
    course = Courses.objects.get(id=id)
    return render(request, 'pages/course__detail.html', {'course': course})
