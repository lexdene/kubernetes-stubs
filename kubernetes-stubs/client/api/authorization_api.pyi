import typing

import kubernetes.client

class AuthorizationApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
