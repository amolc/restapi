from django.urls import path
from .views import CustomersViews

urlpatterns = [
    path('', CustomersViews.as_view()),
    path('<int:id>', CustomersViews.as_view())
]
