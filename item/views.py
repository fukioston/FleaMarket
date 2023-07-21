from item import templates
from django.shortcuts import render, HttpResponse
from django.conf import settings


def show_home(request):
    return render(request, 'layout/home.html')
