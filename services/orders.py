from django.conf import settings

from integrations.base import BaseHttpClient, OrderSchema
from transport.http import RequestsHttpTransport


class OrderService:
    def __init__(self, client: BaseHttpClient) -> None:
        self._client = client

    def create_order(self, data: OrderSchema) -> None:
        self._client.place_order(data)

    def update_order(self, data: OrderSchema) -> None:
        self._client.update_order(data)


def get_order_placement_service() -> OrderService:
    transport = RequestsHttpTransport()
    transport.startup()
    client = BaseHttpClient(transport, settings.WAREHOUSE_BASE_URL)
    return OrderService(client)


def get_order_update_service() -> OrderService:
    transport = RequestsHttpTransport()
    transport.startup()
    client = BaseHttpClient(transport, settings.STORE_BASE_URL)
    return OrderService(client)
