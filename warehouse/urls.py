from django.urls import path

from .views import WarehouseOrderAPIView

urlpatterns = [
    path('orders/', WarehouseOrderAPIView.as_view()),
]
