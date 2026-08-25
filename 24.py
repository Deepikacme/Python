def even_numbers(numbers):
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even
print(even_numbers([1, 2, 3, 4, 5, 6]))