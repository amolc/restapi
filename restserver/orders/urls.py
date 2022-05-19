from django.urls import path
from .views import OrdersViews

urlpatterns = [
    path('', OrdersViews.as_view()),
    path('<int:id>', OrdersViews.as_view())
]
