from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    custemail = forms.EmailField(label="custemail", max_length=30, required=True)
    phone = forms.CharField(label="phone", max_length=12, required=True)
    topic = forms.CharField(label="topic",max_length=200,required=True)
    body = forms.CharField(label="body",max_length=2000, required=True)