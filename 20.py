<<<<<<< HEAD
def largest(numbers):
    large=numbers[0]

    for num in numbers:
        if num>large:
            large=num
    return large
print(largest([10, 25, 15, 40, 30]))
=======
numbers=[10,50,20,40]
smallest=numbers[0]
for i in numbers:
    if i < smallest:
        smallest=i
print(smallest)
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
