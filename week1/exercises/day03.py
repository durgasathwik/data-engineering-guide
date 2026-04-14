import csv
import json
from pathlib import Path

base = Path(__file__).resolve().parent.parent

data = base / "data"
out = data / "output"
out.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    names = []
    rows = []
    with open(data / "students.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            names.append(row["name"])
            rows.append(row)
            print(row)

    print(names)

    student = {"id": 1, "name": "Ravi", "age": 15}
    with open(out / "student.json", "w") as f:
        json.dump(student, f, indent=4)
        f.write("\n")

    with open(out / "students.json", "w") as f:
        json.dump(rows, f, indent=2)
        f.write("\n")
