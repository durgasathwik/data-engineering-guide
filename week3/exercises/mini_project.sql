-- Week 3 Mini Project: Fintech Transaction Reporting

-- Task 1: Deduplication - Get the latest valid transaction state
WITH latest_transactions AS (
    SELECT 
        transaction_id, 
        customer_id, 
        status, 
        amount, 
        updated_at,
        source_system,
        ROW_NUMBER() OVER (
            PARTITION BY transaction_id 
            ORDER BY updated_at DESC
        ) as rn
    FROM transactions
)
SELECT 
    transaction_id, 
    customer_id, 
    status, 
    amount, 
    updated_at, 
    source_system 
FROM latest_transactions 
WHERE rn = 1;

-- Task 2: Trend Analysis - Track status changes over time for each transaction
SELECT 
    transaction_id, 
    customer_id, 
    status, 
    updated_at,
    LAG(status) OVER (
        PARTITION BY transaction_id 
        ORDER BY updated_at ASC
    ) as previous_status
FROM transactions;
