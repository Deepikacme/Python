<<<<<<< HEAD
def even_numbers(numbers):
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even
print(even_numbers([1, 2, 3, 4, 5, 6]))
=======
numbers=[10,20,10,30,20,40]
new_list=[]
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
