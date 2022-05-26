from django.urls import path, include
from .api import RegisterApi
from .views import LoginView


urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      path('login', LoginView.as_view()),
]
