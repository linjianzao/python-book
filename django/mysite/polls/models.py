# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
#所有字段类型说明: https://docs.djangoproject.com/en/1.11/ref/models/fields/

#创建migrations
#1.写相关model
#2.把你所在的app注册到INSTALLED_APPS(所在app第一次创建migration)
#3.执行 python manage.py makemigrations polls  注意最后的polls就是你的app的名字
#4.在app/migrations就自动生成文件了。
#注意INSTALLED_APPS可以使用url namespace里定义的值。

#执行migration
#让migration文件生成sql语句: python manage.py sqlmigrate polls 0001
#执行migration: python manage.py migrate

#
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200,verbose_name='或者使用verbose_name写注释')
    pub_date = models.DateTimeField('第一个参数写注释更改')

    #Question.objects.all()使用这个方法的时候，会有明确的记录提示。
    def __str__(self):
        return self.question_text
    
    #一些值或类型的判断可以这边做
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):
    #models.CASCADE 主键表删除记录时，外键表也删除相关记录，一般都是假删除，不会用。
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text