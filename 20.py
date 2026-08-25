def largest(numbers):
    large=numbers[0]

    for num in numbers:
        if num>large:
            large=num
    return large
print(largest([10, 25, 15, 40, 30]))