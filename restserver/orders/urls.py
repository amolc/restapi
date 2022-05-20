from django.urls import path
from .views import OrdersViews,StripeChargeViews,OrderDetailsViews

urlpatterns = [
    path('orderdetail', OrderDetailsViews.as_view()),
    path('', OrdersViews.as_view()),
    path('<int:id>', OrdersViews.as_view()),
    path('charge', StripeChargeViews.as_view())
   
    
]
