from pathlib import Path

if __name__ == "__main__":
    print("Hello, student")
    print("Welcome to Week 1")

    my_name = "Ravi"
    my_city = "Hyderabad"
    print(my_name)
    print(my_city)

    product_name = "notebook"
    price = 45
    stock = 12
    is_active = True
    print(product_name, price, stock, is_active)

    if price > 100:
        print("expensive")
    else:
        print("ok")

    cities = ["Hyderabad", "Chennai", "Bangalore"]
    for c in cities:
        print(c)
