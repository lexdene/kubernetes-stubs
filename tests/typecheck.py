from decimal import Decimal
from typing import assert_type

from kubernetes import client
from kubernetes.utils import parse_quantity
from kubernetes.utils.quantity import format_quantity
from kubernetes.watch import Watch


class _Response:
    @property
    def data(self) -> bytes:
        return b"{}"


assert_type(client.Configuration(), client.Configuration)
custom_api = client.CustomObjectsApi()
api_client = custom_api.api_client
assert_type(api_client, client.ApiClient)
assert_type(
    api_client.call_api(
        "/apis/{group}/{version}",
        "GET",
        path_params={"group": "example.com", "version": "v1"},
        response_types_map={200: "V1Pod"},
    ),
    object,
)
assert_type(api_client.deserialize(_Response(), client.V1Pod), client.V1Pod)
assert_type(api_client.deserialize(_Response(), "V1Pod"), object)
assert_type(client.ApiClient(pool_threads=4), client.ApiClient)

api = client.CoreV1Api()
inferred_item = next(Watch().stream(api.list_namespaced_pod, "default"))
# ty's generic-protocol constraint solving still produces Unknown here:
# https://github.com/astral-sh/ty/issues/623
if inferred_item is not None:
    if inferred_item["type"] == "BOOKMARK":
        bookmark_object = inferred_item["object"]
        assert_type(bookmark_object, object)  # ty: ignore[type-assertion-failure]
    else:
        pod_object = inferred_item["object"]
        assert_type(pod_object, client.V1Pod)  # ty: ignore[type-assertion-failure]

fixed_item = next(Watch(client.V1Pod).stream(api.list_namespaced_config_map, "default"))
if fixed_item is not None and fixed_item["type"] != "BOOKMARK":
    fixed_object = fixed_item["object"]
    assert_type(fixed_object, client.V1Pod)  # ty: ignore[type-assertion-failure]

raw_item = next(Watch().stream(api.list_namespaced_pod, "default", deserialize=False))
assert_type(raw_item, object)
log_item = next(Watch().stream(api.read_namespaced_pod_log, "pod", "default"))
assert_type(log_item, object)

Watch().stream(api.list_namespaced_pod)  # type: ignore[call-overload]  # ty: ignore[no-matching-overload]

quantity = parse_quantity("1Gi")
assert_type(quantity, Decimal)
assert_type(format_quantity(quantity, "Gi"), str)
