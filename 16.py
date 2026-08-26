<<<<<<< HEAD
def check_palindrome(n):
    original=n
    reverse=0
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n=n//10
    if original==reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(check_palindrome(121))
=======
numbers=[1,2,3,4,5,6]
for i in numbers:
    if i%2==0:
        print(i)
>>>>>>> b4f0831a8fc11de192ce451b32bfc96cd339302a
