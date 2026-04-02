"""CSV normalization, canonical mapping, deduplication helpers."""

from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Any, Callable, Iterable

from .config import DEFAULTS, VendorConfig


def strip_row_keys(row: dict[str | None, str | None]) -> dict[str, str]:
    """Strip dictionary keys and string values."""
    out: dict[str, str] = {}
    for k, v in row.items():
        key = (k or "").strip()
        if isinstance(v, str):
            out[key] = v.strip()
        elif v is None:
            out[key] = ""
        else:
            out[key] = str(v)
    return out


def map_to_canonical(
    row: dict[str, str],
    column_map: dict[str, str],
) -> dict[str, str]:
    """Map vendor-specific keys to canonical names; ignore unmapped keys."""
    canonical: dict[str, str] = {}
    for src, dest in column_map.items():
        if src in row:
            canonical[dest] = row[src]
    return canonical


def apply_defaults(row: dict[str, str]) -> dict[str, str]:
    """Fill missing optional fields from DEFAULTS (string form for downstream parse)."""
    merged = dict(row)
    for key, default in DEFAULTS.items():
        if key not in merged or merged[key] == "":
            merged[key] = str(default)
    return merged


def read_csv_rows(path: Path, config: VendorConfig) -> list[dict[str, str]]:
    """Load all rows with stripped header keys."""
    rows: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter=config["delimiter"])
        for raw in reader:
            rows.append(strip_row_keys(raw))
    return rows


def snake_case_header(name: str) -> str:
    """Normalize a header string to snake_case (used in hands-on task pattern)."""
    s = name.strip()
    s = re.sub(r"[^\w\s]", "", s)
    s = re.sub(r"\s+", "_", s)
    return s.strip("_").lower()


def dedupe_records(
    records: list[dict[str, Any]],
    key: Callable[[dict[str, Any]], tuple[Any, ...]],
) -> list[dict[str, Any]]:
    """Keep first occurrence for each key(rec)."""
    seen: set[tuple[Any, ...]] = set()
    out: list[dict[str, Any]] = []
    for rec in records:
        k = key(rec)
        if k in seen:
            continue
        seen.add(k)
        out.append(rec)
    return out


def sorted_csv_paths(directory: Path) -> list[Path]:
    """Return sorted *.csv paths for deterministic ingest order."""
    return sorted(directory.glob("*.csv"))
