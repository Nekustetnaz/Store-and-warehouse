from logging import getLogger

from django.contrib import admin

from integrations.base import BaseIntegrationError
from services.orders import OrderSchema, get_order_update_service

from .models import WarehouseOrder

logger = getLogger(__name__)


class WarehouseAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.save()
        service = get_order_update_service()

        try:
            service.update_order(
                OrderSchema(
                    order_number=obj.order_number,
                    status=obj.status
                )
            )
        except BaseIntegrationError as err:
            logger.error('Order %s update failed! Error: %s',
                         obj.order_number, str(err))


admin.site.register(WarehouseOrder, WarehouseAdmin)
