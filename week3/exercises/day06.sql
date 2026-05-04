-- Day 6: Query Optimization Basics

-- Select only required columns instead of SELECT *
SELECT 
    customer_id, 
    amount, 
    order_date 
FROM orders 
WHERE status = 'completed';

-- Filter early before performing aggregations
SELECT 
    customer_id, 
    SUM(amount) as total_spent
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY customer_id;

-- Conceptual Index Example:
-- Adding an index on (status, order_date) would speed up the first query.
-- CREATE INDEX idx_order_status_date ON orders(status, order_date);
