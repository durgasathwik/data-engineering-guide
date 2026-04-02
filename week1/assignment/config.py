"""
Per-vendor CSV layout: delimiter, source header → canonical column names.

Canonical output schema:
  product_id, product_name, price (float), category, stock_qty (int), vendor (str)
"""

from __future__ import annotations

from typing import TypedDict


class VendorConfig(TypedDict):
    """Configuration for one vendor file (matched by filename stem)."""

    delimiter: str
    column_map: dict[str, str]


# Keys in column_map are stripped header names as they appear in the file.
VENDOR_CONFIGS: dict[str, VendorConfig] = {
    "vendor_a": {
        "delimiter": ",",
        "column_map": {
            "ProductID": "product_id",
            "ProductName": "product_name",
            "Price": "price",
            "Category": "category",
            "Stock": "stock_qty",
        },
    },
    "vendor_b": {
        "delimiter": ",",
        "column_map": {
            "sku": "product_id",
            "product_title": "product_name",
            "price_usd": "price",
            "cat": "category",
            "qty_on_hand": "stock_qty",
        },
    },
    "vendor_c": {
        "delimiter": ",",
        "column_map": {
            "ID": "product_id",
            "Name": "product_name",
            "Price": "price",
            "Category": "category",
            "Qty": "stock_qty",
        },
    },
    "vendor_d": {
        "delimiter": "|",
        "column_map": {
            "product_code": "product_id",
            "description": "product_name",
            "unit_price": "price",
            "dept": "category",
            "units": "stock_qty",
        },
    },
    "vendor_e": {
        "delimiter": ",",
        "column_map": {
            "ITEM_SKU": "product_id",
            "ITEM_NAME": "product_name",
            "LIST_PRICE": "price",
            "CAT_CODE": "category",
            "AVAILABLE": "stock_qty",
        },
    },
}

DEFAULTS: dict[str, str | int | float] = {
    "category": "UNKNOWN",
    "stock_qty": 0,
}
