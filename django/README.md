本目录django 有关的所有东西
<a href="https://docs.djangoproject.com">https://docs.djangoproject.com</a>

<h1>命名行</h1>
大部分命令: https://docs.djangoproject.com/en/1.11/ref/django-admin/
创建名叫"mysite"的项目: django-admin startproject mysite
创建django app: python manage.py startapp polls
查看版本: python -m django --version
数据库migrate: python manage.py migrate
运行开发服务器: python manage.py runserver 0:8080

使用shell来管理数据库对象: python manage.py shell
    >>> from polls.models import Question, Choice
    >>> Question.objects.all()
    >>> Question.objects.filter(id=1)
    >>> Question.objects.filter(question_text__startswith='What')
    >>> q = Question.objects.get(pk=1)
    >>> q.choice_set.create(choice_text='Not much', votes=0)
    >>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
    >>> c.question
    >>> q.choice_set.all()
    >>> q.choice_set.count()
    >>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
    >>> c.delete()
详细的说明： https://docs.djangoproject.com/en/1.11/ref/models/relations/

<h1>新项目设置需知</h1>
<h5>settings</h5>
TIME_ZONE = 'Asia/Shanghai'
ALLOWED_HOSTS = ['*']
<h5>其他</h5>
支持中文: 每个文件开头加一行  # -*- coding: utf-8 -*-

<h1>settings</h1>
django所有settings: https://docs.djangoproject.com/en/1.11/topics/settings/

<h1>url配置</h1>
详细说明: https://docs.djangoproject.com/en/1.11/ref/urlresolvers/#module-django.urls

<h1>model操作</h1>
model大纲: https://docs.djangoproject.com/en/1.11/ref/models/
构造查询: https://docs.djangoproject.com/en/1.11/topics/db/models/

<h1>后台管理</h1>
python manage.py createsuperuser
