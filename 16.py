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