from django.urls import path
from .views import *
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register(r'home', views.HomeViewApi, basename='home')
router.register(r'category', views.CategoryView, basename='category')
router.register(r'question', views.QuestionView, basename='question')
router.register(r'answer', views.AnswerView, basename='answer')
router.register(r'result', views.ResultView, basename='result')


urlpatterns = [
    # this is test result by category
    path(r'category/<int:pk>/submit/', submit),
]

urlpatterns += router.urls
