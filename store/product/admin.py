from django.contrib import admin

from .models import Product, Test

admin.site.register(Product)
admin.site.register(Test)