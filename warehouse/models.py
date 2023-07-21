from django.db import models


class WarehouseOrder(models.Model):
    """Orders in a warehouse model"""

    class OrderStatus(models.TextChoices):
        NEW = 'New'
        IN_PROCESS = 'In Process'
        STORED = 'Stored'
        SEND = 'Send'

    order_number = models.CharField('Order number', max_length=16)
    status = models.CharField('Status',
                              max_length=16,
                              choices=OrderStatus.choices,
                              default=OrderStatus.NEW)

    class Meta:
        verbose_name = 'Warehouse order'
        verbose_name_plural = 'Warehouse orders'
        ordering = ('status',)

    def __str__(self):
        return f'Order: {self.order_number} - {self.status}'
