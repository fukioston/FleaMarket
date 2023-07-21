from item import templates
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .models import *
from random import *


def show_home(request):
    items_list = Items.objects.all()

    return render(request, 'layout/home.html', {'items_list': items_list})


def show_details(request, gid):
    gid = int(gid)
    item_detail = Items.objects.get(id=gid)
    return render(request, 'layout/details.html', {'item_detail': item_detail})
