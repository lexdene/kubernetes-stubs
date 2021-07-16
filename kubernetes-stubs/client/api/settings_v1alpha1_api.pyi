import typing

import kubernetes.client

class SettingsV1alpha1Api:
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList:
        ...
    def list_namespaced_pod_preset(self, namespace: str, *, pretty: typing.Optional[str] = ..., allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.V1alpha1PodPresetList:
        ...
    def create_namespaced_pod_preset(self, namespace: str, body: kubernetes.client.V1alpha1PodPreset, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1alpha1PodPreset:
        ...
    def delete_collection_namespaced_pod_preset(self, namespace: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., continue: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ...) -> kubernetes.client.V1Status:
        ...
    def read_namespaced_pod_preset(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ..., exact: typing.Optional[bool] = ..., export: typing.Optional[bool] = ...) -> kubernetes.client.V1alpha1PodPreset:
        ...
    def replace_namespaced_pod_preset(self, name: str, namespace: str, body: kubernetes.client.V1alpha1PodPreset, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1alpha1PodPreset:
        ...
    def delete_namespaced_pod_preset(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., dryRun: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ...) -> kubernetes.client.V1Status:
        ...
    def patch_namespaced_pod_preset(self, name: str, namespace: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.V1alpha1PodPreset:
        ...
    def list_pod_preset_for_all_namespaces(self, *, allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., pretty: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.V1alpha1PodPresetList:
        ...
