import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
INPUT_FILE = os.path.join(DATA_DIR, "products_raw.csv")
OUTPUT_FILE = os.path.join(DATA_DIR, "products_clean.json")

def process_data():
    clean_data = []
    with open(INPUT_FILE, "r") as f:
        reader = csv.DictReader(f)
        

        headers = reader.fieldnames
        standard_headers = [h.strip().lower().replace(" ", "_") for h in headers]
        
        for row in reader:
            clean_row = {}
            for old_col, new_col in zip(headers, standard_headers):
                val = row[old_col].strip() if row[old_col] else ""
                

                if not val:
                    if new_col in ["price", "stock"]:
                        val = 0
                    else:
                        val = "Unknown"
                else:
                    if new_col in ["price", "stock"]:
                        try:
                            val = float(val) if '.' in val else int(val)
                        except ValueError:
                            val = 0
                
                clean_row[new_col] = val
                
            clean_data.append(clean_row)
            
    with open(OUTPUT_FILE, "w") as f:
        json.dump(clean_data, f, indent=4)
        
    print(f"Processed {len(clean_data)} rows and saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    process_data()
