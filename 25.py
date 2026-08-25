def odd_numbers(numbers):
    odd = []
    for num in numbers:
        if num % 2 != 0:
            odd.append(num)
    return odd
print(odd_numbers([1, 2, 3, 4, 5, 6]))