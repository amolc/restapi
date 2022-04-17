from django.urls import path
from .views import CategoryViews

urlpatterns = [
    path('category/', CategoryViews.as_view()),
    path('category/<int:id>', CategoryViews.as_view())
]
