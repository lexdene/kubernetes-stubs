import datetime
import typing

import kubernetes.client

class AppsV1beta1DeploymentList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.AppsV1beta1Deployment]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.AppsV1beta1Deployment],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...
    ) -> None: ...
