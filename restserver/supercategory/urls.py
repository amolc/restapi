from django.urls import path
from .views import SupercategoryViews

urlpatterns = [
    path('', SupercategoryViews.as_view()),
    path('<int:id>', SupercategoryViews.as_view())
]
