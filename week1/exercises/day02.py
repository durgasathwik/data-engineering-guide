from pathlib import Path

data = Path(__file__).resolve().parent.parent / "data"


def upper_name(name):
    return name.upper()


if __name__ == "__main__":
    product = {
        "id": 101,
        "name": "USB Cable",
        "category": "Electronics",
        "price": 199,
    }
    print(product["price"])

    print(upper_name("keyboard"))

    notes_path = data / "notes.txt"
    with open(notes_path, "r") as f:
        text = f.read()
    print(text.strip())
