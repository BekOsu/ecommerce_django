from warnings import catch_warnings
from django.db import models
from datetime import datetime

class Product(models.Model):
    
    x = [
         
       ('phone','phone'), 
       ('food','food')   
         
         
         ]
    
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    code= models.IntegerField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    activate = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=x)
    
    def __str__(self):
       return self.name
   
    class Meta:
       verbose_name = 'product_list'
       ordering = ['price']
       
       
class Test(models.Model):  
     date = models.DateField()
     time = models.TimeField(null=True)
     create = models.DateTimeField(default=datetime.now)
     