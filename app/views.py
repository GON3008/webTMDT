from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.

def home(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    productsaler = ProductSale.objects.all()
    news = New.objects.all()
    context={
        'categorys': categorys,
        'products': products,
        'productsaler': productsaler,
        'news': news,
        }
    return render(request, 'app/home.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order ={'get_cart_items':0, 'get_cart_total':0}
    context={'items':items, 'order':order}
    return render(request, 'app/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order ={'get_cart_items':0, 'get_cart_total':0}
    context={'items':items, 'order':order}
    return render(request, 'app/checkout.html', context)

def product_content_1(request):
    context={}
    return render(request, 'app/product/product_content_1.html')


   