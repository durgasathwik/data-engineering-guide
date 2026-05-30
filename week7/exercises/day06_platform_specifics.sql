COPY stg_billing_raw 
FROM 's3://data-lake/billing/2024-01-15/' 
IAM_ROLE 'arn:aws:iam::123:role/RedshiftS3Role' 
CSV IGNOREHEADER 1;

LOAD DATA INTO billing_dataset.stg_billing_raw
FROM FILES(
  format = 'CSV',
  uris = ['gs://data-lake/billing/2024-01-15/*.csv']
);

COPY INTO stg_billing_raw
FROM 'https://datalake.blob.core.windows.net/billing/2024-01-15/'
WITH (
    FILE_TYPE = 'CSV',
    FIRSTROW = 2
);
