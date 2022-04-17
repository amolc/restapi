from django.urls import path
from .views import SupercategoryViews

urlpatterns = [
    path('supercategory/', SupercategoryViews.as_view()),
    path('supercategory/<int:id>', SupercategoryViews.as_view())
]
