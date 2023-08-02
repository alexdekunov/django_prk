from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Главная страница сайта SOFT")


def categories(request):
    return HttpResponse("<h1>Программное обеспечение по категориям</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# Create your views here.
