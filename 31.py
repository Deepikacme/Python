def total_price(price, tax=18):
    total=price + (price * tax / 100)
    return total
print(total_price(1000))