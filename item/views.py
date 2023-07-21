from item import templates
from django.shortcuts import render, HttpResponse
from django.conf import settings

from user.models import UserInfo
from .models import *
from random import *


def show_home(request):
    list = Items.objects.all()
    ran = []
    i = 0
    finlist = []
    if len(list) != 0:
        while True:
            rn = randint(0, len(list) - 1)
            if i == 12:
                break
            if rn not in ran:
                ran.append(rn)
                i = i + 1
        for r in ran:
            finlist.append(list[int(r)])

    # 检测当前页面是不是商城，是就不显示商城标签，将url传入item网页
    current_url = request.path

    # 获取当前session的用户是谁，如果有，右上角可以显示用户名
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()

        return render(request, 'layout/home.html',
                      {'items_list': finlist, 'current_url': current_url, 'user_info': query_set})
    return render(request, 'layout/home.html',
                  {'items_list': finlist, 'current_url': current_url})


def show_details(request, gid):
    gid = int(gid)
    item_detail = Items.objects.get(id=gid)
    return render(request, 'layout/details.html', {'item_detail': item_detail})
