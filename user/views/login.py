from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from user import models
from user.forms.login_sms_form import LoginSmsForm
from user.forms.send_sms_form import SendSmsForm


def login(request):

    return render(request, 'user/login.html')


def send_sms(request):
    form = SendSmsForm(request, data=request.GET)
    if form.is_valid():
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})


def login_sms(request):
    if request.method == 'GET':
        form = LoginSmsForm(request)
        return render(request, 'user/login_sms.html',{'form':form})
    else:
        form = LoginSmsForm(request, data=request.POST)
        if form.is_valid():
            mobile_phone = form.cleaned_data['mobile_phone']
            user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
            if user_object:
                # 登录成功将⽤户信息保存在session中 在前端进⾏显示
                request.session['id'] = user_object.id
                request.session['username'] = user_object.username
                request.session.set_expiry(60 * 60 * 24 * 14)
                return redirect('/user/index/')
            form.add_error('mobile_phone', '手机号或验证码错误')
        return render(request, 'user/login_sms.html', {'form': form})




def index(request):
    return render(request, 'user/index.html')