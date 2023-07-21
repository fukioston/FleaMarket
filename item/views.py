from item import templates
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .models import *
from random import *


def show_home(request):
    list = Items.objects.all()
    ran = []
    i = 0
    finlist = []
    if len(list)!=0:
        while True:
            rn = randint(0, len(list) - 1)
            if i == 12:
                break
            if rn not in ran:
                ran.append(rn)
                i = i + 1
        for r in ran:
            finlist.append(list[int(r)])
    return render(request, 'layout/home.html', {'items_list': finlist})


def show_details(request, gid):
    gid = int(gid)
    item_detail = Items.objects.get(id=gid)
    return render(request, 'layout/details.html', {'item_detail': item_detail})
