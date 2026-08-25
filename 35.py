def largest(*numbers):
    large = numbers[0]
    for num in numbers:
        if num > large:
            large = num
    return large
print(largest(10, 50, 25, 70, 30))