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
        BImage1 = bn.objects.values()[0]['bimage1']
        BImage2 = bn.objects.values()[0]['bimage2']
        BImage3 = bn.objects.values()[0]['bimage3']
        BImage4 = bn.objects.values()[0]['bimage4']
        BImage5 = bn.objects.values()[0]['bimage5']
        Blink1 = bn.objects.values()[0]['blink1']
        Blink2 = bn.objects.values()[0]['blink2']
        Blink3 = bn.objects.values()[0]['blink3']
        Blink4 = bn.objects.values()[0]['blink4']
        Blink5 = bn.objects.values()[0]['blink5']


        cursor = connection.cursor()

        cursor.execute("select listing_carimg.limage ,listing_car.sold, listing_car.price, listing_car.slug, listing_car.title, listing_carimg.mainimage from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = True and listing_car.type = 'Used' and listing_car.sold = 'Sale' and listing_car.publish = True ORDER BY listing_car.id desc")
        dfUsed = dictfetchall(cursor)

        cursor.execute(
            "select listing_carimg.limage, listing_car.price, listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = True and listing_car.type ='Lease' and listing_car.publish = True ORDER BY listing_car.id desc")
        dfLease = dictfetchall(cursor)

        context = {"new":new, "lease":lease, "lennew":lennew, "lenused":lenused, "lenlease":lenlease, 'dfUsed':dfUsed,'dfLease':dfLease,
                   "BImage1": BImage1, "BImage2": BImage2, "BImage3": BImage3, "BImage4": BImage4, "BImage5": BImage5,
                   "Blink1": Blink1, "Blink2": Blink2, "Blink3": Blink3, "Blink4": Blink4, "Blink5": Blink5,
                   }
        return render(request, self.template_name, context)

def email(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        custemail = form.cleaned_data.get('custemail')
        phone_number = form.cleaned_data.get('phone')
        subject = form.cleaned_data.get('topic')
        name = form.cleaned_data.get('name')
        service = form.cleaned_data.get('service')
        message = name+"\n"+"\n"+"Customer Email:" +"  "+ custemail +"\n"+"\n"+ "Customer Phone Number:" +"  "+ phone_number +"\n"+"\n"+"Service Type:" +"  "+ service +"\n"+"\n"+ " " +"\n"+"\n"+form.cleaned_data.get('body')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['justin@jsmyautosales.com']
        send_mail( subject, message, email_from, recipient_list )
    return redirect('index')

def calculator(request):
    CalImg1 = bn.objects.values()[0]['hanin']
    return render(request, 'listing/calculator.html',{'CalImg1':CalImg1})

def hanin(request):
    CalImg1 = bn.objects.values()[0]['hanin']
    return render(request, 'listing/hanin.html',{'CalImg1':CalImg1})

def programImg(request):
    proImg = bn.objects.values()[0]['program']
    return render(request, 'listing/programimg.html',{'proImg':proImg})
def leasedealImg1(request):
    leaseImg = bn.objects.values()[0]['leasedeal']
    return render(request, 'listing/leaseimg.html',{'leaseImg':leaseImg})
def rentalImg(request):
    rentalImg1 = bn.objects.values()[0]['rental']
    return render(request, 'listing/rentalimg.html',{'rentalImg1':rentalImg1})
def migrationImg(request):
    migrationImg1 = bn.objects.values()[0]['migration']
    return render(request, 'listing/migimg.html',{'migrationImg1':migrationImg1})







def search(request):
    if request.method == 'GET':
        car_name = request.GET.get('search')
        try:
            cursor = connection.cursor()
            cursor.execute(
                'select listing_carimg.limage, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = True and listing_car.publish = 1 and listing_car.slug= \"' + car_name + '\" ORDER BY listing_car.created desc '
            )

            dfUsed = dictfetchall(cursor)
            ImgOnly = CarImg.objects.filter()
            status = Car.object.filter(title__icontains=car_name, publish=True,).order_by('-pk')
            return render(request,'listing/search.html',{"carsearch":status, 'ImgOnly':ImgOnly})
        except:
            status=''
    else:
        return render(request,'listing/search.html',{})









