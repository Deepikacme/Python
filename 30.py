def largest_smallest(numbers):
    large = numbers[0]
    small = numbers[0]
    for num in numbers:
        if num > large:
            large = num
        if num < small:
            small = num
    return large, small
result=largest_smallest([10,5,25,15,2])
print("Largest:",result[0])
print("Smallest:",result[1])