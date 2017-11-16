# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

#url函数详细参数说明:https://docs.djangoproject.com/en/1.11/ref/urls/#django.conf.urls.url
#参数name，用来定义变量名，变量值就是本url
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<question_id>[0-9]+)/$', views.detail, name='detail')
]