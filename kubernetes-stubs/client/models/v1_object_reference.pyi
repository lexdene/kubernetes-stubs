import datetime
import typing

import kubernetes.client

class V1ObjectReference:
    api_version: typing.Optional[str]
    field_path: typing.Optional[str]
    kind: typing.Optional[str]
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    resource_version: typing.Optional[str]
    uid: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        field_path: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        uid: typing.Optional[str] = ...
    ) -> None: ...
