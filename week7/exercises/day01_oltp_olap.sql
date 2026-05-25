SELECT * 
FROM orders 
WHERE order_id = 12345;

INSERT INTO orders (order_id, customer_id, amount, status) 
VALUES (12346, 999, 150.00, 'pending');

UPDATE orders 
SET status = 'shipped' 
WHERE order_id = 12345;

SELECT 
    region, 
    SUM(revenue) AS total_revenue, 
    COUNT(DISTINCT customer_id) AS unique_customers
FROM fact_orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY region;
