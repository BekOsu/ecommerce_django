from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    x={'product':'car',
       'price':'45'}
    
    return render(request, 'product/index.html', x)

def cart(request):
   
    
    return render(request, 'product/cart.html')
