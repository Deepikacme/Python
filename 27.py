def check_palindrome(text):
    if text==text[::-1]:
        return"Palindrome"
    else:
        return"Not Palindrome"
print(check_palindrome("madam"))