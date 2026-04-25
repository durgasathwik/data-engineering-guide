SELECT * FROM customers ORDER BY age DESC;

SELECT * FROM customers ORDER BY age ASC;

SELECT * FROM customers ORDER BY name ASC;

SELECT c.name, o.amount 
FROM customers c 
INNER JOIN orders o ON c.id = o.customer_id;

SELECT * 
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id;

SELECT c.name, o.amount
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id;
