from django.http import JsonResponse

from item import templates
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings

from user.models import *
from .form.edit_item import ItemForm
from .form.search_form import SearchForm
from .models import *
from random import *
import os

from item.form import search_form
def show_home(request):
    form = SearchForm(request)
    if request.method == 'POST':
        form = SearchForm(request, data=request.POST)
        kw = form['search_field'].value()
        goods = Items.objects.filter(gname__contains=kw)
        info = request.session.get('info')
        if goods:
            if info:
                user_id = info['id']
                query_set = UserInfo.objects.filter(id=user_id).first()
                return render(request, 'layout/search.html', {'items_list': goods, 'kw': kw,'user_info': query_set,})
            return render(request, 'layout/search.html', {'items_list': goods,'kw': kw})
        form.add_error('search_field', '搜索物品不存在')

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
                      {'items_list': finlist, 'current_url': current_url, 'user_info': query_set, 'form': form})
    return render(request, 'layout/home.html',
                  {'items_list': finlist, 'current_url': current_url, 'form': form})
def show_details(request, gid):
    gid = int(gid)
    item_detail = Items.objects.get(id=gid)
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        return render(request, 'layout/details.html', {'item_detail': item_detail, 'user_info': query_set})
    return render(request, 'layout/details.html', {'item_detail': item_detail, })
def show_submit(request):
    info = request.session.get('info')
    if request.method == 'GET':
        if info:
            user_id = info['id']
            query_set = UserInfo.objects.filter(id=user_id).first()
            return render(request, 'layout/submit.html', {'user_info': query_set, })
        return render(request, 'layout/submit.html', )
    if request.POST.get('sub'):
        print("suc")
        newgname = request.POST.get("newgname")
        newprice = request.POST.get("newprice")
        newintro = request.POST.get("newintro")
        newphone = request.POST.get("newphone")
        newuserid = info['id']
        file = request.FILES.get('file')
        newimg = file.name
        print(file.name)
        Items.objects.create(gname=newgname, userid=newuserid, price=newprice, intro_txt=newintro, img_index=newimg,phone=newphone)
        with open(os.path.join('static/images', file.name), 'wb') as f:  # 在static目录下创建同名文件
            for line in file.chunks():
                f.write(line)  # 逐行读取上传的文件内容并写入新创建的同名文件
        return HttpResponse("<p>提交成功！</p>")
def show_favorite(request):
    info = request.session.get('info')
    if info:
        user_id = info['id']
        query_set = UserInfo.objects.filter(id=user_id).first()
        favorite_item_list = UserFavorite.objects.filter(userid=user_id)
        favorite_list = []

        for item in favorite_item_list:
            item_id = item.itemid
            favorite_item = Items.objects.filter(id=item_id)
            favorite_list.extend(favorite_item)
        return render(request, 'layout/favorite.html', {'user_info': query_set, 'favorite_list': favorite_list})
    return render(request, 'layout/favorite.html')
def change_favorite(request):
    item_id = request.GET.get('item_id')
    user_id = request.GET.get('user_id')

    # 如果表中有了数据就报错
    try:
        if UserFavorite.objects.get(userid=user_id, itemid=item_id):
            return JsonResponse({'status': False, 'err': "已经收藏"})
    except UserFavorite.DoesNotExist:
        UserFavorite.objects.create(userid=user_id, itemid=item_id)
        # 如果表中没有数据
        return JsonResponse({'status': True})
def cancel_favorite(request):
    item_id = request.GET.get('item_id')
    user_id = request.GET.get('user_id')
    if UserFavorite.objects.get(userid=user_id, itemid=item_id):
        UserFavorite.objects.get(userid=user_id, itemid=item_id).delete()
        return JsonResponse({'status': True, 'err': "已经取消收藏"})
def isfavorite(request):
    item_id = request.GET.get('item_id')
    user_id = request.GET.get('user_id')

    # 如果表中有了数据就报错
    try:
        if UserFavorite.objects.get(userid=user_id, itemid=item_id):
            return JsonResponse({'status': True, 'err': "已经收藏"})
    except UserFavorite.DoesNotExist:
        # 如果表中没有数据
        print('cao')
        return JsonResponse({'status': False})
def edit_details(request, gid):
    gid = int(gid)
    item_detail = Items.objects.get(id=gid)
    info = request.session.get('info')
    if request.method == 'GET':
        if info:
            user_id = info['id']
            query_set = UserInfo.objects.filter(id=user_id).first()
            item_info = Items.objects.filter(id=gid).values_list('gname', 'price', 'intro_txt', 'img_index','phone').first()
            item_info2 = {'gname': item_info[0], 'price': item_info[1], 'intro_txt': item_info[2],
                          'img_index': item_info[3],'phone':item_info[4]}
            form = ItemForm(request, initial=item_info2)
            return render(request, 'layout/edit_details.html', {'user_info': query_set, 'form': form,'img_index':item_info[3]})

    form = ItemForm(request, data=request.POST)
    item = Items.objects.filter(id=gid).first()
    if form.is_valid():
        new_price = form.cleaned_data['price']
        new_gname = form.cleaned_data['gname']
        new_intro_txt = form.cleaned_data['intro_txt']
        new_phone=form.cleaned_data['phone']
        file = request.FILES.get('file')
        if file:
            newimg = file.name
            item.img_index = newimg
            with open(os.path.join('static/images', file.name), 'wb') as f:  # 在static目录下创建同名文件
                for line in file.chunks():
                    f.write(line)
        item.gname = new_gname
        item.intro_txt = new_intro_txt
        item.price = new_price
        item.phone=new_phone
        item.save()

        print('info_saved!')
        return redirect('/user/on_sales')
def gdelete(request, gid):
    gid = int(gid)
    Items.objects.filter(id=gid).delete()
    return redirect("http://127.0.0.1:8000/user/on_sales/")