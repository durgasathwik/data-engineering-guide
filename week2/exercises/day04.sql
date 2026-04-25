SELECT * FROM customers WHERE age IS NULL;

SELECT * FROM customers WHERE age IS NULL OR city IS NULL;


SELECT name, 
CASE 
    WHEN age > 18 THEN 'Adult' 
    ELSE 'Minor' 
END as category
FROM customers;

SELECT name, age,
CASE 
    WHEN age >= 30 THEN 'Senior'
    WHEN age >= 18 THEN 'Adult'
    ELSE 'Minor'
END as age_classification
FROM customers;
