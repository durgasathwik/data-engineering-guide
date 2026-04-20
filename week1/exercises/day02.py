student = {
    "name": "Asha",
    "age": 15,
    "grade": "10th"
}
print(student["name"])

product = {
    "id": 101,
    "name": "Notebook",
    "category": "Stationery",
    "price": 45
}
print(product["price"])

def clean_age(age):
    if age == "":
        return 0
    return int(age)

value = clean_age("15")
print(value)

def uppercase_product(name):
    return name.upper()

print(uppercase_product("mouse"))

with open("notes.txt", "w") as file:
    file.write("First line\nSecond line\n")

with open("notes.txt", "r") as file:
    content = file.read()
print(content)

with open("test.txt", "w") as file:
    file.write("Line one\nLine two\n")

with open("test.txt", "r") as file:
    print(file.read())
