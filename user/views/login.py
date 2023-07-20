from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from user.forms.send_sms_form import SendSmsForm


def login(request):

    return render(request, 'user/login.html')


def send_sms(request):
    form = SendSmsForm(request, data=request.GET)
    if form.is_valid():
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})
