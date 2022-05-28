from django.urls import path
from .views import OrgViews, OrgLoginView

urlpatterns = [
    path('', OrgViews.as_view()),
    path('<int:id>', OrgViews.as_view()),
    path('login/', OrgLoginView.as_view()),
]
