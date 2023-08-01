from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Главная страница сайта SOFT")


def categories(request):
    return HttpResponse("<h1>Программное обеспечение по категориям</h1>")

# Create your views here.
