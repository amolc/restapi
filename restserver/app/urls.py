from django.urls import path
from .views import HelloViews
  
urlpatterns = [
    path('hello', HelloViews.as_view()),
]
