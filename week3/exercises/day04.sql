-- Day 4: Subqueries and Correlated Subqueries

-- Find customers who have placed at least one order using a subquery
SELECT name 
FROM customers 
WHERE customer_id IN (
    SELECT customer_id 
    FROM orders
);

-- Rewrite the same idea using a JOIN
SELECT DISTINCT c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;
