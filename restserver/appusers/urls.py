from django.urls import path
from .views import AppusersViews

urlpatterns = [
    path('', AppusersViews.as_view()),
    path('<int:id>', AppusersViews.as_view())
]
