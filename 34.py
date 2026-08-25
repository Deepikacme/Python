def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(total_sum(10, 20, 30, 40))