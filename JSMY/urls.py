"""JSMY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic import TemplateView
from . import views
admin.site.site_header = "JSMY Administration Portal"
admin.site.site_title = "JSMY Admin"
#admin.site.index_title = ""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.banner.as_view(), name='index'),
    path('', include('listing.urls')),
    path('email/',views.email,name='email'),
    path('jsmycalculator/',views.calculator,name='calculator'),
    path('search/', views.search, name='search'),
    path('haninfinance/', views.hanin, name='hanin'),
path('program/', views.programImg, name='program'),
path('migrationservice/', views.migrationImg, name='migration'),
path('rentalservice/', views.rentalImg, name='rental'),
path('monthlylease/', views.leasedealImg1, name='lease'),
]






