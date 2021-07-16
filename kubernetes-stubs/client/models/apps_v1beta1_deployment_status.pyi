import datetime
import typing

import kubernetes.client

class AppsV1beta1DeploymentStatus:
    available_replicas: typing.Optional[int]
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes.client.AppsV1beta1DeploymentCondition]]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: typing.Optional[int]
    unavailable_replicas: typing.Optional[int]
    updated_replicas: typing.Optional[int]
    def __init__(
        self,
        *,
        available_replicas: typing.Optional[int] = ...,
        collision_count: typing.Optional[int] = ...,
        conditions: typing.Optional[
            list[kubernetes.client.AppsV1beta1DeploymentCondition]
        ] = ...,
        observed_generation: typing.Optional[int] = ...,
        ready_replicas: typing.Optional[int] = ...,
        replicas: typing.Optional[int] = ...,
        unavailable_replicas: typing.Optional[int] = ...,
        updated_replicas: typing.Optional[int] = ...
    ) -> None: ...
