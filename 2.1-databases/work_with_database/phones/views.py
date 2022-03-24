from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort_by = ['name', 'min_price', 'max_price']
    sort_var = request.GET.get('sort')
    if sort_var not in sort_by:
        phones = Phone.objects.all()
    else:
        if sort_var == 'name':
            sort_by = request.GET.get('sort', 'name')
        elif sort_var == 'min_price':
            sort_by = 'price'
        elif sort_var == 'max_price':
            sort_by = '-price'
        phones = Phone.objects.order_by(sort_by)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
