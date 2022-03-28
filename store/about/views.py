from django.shortcuts import render
from .models import Login
from .forms import Loginform

 
def about(request):
   if request.method == 'POST':

      dataform = Loginform(request.POST)
      
      if dataform.is_valid():
          dataform.save()   
    
   return render(request, 'about/about.html', {'lf':Loginform})


    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # data = Login (username=username, password=password)
    # data.save() 
    
    
    