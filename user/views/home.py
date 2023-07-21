from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


def home(request):
    return render(request, 'user/home.html')
