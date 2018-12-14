from . import views
from django.urls import include, path
from .models import Car


app_name = 'listing'
urlpatterns = [
    path('new/', views.new.as_view(), name='newListing'),
    path('used/', views.used.as_view(), name='usedListing'),
    path('lease/', views.lease.as_view(), name='leaseListing'),
    path('new/<str:car_slug>', views.car_detail, name='detailListing')
]