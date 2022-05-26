from django.urls import path
from .views import StudentViews

urlpatterns = [
    path('', StudentViews.as_view()),
    path('<int:id>', StudentViews.as_view())
]
