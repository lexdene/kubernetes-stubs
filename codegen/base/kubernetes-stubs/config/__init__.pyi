from typing import Optional

from kubernetes.client import Configuration
from kubernetes.config.config_exception import ConfigException
from kubernetes.config.incluster_config import load_incluster_config
from kubernetes.config.kube_config import (KUBE_CONFIG_DEFAULT_LOCATION,
                                           list_kube_config_contexts,
                                           load_kube_config,
                                           load_kube_config_from_dict,
                                           new_client_from_config)

__all__ = [
    "ConfigException",
    "load_config",
    "load_incluster_config",
    "KUBE_CONFIG_DEFAULT_LOCATION",
    "list_kube_config_contexts",
    "load_kube_config",
    "load_kube_config_from_dict",
    "new_client_from_config",
]


def load_config(
    config_file: Optional[str] = ...,
    kube_config_path: Optional[str] = ...,
    context: Optional[str] = ...,
    client_configuration: Optional[Configuration] = ...,
    persist_config: bool = ...,
    try_refresh_token: bool = ...,
) -> None: ...
