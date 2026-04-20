import os
import csv
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_CSV_PATH = os.path.join(DATA_DIR, "products_raw.csv")
OUT_JSON_PATH = os.path.join(DATA_DIR, "products_clean.json")

def dummy_main():
    os.environ["DATA_FOLDER"] = DATA_DIR 
    folder = os.getenv("DATA_FOLDER")
    print("Data folder is:", folder)

def run_pipeline():
    clean_products = []
    
    with open(RAW_CSV_PATH, "r") as file:
        reader = csv.DictReader(file)
        
        headers = reader.fieldnames
        cleaned_headers = [h.strip().lower().replace(" ", "_") for h in headers]
        
        for row in reader:
            clean_row = {}
            for old_key, new_key in zip(headers, cleaned_headers):
                val = row[old_key]
                if val == "":
                    if new_key == "price":
                        val = "0"
                    elif new_key == "stock":
                        val = "0"
                clean_row[new_key] = val
            clean_products.append(clean_row)

    with open(OUT_JSON_PATH, "w") as out_file:
        json.dump(clean_products, out_file, indent=4)
        
    print(f"Pipeline finished. Cleaned {len(clean_products)} products.")

if __name__ == "__main__":
    dummy_main()
    run_pipeline()
