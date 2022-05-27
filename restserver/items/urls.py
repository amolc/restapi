from django.urls import path
from .views import ItemsViews,NewItemsViews

urlpatterns = [
    path('<int:org_id>/''', ItemsViews.as_view()),
    path('<int:org_id>/''<int:id>', ItemsViews.as_view())
]

