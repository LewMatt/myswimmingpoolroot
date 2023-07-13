from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(required=True, label='Nazwisko')
    
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name','password1','password2']