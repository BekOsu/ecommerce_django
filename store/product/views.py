from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
 

def index(request):
    x = {'pro':Product.objects.all()}
    return render(request, 'product/index.html', x)

def cart(request): 
    return render(request, 'product/cart.html')

# def product(request): 
#     return render(request, 'products/productt.html')

# def products(request): 
#     return render(request, 'products/products.html', {'name':'ahmed'})

