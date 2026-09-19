<<<<<<< HEAD
def largest(*numbers):
    large = numbers[0]
    for num in numbers:
        if num > large:
            large = num
    return large
print(largest(10, 50, 25, 70, 30))
=======
a = 10
b = 20
a, b = b, a
print(a)
print(b)
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
