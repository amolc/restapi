from django.urls import path
from .views import ItemsViews

urlpatterns = [
    path('', ItemsViews.as_view()),
    path('<int:id>', ItemsViews.as_view())
]
