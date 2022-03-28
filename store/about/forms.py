from django import forms
from .models import Login


class Loginform(forms.ModelForm):
     class Meta:
         model = Login
         fields = '__all__'
    
    
    
    
    
    # class Loginform(forms.Form):
    # username = forms.CharField(max_length=50)
    # password = forms.CharField(max_length=50, widget=forms.PasswordInput)