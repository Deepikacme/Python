import json

products = [
    {"name": "Pen", "price": 10, "quantity": 5},
    {"name": "Book", "price": 50, "quantity": 3}
]

f = open("products.json", "w")
json.dump(products, f, indent=4)
f.close()

print("Product file created")