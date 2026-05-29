SELECT 
    invoice_date, 
    customer_id, 
    SUM(invoice_amount) AS daily_revenue
FROM fact_billing 
WHERE invoice_date >= '2024-01-01' 
  AND customer_segment = 'Enterprise'
GROUP BY 1, 2;

SELECT APPROX_COUNT_DISTINCT(customer_id) 
FROM fact_billing;

SELECT 
    segment, 
    total_revenue 
FROM rpt_monthly_revenue 
WHERE month = '2024-01-01';
