# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from .models import Question
# Create your views here.
from django.http import HttpResponse,Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    return render_to_response("index.html",{"latest_question_list":latest_question_list})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('question does not exist')
    return render_to_response("detail.html",{question:question})
        

def results(request, question_id):
    return HttpResponse("results %s." % question_id)

def vote(request, question_id):
    return HttpResponse("vote %s." % question_id)