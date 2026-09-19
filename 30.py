<<<<<<< HEAD
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
=======
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
