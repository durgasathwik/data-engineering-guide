# Day 5: Normalization vs Denormalization

## OLTP (Online Transaction Processing)
- **Design**: Highly Normalized.
- **Goal**: Fast writes and data consistency.
- **Example**: Splitting customer data into `customers`, `addresses`, and `geography` tables to avoid redundancy.

## OLAP (Online Analytical Processing)
- **Design**: Denormalized (Star/Snowflake Schema).
- **Goal**: Fast reads and simple reporting.
- **Example**: Creating a wide `dim_customer` table that pre-joins address and city information for easy slicing in a dashboard.
