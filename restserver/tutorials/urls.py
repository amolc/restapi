from django.urls import path
from .views import TutorialsViews

urlpatterns = [
    path('', TutorialsViews.as_view()),
    path('<int:id>', TutorialsViews.as_view())
]
