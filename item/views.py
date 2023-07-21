from item import templates
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .models import *


def show_home(request):
    items_list = Items.objects.all()

    return render(request, 'layout/home.html', {'items_list': items_list})
