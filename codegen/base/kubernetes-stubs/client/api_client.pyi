from typing import (Any, Mapping, MutableMapping, Optional, Protocol, Sequence,
                    Type, TypeVar, Union, overload)

from kubernetes.client.configuration import Configuration

_T = TypeVar("_T")

class Response(Protocol):
    @property
    def data(self) -> Union[str, bytes]: ...

class ApiClient:
    def __init__(
        self,
        configuration: Optional[Configuration] = ...,
        header_name: Optional[str] = ...,
        header_value: Optional[str] = ...,
        cookie: Optional[str] = ...,
        pool_threads: int = ...,
    ) -> None: ...
    def sanitize_for_serialization(self, obj: Any) -> dict[Any, Any]: ...
    @overload
    def deserialize(self, response: Response, response_type: Type[_T]) -> _T: ...
    @overload
    def deserialize(self, response: Response, response_type: str) -> object: ...
    def call_api(
        self,
        resource_path: str,
        method: str,
        path_params: Optional[MutableMapping[str, object]] = ...,
        query_params: Optional[Sequence[tuple[str, object]]] = ...,
        header_params: Optional[MutableMapping[str, str]] = ...,
        body: object = ...,
        post_params: Optional[
            Union[Mapping[str, object], Sequence[tuple[str, object]]]
        ] = ...,
        files: Optional[Mapping[str, object]] = ...,
        response_types_map: Optional[Mapping[int, Optional[str]]] = ...,
        auth_settings: Optional[Sequence[str]] = ...,
        async_req: Optional[bool] = ...,
        _return_http_data_only: Optional[bool] = ...,
        collection_formats: Optional[Mapping[str, str]] = ...,
        _preload_content: bool = ...,
        _request_timeout: Optional[
            Union[int, float, tuple[Union[int, float], Union[int, float]]]
        ] = ...,
        _host: Optional[str] = ...,
        _request_auth: Optional[Mapping[str, object]] = ...,
    ) -> object: ...
