from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Car, CarImg
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Min, Max
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

        cursor = connection.cursor()
        cursor.execute(
            'select listing_carimg.LImage, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = 1 and listing_car.type ="New" and listing_car.publish = 1 ORDER BY listing_car.created desc ')

        df = dictfetchall(cursor)

        posts = Car.object.filter(type="New", publish=True, created__lte=timezone.now()).order_by('-pk')
        page = request.GET.get('page', 1)
        car_img = CarImg.objects.filter(MainImage=True).order_by('-pk').select_related('car')

        paginator = Paginator(df, 3)
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

        cursor = connection.cursor()
        cursor.execute(
            'select listing_carimg.LImage, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = 1 and listing_car.type ="Used" and listing_car.publish = 1 ORDER BY listing_car.created desc ')

        df = dictfetchall(cursor)

        posts = Car.object.filter(type="Used", publish=True, created__lte=timezone.now()).order_by('-pk')
        page = request.GET.get('page', 1)

        paginator = Paginator(df, 3)
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
        cursor = connection.cursor()
        cursor.execute(
            'select listing_carimg.LImage, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = 1 and listing_car.type ="Lease" and listing_car.publish = 1 ORDER BY listing_car.created desc ')

        df = dictfetchall(cursor)
        posts = Car.object.filter(type="Lease", publish=True, created__lte=timezone.now()).order_by('-pk')
        page = request.GET.get('page', 1)

        paginator = Paginator(df, 3)
        try:
            pag = paginator.page(page)
        except PageNotAnInteger:
            pag = paginator.page(1)
        except EmptyPage:
            pag = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'posts': posts, 'pag':pag})

def usedsold(request):
    cursor = connection.cursor()
    cursor.execute(
        'select listing_carimg.LImage,listing_car.sold, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = 1 and listing_car.type ="Used" and listing_car.sold ="Sold" and listing_car.publish = 1 ORDER BY listing_car.created desc ')

    df = dictfetchall(cursor)
    posts = Car.object.filter(type="Used", sold="Sold", publish=True, created__lte=timezone.now()).order_by('-pk')
    page = request.GET.get('page', 1)

    paginator = Paginator(df, 3)
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        pag = paginator.page(1)
    except EmptyPage:
        pag = paginator.page(paginator.num_pages)

    return render(request, 'listing/used_sold.html', {'posts':posts, 'pag': pag})

def usedsale(request):
    cursor = connection.cursor()
    cursor.execute(
        'select listing_carimg.LImage,listing_car.sold, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = 1 and listing_car.type ="Used" and listing_car.sold ="Sale" and listing_car.publish = 1 ORDER BY listing_car.created desc ')
    df = dictfetchall(cursor)
    posts = Car.object.filter(type="Used", sold="Sale", publish=True, created__lte=timezone.now()).order_by('-pk')
    page = request.GET.get('page', 1)

    paginator = Paginator(df, 3)
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        pag = paginator.page(1)
    except EmptyPage:
        pag = paginator.page(paginator.num_pages)
    return render(request, 'listing/used_for_sale.html', {'posts':posts, 'pag': pag})

import re
def car_detail(request,car_slug):
    cursor = connection.cursor()

    car_name = re.sub(".*[s]+[l]+[u]+[g]+[\%]+[3]+[D]", "", str(request.build_absolute_uri()))
    query1 = 'select listing_carimg.LImage,listing_car.created,listing_car.body ,listing_car.sold, listing_car.price,listing_car.slug, listing_car.title from listing_car inner join listing_carimg on listing_car.id = listing_carimg.car_id where listing_carimg.mainimage = 1 and listing_car.slug = \"' \
             + str(car_name) + '\" ORDER BY listing_car.created desc '
    cursor.execute(query1)
    df = dictfetchall(cursor)



    return render(request, 'listing/list_detail.html', {'dfs': df[0],  })

    '''
    Car._meta.get_fields()
    [{'LImage':1}, {'LImage2':2}, {'LImage3':3}, {'LImage4':4}, {'LImage5':5}, {'LImage6':6}, {'LImage7':7}, {'LImage8':8}]
    Car.object.values_list('LImage2')
    Car.object.values_list('LImage2')[0] == (None,)
    for i in range(0,len(Car.object.values_list('LImage2'))):
        Car.object.values_list('LImage2')[i]

    
a=[]
a.append()
for i in range(0,len(Car._meta.get_fields())):
    a.append(re.sub('.*\.','',str(Car._meta.get_fields()[i])))
    '''
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


