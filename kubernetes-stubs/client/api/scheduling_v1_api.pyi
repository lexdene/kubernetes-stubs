import typing

import kubernetes.client

class SchedulingV1Api:
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList:
        ...
    def list_priority_class(self, *, pretty: typing.Optional[str] = ..., allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.V1PriorityClassList:
        ...
    def create_priority_class(self, body: kubernetes.client.V1PriorityClass, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1PriorityClass:
        ...
    def delete_collection_priority_class(self, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., continue: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ...) -> kubernetes.client.V1Status:
        ...
    def read_priority_class(self, name: str, *, pretty: typing.Optional[str] = ..., exact: typing.Optional[bool] = ..., export: typing.Optional[bool] = ...) -> kubernetes.client.V1PriorityClass:
        ...
    def replace_priority_class(self, name: str, body: kubernetes.client.V1PriorityClass, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1PriorityClass:
        ...
    def delete_priority_class(self, name: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., dryRun: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ...) -> kubernetes.client.V1Status:
        ...
    def patch_priority_class(self, name: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.V1PriorityClass:
        ...
