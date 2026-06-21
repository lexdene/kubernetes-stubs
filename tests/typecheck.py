from decimal import Decimal
from typing import assert_type

from kubernetes.utils import parse_quantity
from kubernetes.utils.quantity import format_quantity

quantity = parse_quantity("1Gi")
assert_type(quantity, Decimal)
assert_type(format_quantity(quantity, "Gi"), str)
