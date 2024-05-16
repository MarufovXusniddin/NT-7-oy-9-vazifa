from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Category, Product
from .utils import CartAuthenticatedUser


# Create your views here.


def index(request):
    data = {
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'app/index.html', data)


def filter_products(request, id):
    data = {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(category_id=id)
    }
    return render(request, 'app/index.html', data)


def cart(request):
    if request.user.is_authenticated:
        product_id = request.POST.get('product_id')  # Productni identifikatori
        action = request.POST.get('action')  # Amal (add yoki delete)
        cart_info = CartAuthenticatedUser(request, product_id, action).get_cart_info()
        data = {
            'order_products': cart_info['order_products']
        }
        return render(request, 'app/cart.html', data)
    else:
        HttpResponse('Avval ro\'yxatdan o\'ting!')


def to_cart(request: HttpRequest, product_id, action):
    if request.user.is_authenticated:
        CartAuthenticatedUser(request, product_id, action)
        page = request.META.get('HTTP_REFERER')
        return redirect(page)
    else:
        HttpResponse('Avval ro\'yxatdan o\'ting!')


def detail(request, id):
    data = {
        'products': Product.objects.get(id=id)
    }
    return render(request, 'app/detail.html', data)
