from django.urls import path
from .views import ItemsViews,ListItemsViews

urlpatterns = [
    path('', ItemsViews.as_view()),
    path('<int:id>', ItemsViews.as_view()),
    path('list/''<int:org_id>', ListItemsViews.as_view())
]
