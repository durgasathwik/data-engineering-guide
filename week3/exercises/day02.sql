-- Day 2: Window Function - ROW_NUMBER

-- Rank customers by age within each city
SELECT 
    name, 
    city, 
    age, 
    ROW_NUMBER() OVER (PARTITION BY city ORDER BY age DESC) AS city_age_rank 
FROM customers;

-- Rank orders by amount within each customer_id
SELECT 
    order_id, 
    customer_id, 
    amount, 
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS amount_rank 
FROM orders;

-- Find the highest amount order per customer
WITH ranked_orders AS (
    SELECT 
        order_id, 
        customer_id, 
        amount, 
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rn
    FROM orders
)
SELECT * FROM ranked_orders WHERE rn = 1;
