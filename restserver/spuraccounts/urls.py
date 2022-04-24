from django.urls import path
from .views import SpurusersViews

urlpatterns = [
    path('', SpurusersViews.as_view()),
    path('<int:id>', SpurusersViews.as_view())
]
