import typing

import kubernetes.client

class AppsV1beta1Api:
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList:
        ...
    def list_controller_revision_for_all_namespaces(self, *, allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., pretty: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1ControllerRevisionList:
        ...
    def list_deployment_for_all_namespaces(self, *, allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., pretty: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.AppsV1beta1DeploymentList:
        ...
    def list_namespaced_controller_revision(self, namespace: str, *, pretty: typing.Optional[str] = ..., allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1ControllerRevisionList:
        ...
    def create_namespaced_controller_revision(self, namespace: str, body: kubernetes.client.V1beta1ControllerRevision, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1beta1ControllerRevision:
        ...
    def delete_collection_namespaced_controller_revision(self, namespace: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., continue: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ...) -> kubernetes.client.V1Status:
        ...
    def read_namespaced_controller_revision(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ..., exact: typing.Optional[bool] = ..., export: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1ControllerRevision:
        ...
    def replace_namespaced_controller_revision(self, name: str, namespace: str, body: kubernetes.client.V1beta1ControllerRevision, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1beta1ControllerRevision:
        ...
    def delete_namespaced_controller_revision(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., dryRun: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ...) -> kubernetes.client.V1Status:
        ...
    def patch_namespaced_controller_revision(self, name: str, namespace: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1ControllerRevision:
        ...
    def list_namespaced_deployment(self, namespace: str, *, pretty: typing.Optional[str] = ..., allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.AppsV1beta1DeploymentList:
        ...
    def create_namespaced_deployment(self, namespace: str, body: kubernetes.client.AppsV1beta1Deployment, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.AppsV1beta1Deployment:
        ...
    def delete_collection_namespaced_deployment(self, namespace: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., continue: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ...) -> kubernetes.client.V1Status:
        ...
    def read_namespaced_deployment(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ..., exact: typing.Optional[bool] = ..., export: typing.Optional[bool] = ...) -> kubernetes.client.AppsV1beta1Deployment:
        ...
    def replace_namespaced_deployment(self, name: str, namespace: str, body: kubernetes.client.AppsV1beta1Deployment, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.AppsV1beta1Deployment:
        ...
    def delete_namespaced_deployment(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., dryRun: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ...) -> kubernetes.client.V1Status:
        ...
    def patch_namespaced_deployment(self, name: str, namespace: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.AppsV1beta1Deployment:
        ...
    def create_namespaced_deployment_rollback(self, name: str, namespace: str, body: kubernetes.client.AppsV1beta1DeploymentRollback, *, dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., pretty: typing.Optional[str] = ...) -> kubernetes.client.V1Status:
        ...
    def read_namespaced_deployment_scale(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...) -> kubernetes.client.AppsV1beta1Scale:
        ...
    def replace_namespaced_deployment_scale(self, name: str, namespace: str, body: kubernetes.client.AppsV1beta1Scale, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.AppsV1beta1Scale:
        ...
    def patch_namespaced_deployment_scale(self, name: str, namespace: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.AppsV1beta1Scale:
        ...
    def read_namespaced_deployment_status(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...) -> kubernetes.client.AppsV1beta1Deployment:
        ...
    def replace_namespaced_deployment_status(self, name: str, namespace: str, body: kubernetes.client.AppsV1beta1Deployment, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.AppsV1beta1Deployment:
        ...
    def patch_namespaced_deployment_status(self, name: str, namespace: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.AppsV1beta1Deployment:
        ...
    def list_namespaced_stateful_set(self, namespace: str, *, pretty: typing.Optional[str] = ..., allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1StatefulSetList:
        ...
    def create_namespaced_stateful_set(self, namespace: str, body: kubernetes.client.V1beta1StatefulSet, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1beta1StatefulSet:
        ...
    def delete_collection_namespaced_stateful_set(self, namespace: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., continue: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ...) -> kubernetes.client.V1Status:
        ...
    def read_namespaced_stateful_set(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ..., exact: typing.Optional[bool] = ..., export: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1StatefulSet:
        ...
    def replace_namespaced_stateful_set(self, name: str, namespace: str, body: kubernetes.client.V1beta1StatefulSet, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1beta1StatefulSet:
        ...
    def delete_namespaced_stateful_set(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ..., body: typing.Optional[kubernetes.client.V1DeleteOptions] = ..., dryRun: typing.Optional[str] = ..., gracePeriodSeconds: typing.Optional[int] = ..., orphanDependents: typing.Optional[bool] = ..., propagationPolicy: typing.Optional[str] = ...) -> kubernetes.client.V1Status:
        ...
    def patch_namespaced_stateful_set(self, name: str, namespace: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1StatefulSet:
        ...
    def read_namespaced_stateful_set_scale(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...) -> kubernetes.client.AppsV1beta1Scale:
        ...
    def replace_namespaced_stateful_set_scale(self, name: str, namespace: str, body: kubernetes.client.AppsV1beta1Scale, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.AppsV1beta1Scale:
        ...
    def patch_namespaced_stateful_set_scale(self, name: str, namespace: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.AppsV1beta1Scale:
        ...
    def read_namespaced_stateful_set_status(self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...) -> kubernetes.client.V1beta1StatefulSet:
        ...
    def replace_namespaced_stateful_set_status(self, name: str, namespace: str, body: kubernetes.client.V1beta1StatefulSet, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ...) -> kubernetes.client.V1beta1StatefulSet:
        ...
    def patch_namespaced_stateful_set_status(self, name: str, namespace: str, body: typing.Any, *, pretty: typing.Optional[str] = ..., dryRun: typing.Optional[str] = ..., fieldManager: typing.Optional[str] = ..., force: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1StatefulSet:
        ...
    def list_stateful_set_for_all_namespaces(self, *, allowWatchBookmarks: typing.Optional[bool] = ..., continue: typing.Optional[str] = ..., fieldSelector: typing.Optional[str] = ..., labelSelector: typing.Optional[str] = ..., limit: typing.Optional[int] = ..., pretty: typing.Optional[str] = ..., resourceVersion: typing.Optional[str] = ..., timeoutSeconds: typing.Optional[int] = ..., watch: typing.Optional[bool] = ...) -> kubernetes.client.V1beta1StatefulSetList:
        ...
