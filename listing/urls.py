from . import views
from django.urls import include, path
from .models import Car


from django.conf.urls.static import static
from django.conf import settings

app_name = 'listing'
urlpatterns = [
    path('new/', views.new.as_view(), name='newListing'),
    path('used/', views.used.as_view(), name='usedListing'),
    path('usedsold/', views.usedsold, name='sold'),
    path('usedsale/', views.usedsale, name='sale'),
    path('rental/', views.lease.as_view(), name='rentalListing'),
    path('new/<str:car_slug>', views.car_detail, name='detailListing'),
    path('faq/', views.faq, name='faq'),
    path('contactus/', views.TemplateView.as_view(template_name='listing/contactus.html'), name='contactus')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)