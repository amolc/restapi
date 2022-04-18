from django.urls import path
from .views import CategoryViews

urlpatterns = [
    path('', CategoryViews.as_view()),
    path('<int:id>', CategoryViews.as_view())
]
