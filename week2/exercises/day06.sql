

SELECT 
    c.name, 
    COUNT(o.order_id) as total_orders, 
    COALESCE(SUM(o.amount), 0) as total_revenue
FROM 
    customers c
LEFT JOIN 
    orders o ON c.id = o.customer_id
GROUP BY 
    c.name
ORDER BY 
    total_revenue DESC;
