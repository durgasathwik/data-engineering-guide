#!/usr/bin/env python3
"""
Task 2 — Schema and row-count validation

Validate that a CSV's headers match expected names (after stripping) and that each
row's values are compatible with expected types: str, int, float.

Returns a structured result dict suitable for logging or tests.

Usage:
  python task2_schema_validator.py --input ../data/sample/vendor_a.csv
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal


TypeName = Literal["str", "int", "float"]


@dataclass
class SchemaValidationResult:
    ok: bool
    row_count: int
    header_errors: list[str] = field(default_factory=list)
    row_errors: list[str] = field(default_factory=list)


def _coerce(
    value: str | None, typ: TypeName, *, optional: bool = False
) -> tuple[bool, str | None]:
    if value is None or (isinstance(value, str) and value.strip() == ""):
        if optional:
            return True, ""
        return False, "empty"
    v = value.strip()
    if typ == "str":
        return True, v
    if typ == "int":
        try:
            int(v)
            return True, v
        except ValueError:
            return False, "invalid_int"
    if typ == "float":
        try:
            float(v)
            return True, v
        except ValueError:
            return False, "invalid_float"
    return False, "unknown_type"


def validate_csv_schema(
    path: Path,
    expected_headers: list[str],
    column_types: dict[str, TypeName],
    *,
    optional_columns: frozenset[str] | None = None,
) -> SchemaValidationResult:
    header_errors: list[str] = []
    row_errors: list[str] = []
    row_count = 0
    optional_columns = optional_columns or frozenset()

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        raw_headers = [h.strip() if h else "" for h in (reader.fieldnames or [])]
        if raw_headers != expected_headers:
            header_errors.append(
                f"header_mismatch: got {raw_headers!r} want {expected_headers!r}"
            )

        for i, row in enumerate(reader, start=2):
            row_count += 1
            for col, typ in column_types.items():
                if col not in row and col not in (reader.fieldnames or []):
                    row_errors.append(f"line {i}: missing column {col!r}")
                    continue
                val = row.get(col)
                ok, _ = _coerce(val, typ, optional=col in optional_columns)
                if not ok:
                    row_errors.append(f"line {i}: column {col!r} failed type {typ!r}")

    ok = not header_errors and not row_errors
    return SchemaValidationResult(
        ok=ok,
        row_count=row_count,
        header_errors=header_errors,
        row_errors=row_errors,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path, required=True)
    args = parser.parse_args()

    expected = ["ProductID", "ProductName", "Price", "Category", "Stock"]
    types: dict[str, TypeName] = {
        "ProductID": "str",
        "ProductName": "str",
        "Price": "float",
        "Category": "str",
        "Stock": "float",
    }
    result = validate_csv_schema(
        args.input,
        expected,
        types,
        optional_columns=frozenset({"Stock"}),
    )
    print("ok:", result.ok)
    print("row_count:", result.row_count)
    print("header_errors:", result.header_errors)
    print("row_errors:", result.row_errors[:10])
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
