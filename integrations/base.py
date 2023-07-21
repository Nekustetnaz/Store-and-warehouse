import json
from dataclasses import dataclass
from enum import Enum
from typing import Any

from furl import furl

from transport.http import (BaseHttpTransportError, HttpMethodEnum,
                            RequestsHttpTransport)


class OrderStatusEnum(str, Enum):
    NEW = 'New'
    IN_PROCESS = 'In Process'
    STORED = 'Stored'
    SEND = 'Send'


@dataclass
class OrderSchema:
    order_number: str
    status: OrderStatusEnum


class BaseIntegrationError(Exception):
    pass


class BaseHttpClient:
    def __init__(self, transport: RequestsHttpTransport, base_url: str):
        self._transport = transport
        self._base_url = base_url
        self._default_headers: dict[str, Any] = {
            'Content-type': 'application/json'}

    def place_order(self, data: OrderSchema) -> None:
        url = furl(self._base_url).add(path='orders/')
        data = json.dumps(data.__dict__)
        self._request(HttpMethodEnum.POST, url.url, self._default_headers,
                      data=data)

    def update_order(self, data: OrderSchema) -> None:
        url = furl(self._base_url).add(path='orders/'+data.order_number)
        data = json.dumps(data.__dict__)
        self._request(HttpMethodEnum.PATCH, url.url, self._default_headers,
                      data=data)

    def _request(self, *args, **kwargs) -> Any:
        try:
            return self._transport.request(*args, **kwargs)
        except BaseHttpTransportError as err:
            raise BaseIntegrationError(f'{err.code} - {err.message}')
