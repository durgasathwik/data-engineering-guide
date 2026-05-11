-- Week 4 Mini Project: E-commerce Warehouse Model (Star Schema)

-- 1. Dimension Tables (The "Slicing" data)

CREATE TABLE dim_customer (
    customer_sk INTEGER PRIMARY KEY, -- Surrogate Key
    customer_id INTEGER NOT NULL,    -- Natural Key from source
    name TEXT,
    email TEXT,
    city TEXT,
    region TEXT,
    is_current BOOLEAN,              -- For SCD Type 2
    effective_start_date DATE,
    effective_end_date DATE
);

CREATE TABLE dim_product (
    product_sk INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    product_name TEXT,
    category TEXT,
    brand TEXT,
    current_price REAL
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY, -- e.g., 20240101
    full_date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER,
    is_holiday BOOLEAN
);

CREATE TABLE dim_promotion (
    promo_sk INTEGER PRIMARY KEY,
    promo_id TEXT,
    promo_name TEXT,
    discount_percentage REAL
);

-- 2. Fact Table (The "Measuring" data)
-- Grain: One row represents one product line item within an order

CREATE TABLE fact_sales (
    sales_id INTEGER PRIMARY KEY,
    order_id INTEGER,                -- Degenerate dimension
    customer_sk INTEGER,
    product_sk INTEGER,
    date_key INTEGER,
    promo_sk INTEGER,
    quantity INTEGER,
    unit_price REAL,
    discount_amount REAL,
    net_revenue REAL,
    FOREIGN KEY (customer_sk) REFERENCES dim_customer(customer_sk),
    FOREIGN KEY (product_sk) REFERENCES dim_product(product_sk),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (promo_sk) REFERENCES dim_promotion(promo_sk)
);
