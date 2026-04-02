"""Tests for hands-on Task 2 schema validator."""

from __future__ import annotations

from pathlib import Path

import pytest

from week1.hands_on.task2_schema_validator import TypeName, validate_csv_schema

_FIXTURE_DIR = Path(__file__).resolve().parents[1] / "data" / "sample"


def test_vendor_a_headers_and_row_count() -> None:
    path = _FIXTURE_DIR / "vendor_a.csv"
    expected = ["ProductID", "ProductName", "Price", "Category", "Stock"]
    types: dict[str, TypeName] = {
        "ProductID": "str",
        "ProductName": "str",
        "Price": "float",
        "Category": "str",
        "Stock": "float",
    }
    result = validate_csv_schema(
        path,
        expected,
        types,
        optional_columns=frozenset({"Stock"}),
    )
    assert result.row_count == 4
    assert result.ok
    assert not result.header_errors


def test_invalid_price_fails() -> None:
    path = _FIXTURE_DIR / "vendor_b.csv"
    expected = ["sku", "product_title", "price_usd", "cat", "qty_on_hand"]
    types: dict[str, TypeName] = {c: "str" for c in expected}
    types["price_usd"] = "float"
    types["qty_on_hand"] = "float"
    result = validate_csv_schema(path, expected, types)
    assert not result.ok
    assert any("invalid" in e.lower() or "failed" in e.lower() for e in result.row_errors)
