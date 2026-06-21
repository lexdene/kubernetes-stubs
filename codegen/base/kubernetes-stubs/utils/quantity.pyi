from decimal import Decimal

def parse_quantity(quantity: object) -> Decimal: ...
def format_quantity(
    quantity_value: Decimal,
    suffix: str,
    quantize: Decimal | None = ...,
) -> str: ...
