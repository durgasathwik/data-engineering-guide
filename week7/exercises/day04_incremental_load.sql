TRUNCATE TABLE fact_billing;

INSERT INTO fact_billing 
SELECT * FROM stg_billing_raw;

MERGE INTO fact_billing AS target 
USING stg_billing_raw AS source 
ON target.invoice_id = source.invoice_id 
WHEN MATCHED THEN 
    UPDATE SET 
        invoice_amount = source.invoice_amount, 
        invoice_date = source.invoice_date 
WHEN NOT MATCHED THEN 
    INSERT (invoice_id, customer_id, invoice_amount, invoice_date) 
    VALUES (source.invoice_id, source.customer_id, source.invoice_amount, source.invoice_date);
