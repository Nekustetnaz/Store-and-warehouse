from django.urls import path

from .views import StoreOrderAPIView

urlpatterns = [
    path('orders/<str:order_number>', StoreOrderAPIView.as_view()),
]
