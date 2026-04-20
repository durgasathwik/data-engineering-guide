import os
import csv
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

V1_PATH = os.path.join(DATA_DIR, "vendor1.csv")
V2_PATH = os.path.join(DATA_DIR, "vendor2.csv")
V3_PATH = os.path.join(DATA_DIR, "vendor3.csv")
OUTPUT_PATH = os.path.join(DATA_DIR, "unified_catalog.json")

def process_vendor(filepath, id_col, name_col, category_col, price_col):
    results = []
    if not os.path.exists(filepath):
        return results

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            price_val = row.get(price_col, "").strip()
            price = float(price_val) if price_val != "" else 0.0
            
            results.append({
                "product_id": row.get(id_col, "").strip(),
                "name": row.get(name_col, "").strip(),
                "category": row.get(category_col, "").strip(),
                "price": price
            })
    return results

def main():
    print("Starting the Mini Project...")
    all_products = []
    
    # Process Vendor 1
    v1_data = process_vendor(V1_PATH, id_col="Product ID", name_col="Product Name", category_col="Category", price_col="Price")
    all_products.extend(v1_data)
    
    # Process Vendor 2
    v2_data = process_vendor(V2_PATH, id_col="id", name_col="name", category_col="category", price_col="price")
    all_products.extend(v2_data)
    
    # Process Vendor 3
    v3_data = process_vendor(V3_PATH, id_col="item_code", name_col="item_name", category_col="item_group", price_col="cost")
    all_products.extend(v3_data)
    
    # Deduplicate by product_id
    unique_products = {}
    for p in all_products:
        pid = p["product_id"]
        if pid not in unique_products:
            unique_products[pid] = p

    final_list = list(unique_products.values())
    
    with open(OUTPUT_PATH, "w") as out:
        json.dump(final_list, out, indent=4)
        
    print(f"Successfully processed and merged catalogs! Total unique products: {len(final_list)}")

if __name__ == "__main__":
    main()
