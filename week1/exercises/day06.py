import os
import csv
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

MISSING_STOCK_PATH = os.path.join(DATA_DIR, "products_missing_stock.csv")
EXPECTED_COLUMNS = ["product_id", "product_name", "category", "price", "stock"]

def validate_file(filepath, expected_cols):
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        headers = next(reader, [])
        
        if headers != expected_cols:
            print(f"Validation failed: Headers do not match. Expected {expected_cols}, got {headers}")
            return False
            
        row_count = sum(1 for row in reader)
        print(f"Validation passed. Found {row_count} rows.")
        return True

validate_file(MISSING_STOCK_PATH, EXPECTED_COLUMNS)

CUSTOMERS_PATH = os.path.join(DATA_DIR, "customers_raw.csv")
LOG_PATH = os.path.join(DATA_DIR, "customer_processing.log")
logging.basicConfig(filename=LOG_PATH, level=logging.ERROR)

print("Processing customers:")
with open(CUSTOMERS_PATH, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            age = int(row["age"])
            print(f"Valid age for {row['name']}: {age}")
        except ValueError:
            logging.error(f"Invalid age '{row['age']}' for customer_id {row['customer_id']}")
            print(f"Skipping bad data for customer_id {row['customer_id']}")
