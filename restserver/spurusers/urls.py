from django.urls import path
from .views import SpurusersViews
from .views import SpurusersUserViews

login = SpurusersUserViews.as_view({'post':'login'})
register = SpurusersUserViews.as_view({'post':'register'})


urlpatterns = [
    path('', SpurusersViews.as_view()),
    path('<int:id>', SpurusersViews.as_view()),
    path('login', login),
    path('register', register),
    
]
