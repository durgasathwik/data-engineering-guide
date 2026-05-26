CREATE TABLE stg_billing_raw (
    invoice_id VARCHAR(50),
    customer_id VARCHAR(50),
    invoice_amount VARCHAR(50),
    invoice_date VARCHAR(50),
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fact_billing (
    billing_key BIGINT IDENTITY PRIMARY KEY,
    invoice_id VARCHAR(50) NOT NULL,
    customer_key BIGINT NOT NULL,
    invoice_amount DECIMAL(12,2) NOT NULL,
    invoice_date DATE NOT NULL
);

CREATE TABLE rpt_monthly_revenue AS
SELECT 
    DATE_TRUNC('month', invoice_date) AS month,
    customer_segment,
    SUM(invoice_amount) AS total_revenue
FROM fact_billing f
JOIN dim_customer c ON f.customer_key = c.customer_key
GROUP BY 1, 2;
