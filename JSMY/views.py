from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
# from .forms import CommentForm
from listing.models import Car
from django.utils import timezone

class banner(TemplateView):
    template_name = 'index.html'
    def get(self, request,):
        new = Car.object.filter(type="New", created__lte=timezone.now()).order_by('created')
        lennew=len(Car.object.filter(type="New", created__lte=timezone.now()).order_by('created'))
        used = Car.object.filter(type="Used", created__lte=timezone.now()).order_by('created')
        lenused=len(Car.object.filter(type="Used", created__lte=timezone.now()).order_by('created'))
        lease = Car.object.filter(type="Lease", created__lte=timezone.now()).order_by('created')
        lenlease=len(Car.object.filter(type="Lease", created__lte=timezone.now()).order_by('created'))



        context = {"new":new,"used":used,"lease":lease,"lennew":lennew,"lenused":lenused,"lenlease":lenlease

                   }
        return render(request, self.template_name, context)
