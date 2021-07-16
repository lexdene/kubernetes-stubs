import datetime
import typing

import kubernetes.client

class AppsV1beta1Deployment:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.AppsV1beta1DeploymentSpec]
    status: typing.Optional[kubernetes.client.AppsV1beta1DeploymentStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.AppsV1beta1DeploymentSpec] = ...,
        status: typing.Optional[kubernetes.client.AppsV1beta1DeploymentStatus] = ...
    ) -> None: ...
