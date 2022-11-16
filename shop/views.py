from django.shortcuts import redirect, render
from shop.models import *
from django.core.paginator import Paginator


def shop(request):

    products = Product.objects.all()

    # Pagintaion
    paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    params = {
        'products': page_obj,
        'total_products': products.__len__,
        'page_num': page_num,
    }

    return render(request, 'pages/shop.html', params)


def product(request, id):
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product=product)
    more_products = Product.objects.order_by('?').exclude(id=id)[:4]
    url = request.META.get('HTTP_REFERER')
    print(url)
    if request.method == "GET":
        params = {
            'product': product,
            'total_reviews': reviews.__len__,
            'reviews': reviews,
            'more_products': more_products
        }
        return render(request, 'pages/product.html', params)
    else:
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        rating = request.POST['rating']

        create = Review.objects.create(
            name=name,
            rating=rating,
            email=email,
            review=message,
            product=product,
        )
        create.save()
        url = request.META.get('HTTP_REFERER')
        return redirect(url)


def order(request):
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        message = request.POST['message']
        email = request.POST['email']

        create = Order.objects.create(
            name=name,
            number=number,
            email=email,
            message=message
        )

        create.save()
        return redirect('shop')


def sorting(request):

    # # Pagintaion
    # paginator = Paginator(products, 4, orphans=2)
    # page_num = request.GET.get('page')
    # page_obj = paginator.get_page(page_num)

    # params = {
    #     'products': page_obj,
    #     'total_products': products.__len__,
    #     'page_num': page_num,
    # }
    return render(request, 'pages/shop.html')
