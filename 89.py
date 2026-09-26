import json

f = open("products.json", "r")
products = json.load(f)
f.close()

total = 0

for product in products:
    total += product["price"] * product["quantity"]

print("Total inventory value:", total)