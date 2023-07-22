from enum import Enum
from http import HTTPStatus
from typing import Any, Mapping, Optional

from requests import HTTPError, RequestException, Session


class HttpMethodEnum(str, Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'


class BaseHttpTransportError(Exception):
    def __init__(self, code: int, message: str) -> None:
        self.code: int = code
        self.message: str = message


class RequestsHttpTransport:
    def __init__(self) -> None:
        self._session: Optional[Session] = None

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[dict[str, Any]] = None,
        params: Optional[Mapping[str, str]] = None,
        data: Optional[dict[Any, Any]] = None,
    ) -> Any:

        try:
            response = self._session.request(method, url, params, data,
                                             headers)
        except RequestException:
            raise BaseHttpTransportError(HTTPStatus.SERVICE_UNAVAILABLE,
                                         'No connection to remote service')

        try:
            response.raise_for_status()
        except HTTPError:
            raise BaseHttpTransportError(response.status_code, response.text)

        if 'Content-Type' in response.headers and response.headers[
                'Content-Type'] == 'application/json':
            return response.json()

        return response.text

    def startup(self) -> None:
        self._session = Session()

    def shutdown(self) -> None:
        if not self._session:
            return

        self._session.close()
