"""Row-level validation for canonical product records."""

from __future__ import annotations


class ValidationError(Exception):
    """Raised when a canonical row fails validation."""

    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def validate_canonical_row(row: dict[str, str], *, line_hint: int | None = None) -> None:
    """
    Validate string-valued canonical row before typing.

    Rules:
    - product_id and product_name must be non-empty
    - price must parse to float > 0
    - stock_qty must parse to int >= 0
    """
    pid = (row.get("product_id") or "").strip()
    pname = (row.get("product_name") or "").strip()
    if not pid:
        raise ValidationError(_msg("missing product_id", line_hint))
    if not pname:
        raise ValidationError(_msg("missing product_name", line_hint))

    price_raw = (row.get("price") or "").strip()
    if not price_raw:
        raise ValidationError(_msg("missing price", line_hint))
    try:
        price = float(price_raw)
    except ValueError as exc:
        raise ValidationError(_msg(f"invalid price: {price_raw!r}", line_hint)) from exc
    if price <= 0:
        raise ValidationError(_msg(f"non-positive price: {price}", line_hint))

    qty_raw = (row.get("stock_qty") or "").strip()
    if not qty_raw:
        raise ValidationError(_msg("missing stock_qty", line_hint))
    try:
        qty = int(float(qty_raw))
    except ValueError as exc:
        raise ValidationError(_msg(f"invalid stock_qty: {qty_raw!r}", line_hint)) from exc
    if qty < 0:
        raise ValidationError(_msg(f"negative stock_qty: {qty}", line_hint))


def _msg(text: str, line_hint: int | None) -> str:
    if line_hint is None:
        return text
    return f"line {line_hint}: {text}"
