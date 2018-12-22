from . import views
from django.urls import include, path
from .models import Car


from django.conf.urls.static import static
from django.conf import settings

app_name = 'listing'
urlpatterns = [
    path('new/', views.new.as_view(), name='newListing'),
    path('used/', views.used.as_view(), name='usedListing'),
    path('lease/', views.lease.as_view(), name='leaseListing'),
    path('new/<str:car_slug>', views.car_detail, name='detailListing')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)