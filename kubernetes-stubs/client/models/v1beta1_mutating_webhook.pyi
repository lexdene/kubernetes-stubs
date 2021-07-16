import datetime
import typing

import kubernetes.client

class V1beta1MutatingWebhook:
    admission_review_versions: typing.Optional[list[str]]
    client_config: kubernetes.client.AdmissionregistrationV1beta1WebhookClientConfig
    failure_policy: typing.Optional[str]
    match_policy: typing.Optional[str]
    name: str
    namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    reinvocation_policy: typing.Optional[str]
    rules: typing.Optional[list[kubernetes.client.V1beta1RuleWithOperations]]
    side_effects: typing.Optional[str]
    timeout_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        admission_review_versions: typing.Optional[list[str]] = ...,
        client_config: kubernetes.client.AdmissionregistrationV1beta1WebhookClientConfig,
        failure_policy: typing.Optional[str] = ...,
        match_policy: typing.Optional[str] = ...,
        name: str,
        namespace_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        object_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        reinvocation_policy: typing.Optional[str] = ...,
        rules: typing.Optional[list[kubernetes.client.V1beta1RuleWithOperations]] = ...,
        side_effects: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...
    ) -> None: ...
