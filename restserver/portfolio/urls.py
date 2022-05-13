from django.urls import path
from .views import PortfolioViews

urlpatterns = [
    path('', PortfolioViews.as_view()),
    path('<int:id>', PortfolioViews.as_view())
]
