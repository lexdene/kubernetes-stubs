import datetime
import typing

import kubernetes.client

class V1SubjectAccessReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1SubjectAccessReviewSpec
    status: typing.Optional[kubernetes.client.V1SubjectAccessReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1SubjectAccessReviewSpec,
        status: typing.Optional[kubernetes.client.V1SubjectAccessReviewStatus] = ...
    ) -> None: ...
