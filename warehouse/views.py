from rest_framework.generics import CreateAPIView

from .models import WarehouseOrder
from .serializers import WarehouseOrderSerializer


class WarehouseOrderAPIView(CreateAPIView):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
