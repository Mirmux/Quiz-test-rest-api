from django.contrib.auth import get_user_model
from django.urls import reverse

from django.db import models

from rest_1 import settings

User = get_user_model()

# Create your models here.


class Home(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    @property
    def get_quest(self):
        quest = self.question_set.all()
        item = [que.get_question for que in quest]
        return item



class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    question_text = models.TextField()
    points = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.category.id

    def __str__(self):
        return f"{self.question_text} id={self.id}"

    @property
    def get_question(self):
        question = self.question_text
        return question


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer_text = models.CharField(max_length=400)
    is_correct = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id

    def __str__(self):
        return f"{self.answer_text}"

    @property
    def question_text(self):
        return self.question.question_text


class Attemper(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    def __int__(self):
        return self.id
