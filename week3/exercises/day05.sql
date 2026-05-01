-- Day 5: Deduplication and Latest-Record Selection

-- Deduplicate by keeping the latest version of each customer record based on updated_at
WITH ranked_customers AS (
    SELECT 
        customer_id, 
        name, 
        city, 
        age, 
        updated_at,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY updated_at DESC
        ) AS rn
    FROM customers
)
SELECT 
    customer_id, 
    name, 
    city, 
    age, 
    updated_at
FROM ranked_customers
WHERE rn = 1;
