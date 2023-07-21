from rest_framework.serializers import ModelSerializer

from .models import WarehouseOrder


class WarehouseOrderSerializer(ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = ('order_number', 'status')
