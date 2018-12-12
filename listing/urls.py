from . import views
from django.urls import include, path

app_name = 'listing'
urlpatterns = [
    path('newlisting', views.ListingIndex.as_view(), name='newlisting'),
    path('newlisting/<int:pk>/', views.car_detail, name='car_detail')
]