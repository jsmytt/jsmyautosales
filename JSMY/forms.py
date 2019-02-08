from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

service_choice=[("New", "New Vehicles"), ("Used", "Used Vehicles")]

class LoginForm(forms.Form):
    name = forms.CharField(label="name", max_length=30, required=False)
    custemail = forms.EmailField(label="custemail", max_length=30, required=True)
    phone = forms.CharField(label="phone", max_length=12, required=True)
    topic = forms.CharField(label="topic",max_length=200,required=True)
    body = forms.CharField(label="body", max_length=2000, required=True)
    service = forms.CharField(label="service", max_length=100, required=False)


class SearchForm(forms.Form):
    searchfield = forms.CharField(label="searchfield", max_length=75, required=True)



