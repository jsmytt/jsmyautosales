from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
# from .forms import CommentForm
from . import models
from .models import Car
from django.utils import timezone

# def listing_index(request):
#     return render(request, 'listing/new.html', {})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




class new(TemplateView):
    template_name = 'listing/new.html'
    def get(self, request,):
        posts = Car.object.filter(type="New", publish=True, created__lte=timezone.now()).order_by('-pk')
        page = request.GET.get('page', 1)

        paginator = Paginator(posts, 3)
        try:
            pag = paginator.page(page)
        except PageNotAnInteger:
            pag = paginator.page(1)
        except EmptyPage:
            pag = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'posts': posts, 'pag':pag})



class used(TemplateView):
    template_name = 'listing/used.html'
    def get(self, request,):
        posts = Car.object.filter(type="Used", publish=True, created__lte=timezone.now()).order_by('-pk')
        page = request.GET.get('page', 1)

        paginator = Paginator(posts, 3)
        try:
            pag = paginator.page(page)
        except PageNotAnInteger:
            pag = paginator.page(1)
        except EmptyPage:
            pag = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'posts': posts, 'pag':pag})


class lease(TemplateView):
    template_name = 'listing/rental.html'
    def get(self, request,):
        posts = Car.object.filter(type="Lease", publish=True, created__lte=timezone.now()).order_by('-pk')
        page = request.GET.get('page', 1)

        paginator = Paginator(posts, 3)
        try:
            pag = paginator.page(page)
        except PageNotAnInteger:
            pag = paginator.page(1)
        except EmptyPage:
            pag = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'posts': posts, 'pag':pag})

def usedsold(request):
    posts = Car.object.filter(type="Used", sold="Sold", publish=True, created__lte=timezone.now()).order_by('-pk')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        pag = paginator.page(1)
    except EmptyPage:
        pag = paginator.page(paginator.num_pages)

    return render(request, 'listing/used_sold.html', {'posts':posts, 'pag': pag})

def usedsale(request):
    posts = Car.object.filter(type="Used", sold="Sale", publish=True, created__lte=timezone.now()).order_by('-pk')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        pag = paginator.page(1)
    except EmptyPage:
        pag = paginator.page(paginator.num_pages)
    return render(request, 'listing/used_for_sale.html', {'posts':posts, 'pag': pag})


def car_detail(request,car_slug):

    car = get_object_or_404(Car, slug=car_slug)
    return render(request, 'listing/list_detail.html', {'car': car})

    # def get(self, request,):
    #     form = CommentForm()
    #     context = {
    #         'form': form,
    #     }
    #     return render(request, self.template_name, context)


    # queryset = models.Car.object.published()
    # template_name = "new.html"
    # paginate_by = 20

