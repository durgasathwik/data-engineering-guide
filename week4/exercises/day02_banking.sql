-- Day 2: Entities, Attributes, and Keys (Banking App Example)

-- Customer Table (Surrogate Primary Key)
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY, -- Surrogate Key
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,       -- Natural Key candidate
    phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Account Table (Surrogate Primary Key, Foreign Key to Customer)
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,   -- Surrogate Key
    customer_id INTEGER NOT NULL,     -- Foreign Key
    account_number TEXT UNIQUE NOT NULL, -- Natural Key candidate
    account_type TEXT CHECK(account_type IN ('Savings', 'Checking')),
    balance REAL DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Payment/Transaction Table
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    transaction_type TEXT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);
