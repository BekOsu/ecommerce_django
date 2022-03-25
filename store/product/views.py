from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
 

def index(request):
    
    return render(request, 'product/index.html', {'pro':Product.objects.all()})

def cart(request): 
    return render(request, 'product/cart.html')

# def product(request): 
#     return render(request, 'products/productt.html')

# def products(request): 
#     return render(request, 'products/products.html', {'name':'ahmed'})

