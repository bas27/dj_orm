import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    current_page = request.GET.get('page', 1)
    data = [i for i in get_data()]
    paginator = Paginator(data, 10)
    data_page = paginator.get_page(current_page)

    context = {
        'bus_stations': data_page,
        'current_page': current_page,
        'page': data_page,
    }

    return render(request, 'stations/index.html', context)


def get_data():
    data_bus_st = []
    with open(settings.BUS_STATION_CSV, encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            tmp_dict = {
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            }
            data_bus_st.append(tmp_dict)
    return data_bus_st
