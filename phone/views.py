
from django.shortcuts import get_list_or_404, render, get_object_or_404
from phone.models import Brand, Color, Phone
from django.db.models import Q
from django.core.paginator import Paginator
from phone.utils import q_search

def index(request, slug=None):
    brands = Brand.objects.all()
    page = request.GET.get('page', 1)
    ramrom_filters = request.GET.getlist('ramrom', None)
    color_filters = request.GET.getlist('цвет', None)
    search = request.GET.get('q')
    discount = request.GET.get('discount', None)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    phones_count = Phone.objects.all().count()
    
    if slug == 'all' or not slug:
        phones = Phone.objects.all()
        current_brand = None
    else:
        phones = Phone.objects.filter(brand__slug=slug)
        current_brand = get_list_or_404(Brand, slug=slug)

    if search:
        phones = q_search(search)
        print(search)

    ramrom_q = Q()
    if ramrom_filters:
        for filter_val in ramrom_filters:
            rom, ram = map(int, filter_val.split('-'))
            ramrom_q |= Q(ram=ram, rom=rom)
    
    color_q = Q()
    if color_filters:
        for filter_color in color_filters:
            color_q |= Q(color__name=filter_color)
    
    if ramrom_q:
        phones = phones.filter(ramrom_q)
    
    if color_q:
        phones = phones.filter(color_q)

    if discount:
        phones = phones.filter(discount__gt=0)

    if min_price or max_price:
        phones = phones.filter(price__gte=min_price).filter(price__lte=max_price)
    
    paginator = Paginator(phones, 8)
    current_page = paginator.get_page(page)

    colors = Color.objects.all()
    
    context = {
        'title': 'Главная страница',
        'phones': current_page,
        'brands': brands,
        'current_brand': current_brand,
        'slug': slug if slug else 'all',
        'selected_filters': ramrom_filters,
        'selected_filters_color': color_filters,
        'colors': colors,
        'slug_url': slug,
        'min_price': min_price,
        'max_price': max_price,
        'phones_count': phones_count,
    }
    return render(request, 'phone/index.html', context)


def phone_detail(request, phone_slug=None):

    
    phone = Phone.objects.get(slug=phone_slug)
    images = [phone.image, phone.image1, phone.image2, phone.image3]
    
    context = {
        'title': 'Подробнее про телефон',
        'phone': phone,
        'images': images,
    }
    return render(request, 'phone/phone-detail.html', context)

