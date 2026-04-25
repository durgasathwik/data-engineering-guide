SELECT city, COUNT(*) FROM customers GROUP BY city;

SELECT city, COUNT(*) as customer_count 
FROM customers 
GROUP BY city;

SELECT c.city, SUM(o.amount) as total_amount 
FROM customers c 
INNER JOIN orders o ON c.id = o.customer_id 
GROUP BY c.city;


SELECT city, COUNT(*) FROM customers GROUP BY city HAVING COUNT(*) > 1;

SELECT city, COUNT(*) as customer_count 
FROM customers 
GROUP BY city 
HAVING COUNT(*) > 1;
