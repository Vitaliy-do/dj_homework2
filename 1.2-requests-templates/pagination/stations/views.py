from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator
from django.conf import settings




def index(request):
    return redirect(reverse('bus_stations'))

# функция пагинация формирующая вывод списка станций по странично
def bus_stations(request):
    # менеджер контекста для чтения файла формата CSV
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        stations = list(reader) # формируется список словарей, который является
        # строка csv файла, где ключами являются заголовки столбцов,
        # а значениями является информация об остановке
    page_number = int(request.GET.get('page', 1)) # запрос примет номер страницы
    paginator = Paginator(stations, page_number)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': stations,
        'page': page
    }
    return render(request, 'stations/index.html', context)
