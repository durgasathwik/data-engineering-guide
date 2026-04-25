import csv
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
INPUT_FILE = os.path.join(DATA_DIR, "products_raw.csv")
LOG_FILE = os.path.join(DATA_DIR, "bad_records.log")
OUTPUT_FILE = os.path.join(DATA_DIR, "valid_products.csv")


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_with_logging():
    valid_records = []
    
    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        
        for row_num, row in enumerate(reader, start=2):
            try:
                product_id = row.get("Product ID", "").strip()
                price = row.get("Price", "").strip()
                

                if not product_id:
                    raise ValueError(f"Missing Product ID on row {row_num}")
                if not price:
                    raise ValueError(f"Missing Price for Product ID '{product_id}' on row {row_num}")
                    

                float(price)
                
                valid_records.append(row)
                
            except Exception as e:
                logging.error(f"Bad record encountered: {str(e)} | Data: {row}")

                continue
                

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(valid_records)
        
    print(f"Finished processing. Valid records saved to {OUTPUT_FILE}. Bad records logged to {LOG_FILE}.")

if __name__ == "__main__":
    process_with_logging()
