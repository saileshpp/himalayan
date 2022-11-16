from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from blog__app.models import Blog
from gallery.models import Gallery
from .models import *
from courses.models import Courses
from django.core.mail import send_mail
from HimalayanNadaNirvanaYoga import settings


def index(request):
    # GETING RECENT BLOGS
    recent__blogs = Blog.objects.order_by('-date_added')

    sliders = HomeSlider.objects.order_by('-date_added')
    about = About.objects.all
    courses = Courses.objects.order_by('-date_added')
    ourteams = OurTeam.objects.order_by('-id')
    testimonials = Testimonial.objects.order_by('-id')

    # GETTING OUR STATUS DATA
    ourStatusTotalUsers = OurStatus.objects.get(name='Total Users')
    ourStatusYearsofExperience = OurStatus.objects.get(
        name='Years of Experience')

    # GETING RECENT IMAGES FROM GALLERY
    recent__images = Gallery.objects.order_by('-date_added')

    params = {
        'blogs': recent__blogs[:3],
        'galleries': recent__images[:4],
        'sliders': sliders,
        'abouts': about,
        'courses': courses[:4],
        'ourteams': ourteams,
        'testimonials': testimonials,
        'ourStatusTotalUsers': ourStatusTotalUsers,
        'ourStatusYearsofExperience': ourStatusYearsofExperience,
    }
    return render(request, 'pages/index.html', params)


# CONTACT FUNCTION
def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        newmessage = ContactMessage.objects.create(
            name=name, email=email, message=message)
        newmessage.save()

        # send_mail('Contact', message, 'jerkinsailesh@gmail.com',
        #           ['shaileshpuzari@gmail.com'])

        # return render(request, 'pages/contact.html')
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

    else:
        return render(request, 'pages/contact.html')


def about(request):
    about = About.objects.all
    ourteams = OurTeam.objects.order_by('-id')
    testimonials = Testimonial.objects.order_by('-id')

    # GETTING OUR STATUS DATA
    ourStatusTotalUsers = OurStatus.objects.get(name='Total Users')
    ourStatusYearsofExperience = OurStatus.objects.get(
        name='Years of Experience')
    params = {
        'abouts': about,
        'ourteams': ourteams,
        'testimonials': testimonials,
        'ourStatusTotalUsers': ourStatusTotalUsers,
        'ourStatusYearsofExperience': ourStatusYearsofExperience,
    }
    return render(request, 'pages/about.html', params)


def singingbowl(request):
      return render(request, 'pages/singing__bowls.html')