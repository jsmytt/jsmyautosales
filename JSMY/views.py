from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from listing.models import Car
from django.utils import timezone
from banner.models import banner as bn
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from .forms import LoginForm

class banner(TemplateView):
    template_name = 'index.html'
    def get(self, request,):
        new = Car.object.filter(type="New", publish=True, created__lte=timezone.now()).order_by('-pk')
        lennew=len(Car.object.filter(type="New", publish=True, created__lte=timezone.now()).order_by('-pk'))
        used = Car.object.filter(type="Used", publish=True, created__lte=timezone.now()).order_by('-pk')
        lenused=len(Car.object.filter(type="Used", publish=True, created__lte=timezone.now()).order_by('-pk'))
        lease = Car.object.filter(type="Lease", publish=True, created__lte=timezone.now()).order_by('-pk')
        lenlease=len(Car.object.filter(type="Lease", publish=True, created__lte=timezone.now()).order_by('-pk'))
        BImage1 = bn.objects.values()[0]['BImage1']
        BImage2 = bn.objects.values()[0]['BImage2']
        BImage3 = bn.objects.values()[0]['BImage3']
        BImage4 = bn.objects.values()[0]['BImage4']
        BImage5 = bn.objects.values()[0]['BImage5']
        Blink1 = bn.objects.values()[0]['Blink1']
        Blink2 = bn.objects.values()[0]['Blink2']
        Blink3 = bn.objects.values()[0]['Blink3']
        Blink4 = bn.objects.values()[0]['Blink4']
        Blink5 = bn.objects.values()[0]['Blink5']


        context = {"new":new,"used":used,"lease":lease,"lennew":lennew,"lenused":lenused,"lenlease":lenlease,
                   "BImage1":BImage1, "BImage2":BImage2, "BImage3":BImage3, "BImage4":BImage4, "BImage5":BImage5,
                   "Blink1":Blink1, "Blink2":Blink2, "Blink3":Blink3, "Blink4":Blink4, "Blink5":Blink5
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