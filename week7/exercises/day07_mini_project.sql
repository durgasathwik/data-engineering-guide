TRUNCATE TABLE stg_billing_raw;

COPY stg_billing_raw 
FROM 's3://data-lake/billing/2024-01-15/' 
IAM_ROLE 'arn:aws:iam::123:role/RedshiftS3Role' 
CSV IGNOREHEADER 1;

SELECT 
    COUNT(*) AS total_rows, 
    SUM(CASE WHEN invoice_id IS NULL THEN 1 ELSE 0 END) AS null_invoice_ids, 
    SUM(CASE WHEN invoice_amount IS NULL THEN 1 ELSE 0 END) AS null_amounts 
FROM stg_billing_raw;

MERGE INTO fact_billing AS target 
USING stg_billing_raw AS source 
ON target.invoice_id = source.invoice_id 
WHEN MATCHED THEN 
    UPDATE SET 
        invoice_amount = CAST(source.invoice_amount AS DECIMAL(12,2)), 
        invoice_date = CAST(source.invoice_date AS DATE) 
WHEN NOT MATCHED THEN 
    INSERT (invoice_id, customer_id, invoice_amount, invoice_date) 
    VALUES (
        source.invoice_id, 
        source.customer_id, 
        CAST(source.invoice_amount AS DECIMAL(12,2)), 
        CAST(source.invoice_date AS DATE)
    );

DELETE FROM rpt_monthly_revenue 
WHERE month = DATE_TRUNC('month', CURRENT_DATE);

INSERT INTO rpt_monthly_revenue 
SELECT 
    DATE_TRUNC('month', invoice_date) AS month, 
    c.customer_segment, 
    SUM(f.invoice_amount) AS total_revenue, 
    COUNT(DISTINCT f.customer_id) AS active_customers 
FROM fact_billing f 
JOIN dim_customer c ON f.customer_id = c.customer_id 
WHERE invoice_date >= DATE_TRUNC('month', CURRENT_DATE) 
GROUP BY 1, 2;
