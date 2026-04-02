#!/usr/bin/env python3
"""
Task 3 — Bad-record logger (continue on failure)

Read a CSV row-by-row. For each row, attempt to parse `price` as float and `qty` as int.
Rows that fail validation are appended to a log file (JSON lines: line number, row, reason).
Good rows are collected and printed as a count at the end.

Usage:
  python task3_bad_record_logger.py --input ../data/sample/vendor_b.csv --bad-log ../data/output/bad_rows.jsonl
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
from pathlib import Path
from typing import Any


def _parse_row(raw: dict[str, str]) -> tuple[dict[str, Any] | None, str | None]:
    price_raw = (raw.get("price_usd") or "").strip()
    qty_raw = (raw.get("qty_on_hand") or "").strip()
    if not price_raw:
        return None, "missing_price"
    try:
        price = float(price_raw)
    except ValueError:
        return None, "invalid_price"
    if price < 0:
        return None, "negative_price"
    if not qty_raw:
        return None, "missing_qty"
    try:
        qty = int(qty_raw)
    except ValueError:
        return None, "invalid_qty"
    if qty < 0:
        return None, "negative_qty"
    return {"sku": raw.get("sku", "").strip(), "price": price, "qty": qty}, None


def process_with_bad_log(
    input_path: Path,
    bad_log_path: Path,
    *,
    log: logging.Logger | None = None,
) -> tuple[int, int]:
    log = log or logging.getLogger("task3")
    bad_log_path.parent.mkdir(parents=True, exist_ok=True)
    good = 0
    bad = 0
    with input_path.open(newline="", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        with bad_log_path.open("a", encoding="utf-8") as f_bad:
            for line_no, row in enumerate(reader, start=2):
                parsed, reason = _parse_row(row)
                if parsed is not None:
                    good += 1
                    continue
                bad += 1
                record = {"line": line_no, "row": row, "reason": reason}
                f_bad.write(json.dumps(record, ensure_ascii=False) + "\n")
                log.warning("bad row line %s: %s", line_no, reason)
    return good, bad


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    log = logging.getLogger("task3")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=Path, required=True)
    parser.add_argument("--bad-log", "-b", type=Path, required=True)
    args = parser.parse_args()

    if args.bad_log.exists():
        args.bad_log.unlink()

    good, bad = process_with_bad_log(args.input, args.bad_log, log=log)
    print(f"good_rows={good} bad_rows={bad} bad_log={args.bad_log}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
