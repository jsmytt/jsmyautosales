from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from listing.models import Car, CarImg
from django.utils import timezone
from banner.models import banner as bn
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from .forms import LoginForm


from django.db import connection




def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]





class banner(TemplateView):
    template_name = 'index.html'
    def get(self, request,):
        new = Car.object.filter(type="New", publish=True, created__lte=timezone.now()).order_by('-pk')
        lennew=len(Car.object.filter(type="New", publish=True, created__lte=timezone.now()).order_by('-pk'))
        #used = Car.object.filter(type="Used", publish=True, created__lte=timezone.now()).order_by('-pk').all()
        lenused=len(Car.object.filter(type="Used", publish=True, created__lte=timezone.now()).order_by('-pk'))
        lease = Car.object.filter(type="Lease", publish=True, created__lte=timezone.now()).order_by('-pk')
        lenlease=len(Car.object.filter(type="Lease", publish=True, created__lte=timezone.now()).order_by('-pk'))
        cursor = connection.cursor()
        cursor.execute(
            'select listing_carimg.LImage, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = 1 and listing_car.type ="Used" ORDER BY listing_car.created desc ')

        dfUsed = dictfetchall(cursor)
        cursor.execute(
            'select listing_carimg.LImage, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = 1 and listing_car.type ="Lease" ORDER BY listing_car.created desc ')

        dfLease = dictfetchall(cursor)

        context = {"new":new,"lease":lease,"lennew":lennew,"lenused":lenused,"lenlease":lenlease, 'dfUsed':dfUsed,'dfLease':dfLease


                   }
        return render(request, self.template_name, context)



def email(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        custemail = form.cleaned_data.get('custemail')
        phone_number = form.cleaned_data.get('phone')
        subject = form.cleaned_data.get('topic')
        message = "Customer Email:" +"  "+ custemail +"\n"+"\n"+ "Customer Phone Number:" +"  "+ phone_number +"\n"+"\n"+ form.cleaned_data.get('body')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['jsmyautosales@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
    return redirect('index')


def calculator(request):
    return render(request, 'listing/calculator.html',{})