from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
# /products -> index
# Uniform Resource Locator (Address)

def index(request):
    products = Product.objects.all()               # returns all the products that we have in our DB
    return render(request, 'index.html', {'products': products})
#   return HttpResponse('Hello World')

def new(request):
    return HttpResponse('New Products')

