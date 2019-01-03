from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Car
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CarImg

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

        ImgOnly=CarImg.objects.filter()


        return render(request, self.template_name, {'posts': posts, 'pag':pag,'ImgOnly':ImgOnly})



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
    ImgOnly = CarImg.objects.filter()
    return render(request, 'listing/list_detail.html', {'car': car,'ImgOnly':ImgOnly})

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
