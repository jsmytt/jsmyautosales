from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Car
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CarImg
from django.db import connection

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

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

        cursor = connection.cursor()
        cursor.execute(
            'select * from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id')

        df = dictfetchall(cursor)

        return render(request, self.template_name, {'posts': posts, 'pag':pag,'df':df})



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

        cursor = connection.cursor()
        cursor.execute(
            'select * from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id')

        df = dictfetchall(cursor)

        return render(request, self.template_name, {'posts': posts, 'pag':pag,'df':df})


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

        cursor = connection.cursor()
        cursor.execute(
            'select * from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id')

        df = dictfetchall(cursor)

        return render(request, self.template_name, {'posts': posts, 'pag':pag,'df':df})


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
    ImgOnly = CarImg.objects.filter()
    return render(request, 'listing/list_detail.html', {'car': car,'ImgOnly':ImgOnly})


def faq(request):
    posts = Car.object.filter(type="faq", sold="Sale", publish=True, created__lte=timezone.now()).order_by('-pk')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        pag = paginator.page(1)
    except EmptyPage:
        pag = paginator.page(paginator.num_pages)
    return render(request, 'listing/faq.html', {'posts':posts, 'pag': pag})

