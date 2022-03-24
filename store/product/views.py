from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'product/index.html')


def cart(request):
    pass
 