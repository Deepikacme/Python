<<<<<<< HEAD
def separate_numbers(*numbers):
    even=[]
    odd=[]

    for num in numbers:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    print("Even Numbers:",even)
    print("Odd Numbers:",odd)
separate_numbers(1,2,3,4,5,6,7,8)
=======
data = ([10, 20], [30, 40])
data[0].append(50)
data[1][0] = 100
print(data)
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
