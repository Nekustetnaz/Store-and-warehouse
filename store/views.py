from rest_framework.generics import UpdateAPIView

from .models import StoreOrder
from .serializers import StoreOrderSerializer


class StoreOrderAPIView(UpdateAPIView):
    queryset = StoreOrder.objects.all()
    serializer_class = StoreOrderSerializer
    lookup_field = 'order_number'
