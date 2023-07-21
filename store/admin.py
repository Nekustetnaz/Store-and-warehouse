from logging import getLogger

from django.contrib import admin

from integrations.base import BaseIntegrationError
from services.orders import OrderSchema, get_order_placement_service

from .models import StoreOrder

logger = getLogger(__name__)


class StoreAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.save()
        service = get_order_placement_service()

        try:
            service.create_order(
                OrderSchema(
                    order_number=obj.order_number,
                    status=obj.status
                )
            )
        except BaseIntegrationError as err:
            logger.error('Order %s placement failed! Error: %s',
                         obj.order_number, str(err))


admin.site.register(StoreOrder, StoreAdmin)
