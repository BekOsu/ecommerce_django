from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='product'),
    
    path('cart/', views.cart, name='cart'),
    
   
    
]