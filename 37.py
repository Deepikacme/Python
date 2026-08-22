products = [
    ("Pen", 10, 5),
    ("Book", 50, 2)
]
for product in products:
    total=product[1] * product[2]
    print(product[0], total)