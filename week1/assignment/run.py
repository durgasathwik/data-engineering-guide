#!/usr/bin/env python3
"""CLI entry point for vendor catalog ingestion."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from .vendor_ingestion import ingest_directory


def _configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(levelname)s %(name)s: %(message)s",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ingest vendor CSVs into one JSON file.")
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        required=True,
        help="Directory containing vendor_*.csv files",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        required=True,
        help="Output JSON path for the curated catalog",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Logging level (DEBUG, INFO, WARNING, ERROR)",
    )
    args = parser.parse_args(argv)

    _configure_logging(args.log_level)

    records, errors = ingest_directory(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "record_count": len(records),
        "errors": errors,
        "records": records,
    }
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    log = logging.getLogger("run")
    log.info("wrote %s records to %s", len(records), args.output)
    if errors:
        log.warning("skipped %s bad rows", len(errors))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
