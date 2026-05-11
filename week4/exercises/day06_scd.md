# Day 6: Star Schema & Slowly Changing Dimensions (SCD)

## SCD Type 1: Overwrite
- **Use Case**: Fixing incorrect data (e.g., misspelled name).
- **Result**: Historical record is lost.

## SCD Type 2: Add New Row
- **Use Case**: Tracking historical changes (e.g., customer moves to a new city).
- **Result**: Both old and new data are preserved.
- **Attributes**: `effective_start_date`, `effective_end_date`, `is_current`.
