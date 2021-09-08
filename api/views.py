from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import *
from rest_framework import generics, viewsets, mixins
from .serializers import *
from .permissions import IsAuthenticatedOrReadOnly


# Create your views here.


class HomeViewApi(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializers


class CategoryView(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionView(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerView(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ResultView(viewsets.GenericViewSet,
             mixins.ListModelMixin,
             mixins.RetrieveModelMixin):
    queryset = Attemper.objects.all()
    serializer_class = SubmitSerializer


def submit(request, pk):
    user = request.user
    score = 0
    category = get_object_or_404(Category, id=pk)
    questions = request.POST.getlist('question')
    answers = request.POST.getlist('answer')
    attempter = Attemper.objects.create(user=user, category=category, score=0)

    for q, a in zip(questions, answers):
        question = Question.objects.get(id=q)
        answer = Answer.objects.get(id=a)
        if answer.is_correct == True:
            score += question.points
            attempter.score += score
            attempter.save()

    # serializer = SubmitSerializer(data=attempter)
    #
    # if serializer.is_valid():
    #     serializer.save()
    #     return JsonResponse(serializer.data, safe=False)
    return HttpResponse('Success your exams!!!')
