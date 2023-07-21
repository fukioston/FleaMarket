from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from user.forms.edit_info import InfoForm
from user.forms.edit_pwd import PwdForm
from user.models import UserInfo
from item.models import Items


def home(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    on_sales_num = Items.objects.filter(userid=user_id).count()

    return render(request, 'user/home.html', {'user_info': query_set, 'on_sales_num': on_sales_num})


def on_sales(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    on_sales = Items.objects.filter(userid=user_id)

    return render(request, 'user/on_sales.html', {'user_info': query_set, 'on_sales': on_sales})


def logout(request):
    request.session.flush()
    return redirect('/user/login/sms/')

def edit_info(request):
    info = request.session.get('info')
    user_id = info['id']
    query_set = UserInfo.objects.filter(id=user_id).first()
    if request.method == 'GET':
        user_info = UserInfo.objects.filter(id=user_id).values_list('username', 'email', 'mobile_phone').first()
        init_info = {'username': user_info[0], 'mobile_phone': user_info[2], 'email': user_info[1]}
        form = InfoForm(request, initial=init_info)
        return render(request, 'user/edit_info.html', {'user_info': query_set, 'form': form})

    form = InfoForm(request, data=request.POST)
    user = UserInfo.objects.filter(id=user_id).first()
    if form.is_valid():
        new_name = form.cleaned_data['username']
        new_phone = form.cleaned_data['mobile_phone']
        new_email = form.cleaned_data['email']
        user.username = new_name
        user.mobile_phone = new_phone
        user.email = new_email
        user.save()
        print('info_saved!')
        return redirect('/user/home/')


def edit_pwd(request):
    info = request.session.get('info')
    user_id = info['id']
    if request.method == 'GET':
        form = PwdForm(request)
        return render(request, 'user/edit_pwd.html', {'form': form})

    form = PwdForm(request, data=request.POST)
    user = UserInfo.objects.filter(id=user_id).first()
    if form.is_valid():
        old_pwd = form.cleaned_data['old_pwd']
        new_pwd = form.cleaned_data['new_pwd']
        if old_pwd==user.password:
            user.password=new_pwd
            return redirect('/user/home/')
        else:
            form.add_error('old_pwd', '旧密码错误')
            return render(request, 'user/edit_pwd.html', {'form': form})