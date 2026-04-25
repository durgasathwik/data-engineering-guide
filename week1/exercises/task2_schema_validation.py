import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
INPUT_FILE = os.path.join(DATA_DIR, "products_raw.csv")

EXPECTED_COLUMNS = ["Product ID", "Product Name", "Category", "Price", "Stock"]

def validate_schema_and_count():
    total_rows = 0
    valid_rows = 0
    invalid_rows = 0
    
    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        

        actual_columns = reader.fieldnames
        if actual_columns != EXPECTED_COLUMNS:
            print(f"Schema mismatch!\nExpected: {EXPECTED_COLUMNS}\nGot: {actual_columns}")
            return
            
        print("Schema is valid.")
        
        for row in reader:
            total_rows += 1
            

            if not row.get("Product ID") or not row.get("Price"):
                invalid_rows += 1
            else:
                valid_rows += 1
                
    print(f"Total Rows: {total_rows}")
    print(f"Valid Rows: {valid_rows}")
    print(f"Invalid Rows: {invalid_rows}")

if __name__ == "__main__":
    validate_schema_and_count()
