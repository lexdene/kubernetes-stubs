import datetime
import typing

import kubernetes.client

class V1beta1PodDisruptionBudget:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta1PodDisruptionBudgetSpec]
    status: typing.Optional[kubernetes.client.V1beta1PodDisruptionBudgetStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta1PodDisruptionBudgetSpec] = ...,
        status: typing.Optional[
            kubernetes.client.V1beta1PodDisruptionBudgetStatus
        ] = ...
    ) -> None: ...
