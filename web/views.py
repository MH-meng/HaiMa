from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from web import models

# 分页
from web.pager import Pagination, PaginationNew

from web.tests import change_info
def home(request):
    change_info(request)
    return render(request, 'home.html')

def profiles(request):
    return render(request,'profiles.html')


def culture(request):
    return render(request,'culture.html')


def cooperations(request):
    return render(request, 'cooperations.html')

def relation(request):
    return render(request, 'relation.html')


def price(request):
    t = models.Price.objects.all().count()
    current_page = request.GET.get('p')
    page_obj = Pagination(t, current_page)
    USER_LIST = models.Price.objects.all().values().order_by('-time')
    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request, 'price.html', {'data_list': data_list, 'page_obj': page_obj})

def serverflow(request):
    return render(request,'serverflow.html')

def carriage(request):
    return render(request,'carriage.html')

def maritime(request):
    return render(request,'maritime.html')

def timereach(request):
    return render(request,'timereach.html')

def warehouse(request):
    return render(request,'warehouse.html')

def packaging(request):
    return render(request,'packaging.html')

def distribution(request):
    return render(request,'distribution.html')

def information(request):
    return render(request,'information.html')

def news(request):
    n = models.News.objects.all().count()
    current_page = request.GET.get('p')
    page_new = PaginationNew(n, current_page)
    NEWS_LIST =models.News.objects.all().values().order_by('-time')
    dataNews_list = NEWS_LIST[page_new.start():page_new.end()]
    return render(request, 'news.html', {'dataNews_list': dataNews_list, 'page_new': page_new})

def i404(request):
    return render(request,'404.html')

def i500(request):
    return render(request,'500.html')

def login(request):
    if request.method == "POST":

        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("account")
        pwd = request.POST.get("password")
        if username == 'Admin' and pwd == 'admin123':
            # 用户名密码正确
            # 给用户做登录
            request.session['is_login1'] = True
            request.session.set_expiry(60*60*24*7)
            ret["status"] = 1
            ret["msg"] = "/h_index/"
        else:
            # 用户名密码错误
            ret["status"] = 0
            ret["msg"] = "用户名或密码错误,请重新输入！"

        return JsonResponse(ret)
    return render(request, 'admin_haima/login.html')

def h_index(request):
    # print(request.user.is_authenticated())
    if request.session.get('is_login1', None):
        return render(request, 'admin_haima/index.html')
    else:
        return redirect('/login/')

def welcome(request):
    return render(request, 'admin_haima/welcome.html')

def news_list(request):
    news_list = models.News.objects.filter().values().order_by('-time')
    count = models.News.objects.all().count()
    return render(request, 'admin_haima/article-list.html',{'news_list':news_list, 'count':count})

def news_start(request):
    if request.method == "POST":
        id = request.POST.get("id")
        # print(id)
        models.News.objects.filter(id=id).update(status=1)
        ret = {}
        ret["id"] = id
        return JsonResponse(ret)

def news_stop(request):
    if request.method == "POST":
        id = request.POST.get("pk")
        models.News.objects.filter(id=id).update(status='2')
        ret = {}
        ret["id"] = id
        return JsonResponse(ret)

def news_del(request):
    if request.method == "POST":
        id = request.POST.get("pk")
        models.News.objects.filter(id=id).delete()
        ret = {}
        ret["status"] = 1
        return JsonResponse(ret)

import json

def news_add(request):
    if request.method == "GET":
        return render(request, 'admin_haima/article-add.html')

def news_add_comfirm(request):
    if request.method == "POST":
        show_inf = {'status': True, 'inf': None}
        title = request.POST.get("title")
        introduction = request.POST.get("introduction")
        author = request.POST.get("author")
        time = request.POST.get("time")
        content = request.POST.get("content")
        if title and introduction and author and time and content:
            models.News.objects.create(
                title =title,
                introduction=introduction,
                author=author,
                time=time,
                content=content
            )
            show_inf['status'] = True
            show_inf['inf'] = '发布新闻信息成功'
            show_inf['link'] = '/news_list/'
        else:
            show_inf['status'] = False
            show_inf['inf'] = '请把信息填写完整，谢谢！'
            # print(show_inf)
        res = json.dumps(show_inf)
        return HttpResponse(res)

def create_uuid():
    import uuid
    s_uuid = str(uuid.uuid1())
    l_uuid = s_uuid.split('-')
    uid = ''.join(l_uuid)
    return uid

import os
from HaiMa import settings

def upload(request):
    obj = request.FILES.get("upload_img")
    avatar_uid = create_uuid()
    avatar_img_name = avatar_uid + "." + obj.name.split(".")[1]
    flag = ".doc" in obj.name
    if flag:
        path = os.path.join(settings.MEDIA_ROOT, 'add_news_file', avatar_img_name)
    else:
        path = os.path.join(settings.MEDIA_ROOT, 'add_news_img', avatar_img_name)

    # print('path', path)
    with open(path, "wb") as f:
        for line in obj:
            f.write(line)

    res = {
        "error": 0,
        "url": "/" + path.split("\\")[4] + "/" + path.split("\\")[5] + "/" + avatar_img_name
    }
    # print("res['url']", res['url'])
    return HttpResponse(json.dumps(res))

def news_detail(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        # print(id)
        news_detail = models.News.objects.filter(id=id).values()
        # print(news_detail)
        return render(request, 'news_detail.html', locals())

def news_edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        news_edit = models.News.objects.filter(id=id).values()
        # print(news_edit)
        return render(request, 'admin_haima/news_edit.html', {'news_edit':news_edit})

def news_edit_comfirm(request):
    if request.method == "POST":
        show_inf = {'status': True, 'inf': None}
        id = request.POST.get("id")
        title = request.POST.get("title")
        introduction = request.POST.get("introduction")
        author = request.POST.get("author")
        time = request.POST.get("time")
        content = request.POST.get("content")
        # print(id)
        if title and introduction and author and time and content:
            models.News.objects.filter(id=id).update(
                title=title,
                introduction=introduction,
                author=author,
                time=time,
                content=content
            )
            show_inf['status'] = True
            show_inf['inf'] = '发布新闻信息成功'
            show_inf['link'] = '/news_list/'
        else:
            show_inf['status'] = False
            show_inf['inf'] = '请把信息填写完整，谢谢！'
            # print(show_inf)
        res = json.dumps(show_inf)
        return HttpResponse(res)

def price_list(request):
    price_list = models.Price.objects.filter().values().order_by('-time')
    count = models.Price.objects.all().count()
    return render(request, 'admin_haima/price_list.html', {'price_list': price_list, 'count': count})

def price_stop(request):
    if request.method == "POST":
        id = request.POST.get("pk")
        models.Price.objects.filter(id=id).update(status=0)
        ret = {}
        ret["id"] = id
        return JsonResponse(ret)

def price_start(request):
    if request.method == "POST":
        id = request.POST.get("id")
        # print(id)
        models.Price.objects.filter(id=id).update(status=1)
        ret = {}
        ret["id"] = id
        return JsonResponse(ret)

def price_del(request):
    if request.method == "POST":
        id = request.POST.get("pk")
        models.Price.objects.filter(id=id).delete()
        ret = {}
        ret["status"] = 1
        return JsonResponse(ret)

def price_add(request):
    return render(request, 'admin_haima/price_add.html')

def price_add_comfirm(request):
    if request.method == "POST":
        show_inf = {'status': True, 'inf': None}
        departure = request.POST.get("departure")
        destination = request.POST.get("destination")
        type = request.POST.get("type")
        price = request.POST.get("price")
        author = request.POST.get("author")
        time = request.POST.get("time")
        content = request.POST.get("content")
        if departure and destination and author and time and content and type and price:
            models.Price.objects.create(
                departure=departure,
                destination=destination,
                author=author,
                type=type,
                price=price,
                time=time,
                content=content
            )
            show_inf['status'] = True
            show_inf['inf'] = '发布价格信息成功'
            show_inf['link'] = '/price_list/'
        else:
            show_inf['status'] = False
            show_inf['inf'] = '请把信息填写完整，谢谢！'
            # print(show_inf)
        res = json.dumps(show_inf)
        return HttpResponse(res)

def price_edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        price_edit = models.Price.objects.filter(id=id).values()
        return render(request, 'admin_haima/price_edit.html', {'price_edit':price_edit})

def price_edit_comfirm(request):
    if request.method == "POST":
        show_inf = {'status': True, 'inf': None}
        id = request.POST.get("id")
        departure = request.POST.get("departure")
        destination = request.POST.get("destination")
        type = request.POST.get("type")
        price = request.POST.get("price")
        author = request.POST.get("author")
        time = request.POST.get("time")
        content = request.POST.get("content")
        if departure and destination and author and time and content and type and price:
            models.Price.objects.filter(id=id).update(
                departure=departure,
                destination=destination,
                author=author,
                type=type,
                price=price,
                time=time,
                content=content
            )
            show_inf['status'] = True
            show_inf['inf'] = '修改价格信息成功'
            show_inf['link'] = '/price_list/'
        else:
            show_inf['status'] = False
            show_inf['inf'] = '请把信息填写完整，谢谢！'
            # print(show_inf)
        res = json.dumps(show_inf)
        return HttpResponse(res)