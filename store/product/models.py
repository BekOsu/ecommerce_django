from django.db import models


class Product(models.Model):
    
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    code= models.IntegerField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    activate = models.BooleanField(default=True)
    
    def __str__(self):
       return self.name