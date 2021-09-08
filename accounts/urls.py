from django.urls import path
from .views import RegistrationApi

urlpatterns = [
    path('register/', RegistrationApi.as_view()),
]
