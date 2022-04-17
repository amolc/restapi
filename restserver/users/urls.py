from django.urls import path
from .views import UsersViews

urlpatterns = [
    path('users/', UsersViews.as_view()),
    path('users/<int:id>', UsersViews.as_view())
]
