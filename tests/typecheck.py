from decimal import Decimal
from typing import assert_type

from kubernetes import client
from kubernetes.utils import parse_quantity
from kubernetes.utils.quantity import format_quantity


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

quantity = parse_quantity("1Gi")
assert_type(quantity, Decimal)
assert_type(format_quantity(quantity, "Gi"), str)
