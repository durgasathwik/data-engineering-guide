-- Day 3: RANK, DENSE_RANK, LAG, and LEAD

-- Difference between ROW_NUMBER, RANK, and DENSE_RANK
SELECT 
    customer_id, 
    amount, 
    ROW_NUMBER() OVER (ORDER BY amount DESC) as row_num,
    RANK() OVER (ORDER BY amount DESC) as rank_val,
    DENSE_RANK() OVER (ORDER BY amount DESC) as dense_rank_val
FROM orders;

-- LAG: compare each order amount with the previous order amount per customer
SELECT 
    customer_id, 
    order_date, 
    amount, 
    LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_order_amount 
FROM orders;

-- LEAD: see the next order date for each customer
SELECT 
    customer_id, 
    order_date, 
    amount, 
    LEAD(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS next_order_date 
FROM orders;
