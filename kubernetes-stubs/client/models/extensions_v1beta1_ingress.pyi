import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1Ingress:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.ExtensionsV1beta1IngressSpec]
    status: typing.Optional[kubernetes.client.ExtensionsV1beta1IngressStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.ExtensionsV1beta1IngressSpec] = ...,
        status: typing.Optional[kubernetes.client.ExtensionsV1beta1IngressStatus] = ...
    ) -> None: ...
