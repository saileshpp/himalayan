from unicodedata import name
from venv import create
from django.shortcuts import render
from blog__app.models import Blog, Comment
from django.core.paginator import Paginator


def blogview(request, id):
    blog = Blog.objects.get(id=id)
    recent_blogs = Blog.objects.all().exclude(id=id)

    # Comments Funtion

    # Getting All Comments of the post and displaying
    comments = Comment.objects.filter(blog=blog)

    # Cleaner Parameter
    params = {
        'blog': blog,
        'recentblogs': recent_blogs[:6],
        'comments': comments,
    }

    # Posting A Comment
    if request.method == "GET":
        return render(request, 'pages/blog__detail.html', params)

    else:
        comment = request.POST['comment']
        author = request.POST['author']
        email = request.POST['email']

        create = Comment.objects.create(
            author=author,
            comment=comment,
            blog=blog,
            email=email,
        )

        create.save()
        return render(request, 'pages/blog__detail.html', params)
    # End Comments


def bloglisting(request):
    blog = Blog.objects.all()

    # Pagintaion
    paginator = Paginator(blog, 9)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    params = {
        'blogs': page_obj,
    }
    return render(request, 'pages/blog__listing.html', params)

