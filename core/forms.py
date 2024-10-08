from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm (AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-3/4 py-4 px-6 rounded-xl'
    }))
    
    
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-3/4 py-4 px-6 rounded-xl'
    }))
        

class SignupForm(UserCreationForm):
    class Meta:
        model =User
        fields =('username','email','password1','password2',)
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-3/4 py-4 px-6 rounded-xl'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email address',
        'class': 'w-3/4 py-4 px-6 rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-3/4 py-4 px-6 rounded-xl'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': 'w-3/4 py-4 px-6 rounded-xl'
    }))

