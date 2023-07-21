from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from user.models import UserInfo
from item.models import Items


def home(request):
    info = request.session.get('info')
    username = info['name']
    query_set = UserInfo.objects.filter(username=username).first()
    user_id = query_set.id
    on_sales_num = Items.objects.filter(userid=user_id).count()

    return render(request, 'user/home.html', {'user_info': query_set, 'on_sales_num': on_sales_num})


def on_sales(request):
    info = request.session.get('info')
    username = info['name']
    query_set = UserInfo.objects.filter(username=username).first()
    user_id = query_set.id
    on_sales = Items.objects.filter(userid=user_id)

    return render(request, 'user/on_sales.html', {'on_sales': on_sales, 'user_info': query_set})


def logout(request):
    request.session.flush()
    return redirect('/user/login/sms/')