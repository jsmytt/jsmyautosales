from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(label="username",max_length=2000,required=True)
    password = forms.CharField(label="password",widget=forms.PasswordInput, required=True)