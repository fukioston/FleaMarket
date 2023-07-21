from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from user.models import UserInfo


def home(request):
    info = request.session.get('info')
    username = info['name']
    query_set = UserInfo.objects.filter(username=username).first()
    return render(request, 'user/home.html', {'user_info': query_set})
