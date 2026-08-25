def number_square(numbers):
    result={}
    for n in numbers:
        result[n]=n*n
    return result
numbers=[2, 3, 4, 5]
print(number_square(numbers))