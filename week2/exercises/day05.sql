
SELECT * FROM customers;

SELECT * FROM customers WHERE city = 'Bangalore';

SELECT c.name, o.amount 
FROM customers c 
INNER JOIN orders o ON c.id = o.customer_id;

SELECT c.name, COUNT(o.order_id) as total_orders 
FROM customers c 
LEFT JOIN orders o ON c.id = o.customer_id 
GROUP BY c.name;

SELECT * FROM customers 
WHERE name IS NULL OR age IS NULL OR city IS NULL;
