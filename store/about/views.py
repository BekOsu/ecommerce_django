from django.shortcuts import render
from.models import Login

 
def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = Login (username=username, password=password)
    data.save() 
    
    
    return render(request, 'about/about.html')