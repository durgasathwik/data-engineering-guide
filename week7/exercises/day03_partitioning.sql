CREATE TABLE billing_dataset.fact_billing (
    invoice_id STRING,
    customer_id STRING,
    invoice_amount NUMERIC,
    invoice_date DATE
)
PARTITION BY invoice_date
CLUSTER BY customer_id;

CREATE TABLE fact_billing_rs (
    invoice_id VARCHAR(50) NOT NULL,
    customer_id VARCHAR(50) DISTKEY,
    invoice_amount DECIMAL(12,2),
    invoice_date DATE
)
SORTKEY(invoice_date);

CREATE TABLE fact_billing_syn (
    invoice_id NVARCHAR(50),
    customer_id NVARCHAR(50),
    invoice_amount DECIMAL(12,2),
    invoice_date DATE
)
WITH (
    DISTRIBUTION = HASH(customer_id),
    CLUSTERED COLUMNSTORE INDEX
);
