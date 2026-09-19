<<<<<<< HEAD
def average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
print(average([10, 20, 30, 40, 50]))
=======
numbers=[1,2,3,4,5,6]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even:",even)
print("Odd:",odd)
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
