from django.urls import path
from .views import OrgViews

urlpatterns = [
    path('org/', OrgViews.as_view()),
    path('org/<int:id>', OrgViews.as_view())
]