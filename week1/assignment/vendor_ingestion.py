"""Orchestrate multi-file vendor catalog ingestion."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from .config import VENDOR_CONFIGS
from .utils import (
    apply_defaults,
    dedupe_records,
    map_to_canonical,
    read_csv_rows,
    sorted_csv_paths,
)
from .validators import ValidationError, validate_canonical_row

log = logging.getLogger(__name__)


def _coerce_types(row: dict[str, str]) -> dict[str, Any]:
    """Convert validated string row to typed output."""
    return {
        "product_id": row["product_id"].strip(),
        "product_name": row["product_name"].strip(),
        "price": float(row["price"]),
        "category": (row.get("category") or "").strip() or "UNKNOWN",
        "stock_qty": int(float(row["stock_qty"])),
        "vendor": row["vendor"],
    }


def ingest_directory(input_dir: Path) -> tuple[list[dict[str, Any]], list[str]]:
    """
    Read all configured vendor CSV files, validate rows, dedupe by (product_id, vendor).

    Returns (good_records, bad_messages).
    """
    good: list[dict[str, Any]] = []
    bad: list[str] = []

    for path in sorted_csv_paths(input_dir):
        stem = path.stem
        cfg = VENDOR_CONFIGS.get(stem)
        if cfg is None:
            log.warning("skip unconfigured file: %s", path.name)
            continue

        rows = read_csv_rows(path, cfg)
        for idx, raw in enumerate(rows, start=2):
            canonical_strings = map_to_canonical(raw, cfg["column_map"])
            filled = apply_defaults(canonical_strings)
            filled["vendor"] = stem
            try:
                validate_canonical_row(filled, line_hint=idx)
                good.append(_coerce_types(filled))
            except ValidationError as exc:
                msg = f"{path.name}:{exc}"
                bad.append(msg)
                log.warning("%s", msg)

    deduped = dedupe_records(good, key=lambda r: (r["product_id"], r["vendor"]))
    return deduped, bad
