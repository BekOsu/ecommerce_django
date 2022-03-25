from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='product'),
    
    path('cart/', views.cart, name='cart'),
    
    # path('productt/', views.cart, name='productt'),
    
    # path('products/', views.cart, name='products'),
    
]