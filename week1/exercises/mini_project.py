import csv
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_FILE = os.path.join(DATA_DIR, "mini_project_errors.log")
OUTPUT_FILE = os.path.join(DATA_DIR, "unified_products.csv")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

VENDORS = [
    {
        "file": "vendor1.csv",
        "mapping": {"Product ID": "product_id", "Product Name": "product_name", "Price": "price", "Category": "category"}
    },
    {
        "file": "vendor2.csv",
        "mapping": {"id": "product_id", "name": "product_name", "price": "price", "category": "category"}
    },
    {
        "file": "vendor3.csv",
        "mapping": {"item_code": "product_id", "item_name": "product_name", "cost": "price", "item_group": "category"}
    }
]

def run_ingestion():
    unified_data = {}
    
    for vendor in VENDORS:
        filepath = os.path.join(DATA_DIR, vendor["file"])
        if not os.path.exists(filepath):
            logging.error(f"File not found: {filepath}")
            continue
            
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            
            for row_num, row in enumerate(reader, start=2):
                try:

                    mapped_row = {}
                    for old_col, new_col in vendor["mapping"].items():
                        mapped_row[new_col] = row.get(old_col, "").strip()
                        

                    product_id = mapped_row["product_id"]
                    price = mapped_row["price"]
                    
                    if not product_id:
                        raise ValueError(f"Missing product_id in {vendor['file']} on row {row_num}")
                    
                    if not price:
                        mapped_row["price"] = "0"
                    
                    if not mapped_row["category"]:
                        mapped_row["category"] = "Unknown"
                    

                    if product_id not in unified_data:
                        unified_data[product_id] = mapped_row
                    else:
                        logging.warning(f"Duplicate product_id {product_id} found in {vendor['file']} on row {row_num}, skipping.")
                        
                except Exception as e:
                    logging.error(f"Bad record in {vendor['file']}: {str(e)} | Data: {row}")
                    continue
                    

    with open(OUTPUT_FILE, "w", newline="") as f:
        fieldnames = ["product_id", "product_name", "category", "price"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in unified_data.values():
            writer.writerow(record)
            
    print(f"Ingestion complete. {len(unified_data)} unique records saved to {OUTPUT_FILE}.")

if __name__ == "__main__":
    run_ingestion()
