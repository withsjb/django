
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Question

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
   
   # question = Question.objects.get(id=question_id)
   question = get_object_or_404(Question, pk=question_id)#pk는 question 모델의 기본키 primary key에 해당함
   context = {'question': question}
   return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)


# Create your views here.
