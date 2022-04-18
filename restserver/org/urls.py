from django.urls import path
from .views import OrgViews

urlpatterns = [
    path('', OrgViews.as_view()),
    path('<int:id>', OrgViews.as_view())
]