"""HaiMa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from web import  views
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home),

    url(r'^profiles.html/$',views.profiles),
    url(r'^culture.html/$',views.culture),

    url(r'^cooperations.html/$',views.cooperations),
    url(r'^relation.html/$',views.relation),


    url(r'^price.html/$',views.price),
    url(r'^serverflow.html/$',views.serverflow),
    url(r'^carriage.html/$',views.carriage),
    url(r'^maritime.html/$',views.maritime),
    url(r'^timereach.html/$',views.timereach),
    url(r'^warehouse.html/$',views.warehouse),
    url(r'^packaging.html/$',views.packaging),
    url(r'^distribution.html/$',views.distribution),

    url(r'^news.html/$',views.news),
    url(r'^information.html/$',views.information),

    # media 相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),

    url(r'^404.html/$',views.i404),
    url(r'^500.html/$',views.i500),

    url(r'^login/$', views.login),
    url(r'^h_index/$', views.h_index),
    url(r'^welcome/$', views.welcome),
    url(r'^news_list/$', views.news_list),
    url(r'^news_start/$', views.news_start),
    url(r'^news_stop/$', views.news_stop),
    url(r'^news_del/$', views.news_del),
    url(r'^news_add/$', views.news_add),
    url(r'^news_add_comfirm/$', views.news_add_comfirm),
    url(r'^upload/$', views.upload),
    url(r'^news_detail/$', views.news_detail),
    url(r'^news_edit/$', views.news_edit),
    url(r'^news_edit_comfirm/$', views.news_edit_comfirm),

    url(r'^price_list/$', views.price_list),
    url(r'^price_stop/$', views.price_stop),
    url(r'^price_start/$', views.price_start),
    url(r'^price_del/$', views.price_del),
    url(r'^price_add/$', views.price_add),
    url(r'^price_add_comfirm/$', views.price_add_comfirm),
    url(r'^price_edit/$', views.price_edit),
    url(r'^price_edit_comfirm/$', views.price_edit_comfirm),


]