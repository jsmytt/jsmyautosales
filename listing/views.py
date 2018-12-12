from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
# from .forms import CommentForm
from . import models
from .models import Car
from django.utils import timezone

# def listing_index(request):
#     return render(request, 'listing/newlisting.html', {})


class ListingIndex(TemplateView):
    template_name = 'listing/newlisting.html'

    def get(self, request,):
        posts = Car.object.filter(created__lte=timezone.now()).order_by('created')
        return render(request, self.template_name, {'posts': posts})

def car_detail(request, pk):
    carlist = get_object_or_404(Car, pk=pk)
    return render(request, 'listing/list_detail.html', {'carlist': carlist})

    # def get(self, request,):
    #     form = CommentForm()
    #     context = {
    #         'form': form,
    #     }
    #     return render(request, self.template_name, context)


    # queryset = models.Car.object.published()
    # template_name = "newlisting.html"
    # paginate_by = 20

