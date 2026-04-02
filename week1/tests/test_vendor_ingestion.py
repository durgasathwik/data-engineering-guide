"""Tests for Week 1 assignment ingestion."""

from __future__ import annotations

from pathlib import Path

from week1.assignment.vendor_ingestion import ingest_directory

_SAMPLE = Path(__file__).resolve().parents[1] / "data" / "sample"


def test_ingest_sample_counts_and_schema() -> None:
    records, errors = ingest_directory(_SAMPLE)
    assert len(records) == 10
    assert len(errors) == 5
    for rec in records:
        assert set(rec.keys()) == {
            "product_id",
            "product_name",
            "price",
            "category",
            "stock_qty",
            "vendor",
        }
        assert isinstance(rec["price"], float)
        assert isinstance(rec["stock_qty"], int)


def test_dedupe_duplicate_product_same_vendor() -> None:
    records, _ = ingest_directory(_SAMPLE)
    keys = [(r["product_id"], r["vendor"]) for r in records]
    assert len(keys) == len(set(keys))
