import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
student_csv_path = os.path.join(DATA_DIR, "students.csv")

with open(student_csv_path, "w") as f:
    f.write("id,name,city\n1,Ravi,Hyderabad\n2,Asha,Chennai\n3,Imran,Bangalore\n")

with open(student_csv_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

with open(student_csv_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])

student = {
    "id": 1,
    "name": "Ravi",
    "age": 15
}
json_path = os.path.join(DATA_DIR, "student.json")
with open(json_path, "w") as file:
    json.dump(student, file, indent=4)

product_data = {
    "product_id": 99,
    "item": "Keyboard",
    "price": 2500
}
output_json = os.path.join(DATA_DIR, "product.json")
with open(output_json, "w") as file:
    json.dump(product_data, file, indent=4)
