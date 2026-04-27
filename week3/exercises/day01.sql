WITH completed_orders AS (
    SELECT *
    FROM orders
    WHERE status = 'completed'
)
SELECT * FROM completed_orders;

WITH recent_orders AS (
    SELECT *
    FROM orders
    WHERE order_date > '2024-02-01'
)
SELECT * FROM recent_orders;
