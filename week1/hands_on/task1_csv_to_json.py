#!/usr/bin/env python3
"""
Task 1 — CSV → JSON cleaner

Read a CSV, strip whitespace from headers, convert headers to snake_case, replace
empty/missing cell values with None (JSON null), write a JSON array of objects.

Usage:
  python task1_csv_to_json.py --input ../data/sample/vendor_a.csv --output ../data/output/task1.json
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


def _snake_case(name: str) -> str:
    s = name.strip()
    s = re.sub(r"[^\w\s]", "", s)
    s = re.sub(r"\s+", "_", s)
    s = re.sub(r"_+", "_", s)
    return s.strip("_").lower()


def _clean_value(value: str | None) -> Any:
    if value is None:
        return None
    stripped = value.strip()
    return None if stripped == "" else stripped


def csv_to_records(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return []
        fieldnames = [_snake_case(h or "") for h in reader.fieldnames]
        rows: list[dict[str, Any]] = []
        for raw in reader:
            row: dict[str, Any] = {}
            for canon_key, orig in zip(fieldnames, reader.fieldnames or []):
                row[canon_key] = _clean_value(raw.get(orig))
            rows.append(row)
        return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert CSV to cleaned JSON.")
    parser.add_argument("--input", "-i", type=Path, required=True)
    parser.add_argument("--output", "-o", type=Path, required=True)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    records = csv_to_records(args.input)
    with args.output.open("w", encoding="utf-8") as out:
        json.dump(records, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
