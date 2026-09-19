def even_odd_count(numbers):
    even=0
    odd=0
    for n in numbers:
        if n%2==0:
            even+=1
        else:
            odd+=1
    return {"even":even,"odd":odd}
numbers=[1,2,3,4,5,6,8]
print(even_odd_count(numbers))
    