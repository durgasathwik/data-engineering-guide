-- Setup script for Week 3
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS transactions;

CREATE TABLE customers (
    customer_id INTEGER,
    name TEXT,
    city TEXT,
    age INTEGER,
    updated_at TIMESTAMP
);

CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    order_date DATE,
    amount REAL,
    status TEXT
);

CREATE TABLE transactions (
    transaction_id TEXT,
    customer_id INTEGER,
    status TEXT,
    amount REAL,
    updated_at TIMESTAMP,
    source_system TEXT
);

-- Insert sample data for customers
INSERT INTO customers VALUES (1, 'Ravi', 'Hyderabad', 25, '2024-01-10');
INSERT INTO customers VALUES (2, 'Asha', 'Chennai', 30, '2024-01-12');
INSERT INTO customers VALUES (3, 'Imran', 'Hyderabad', 22, '2024-01-11');
INSERT INTO customers VALUES (1, 'Ravi', 'Hyderabad', 26, '2024-02-01');

-- Insert sample data for orders
INSERT INTO orders VALUES (101, 1, '2024-01-01', 500, 'completed');
INSERT INTO orders VALUES (102, 2, '2024-02-01', 700, 'completed');
INSERT INTO orders VALUES (103, 1, '2024-03-01', 300, 'returned');
INSERT INTO orders VALUES (104, 3, '2024-03-05', 250, 'completed');

-- Insert sample data for transactions (Mini Project)
INSERT INTO transactions VALUES ('T001', 1, 'initiated', 1000, '2024-03-01 10:00:00', 'APP');
INSERT INTO transactions VALUES ('T001', 1, 'pending', 1000, '2024-03-01 10:05:00', 'CORE');
INSERT INTO transactions VALUES ('T001', 1, 'completed', 1000, '2024-03-01 10:10:00', 'CORE');
INSERT INTO transactions VALUES ('T002', 2, 'initiated', 500, '2024-03-02 11:00:00', 'APP');
INSERT INTO transactions VALUES ('T002', 2, 'failed', 500, '2024-03-02 11:15:00', 'GATEWAY');
